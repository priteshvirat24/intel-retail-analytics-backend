import argparse
import asyncio
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional
import yaml
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from app.models.registry import TargetRegistry, CanonicalTarget
from app.models.crawl_result import TargetCrawlReport
from app.orchestrator.engine import CrawlOrchestrator
from app.orchestrator.manifest import ManifestManager
from app.reporting.json_report import JsonReportGenerator
from app.reporting.csv_report import CsvReportGenerator
from app.reporting.html_report import HtmlReportGenerator
from app.reporting.benchmark_summary import BenchmarkSummaryGenerator
from app.evidence.store import EvidenceStore

console = Console()


async def run_targets(
    targets: List[CanonicalTarget],
    registry: TargetRegistry,
    limit: int = 20,
    strategy: str = "auto",
    headful: bool = False,
    save_evidence: bool = True,
    generate_reports: bool = True
) -> List[TargetCrawlReport]:
    """Runs orchestrator across selected retailer targets concurrently (concurrency: 5)."""
    evidence_store = EvidenceStore() if save_evidence else None
    orchestrator = CrawlOrchestrator(evidence_store=evidence_store, headful=headful)

    run_id = f"run_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    # Generate immutable run manifest
    manifest_path = ManifestManager.create_manifest(
        run_id=run_id,
        target_ids=[t.target_id for t in targets],
        sku_limit=limit,
        configuration_hash=registry.configuration_hash,
        strategies_enabled=["HTTP", "PLAYWRIGHT", "ADAPTER"]
    )
    console.print(f"[dim]Run manifest generated at: {manifest_path}[/dim]")

    console.print(f"[bold cyan]Starting evaluation across {len(targets)} retailer target(s) (Target: {limit} SKUs each, concurrency: 5)...[/bold cyan]\n")

    target_sem = asyncio.Semaphore(5)

    async def _eval_target(idx: int, target: CanonicalTarget) -> Optional[TargetCrawlReport]:
        async with target_sem:
            console.print(Panel(
                f"[bold white]{target.brand_name} ({target.country})[/bold white] - Domain: [dim]{target.domain}[/dim] | Target ID: [cyan]{target.target_id}[/cyan]",
                title=f"Target {idx + 1}/{len(targets)}"
            ))
            try:
                report = await orchestrator.crawl_target(
                    target_config=target,
                    limit=limit,
                    forced_strategy=None if strategy == "auto" else strategy.upper()
                )
                cov = round(report.sku_coverage * 100)
                grade_color = "green" if report.capability_grade in ("A", "B") else "yellow" if report.capability_grade == "C" else "red"
                console.print(
                    f"  -> [{target.target_id}] Discovered: [bold]{report.discovered}/{report.target_skus}[/bold] | "
                    f"Validated: [bold green]{report.validated_count}[/bold green] | "
                    f"Observed Coverage: [{grade_color}]{cov}%[/{grade_color}] ({report.validated_count}/{report.sample_size}) | "
                    f"Grade: [{grade_color}]{report.capability_grade}[/{grade_color}] | "
                    f"Category: [cyan]{report.capability_category}[/cyan] | "
                    f"Block: [yellow]{round(report.block_rate * 100)}%[/yellow] | "
                    f"Avg Latency: [dim]{int(report.avg_latency_ms)}ms[/dim]"
                )
                if report.main_failure_reason:
                    console.print(f"     [{target.target_id}] [dim]Main failure: {report.main_failure_reason}[/dim]")
                console.print()
                return report
            except Exception as e:
                console.print(f"[bold red]Unexpected failure crawling target {target.target_id}: {str(e)}[/bold red]\n")
                return None

    eval_tasks = [_eval_target(i, t) for i, t in enumerate(targets)]
    raw_results = await asyncio.gather(*eval_tasks)
    reports = [r for r in raw_results if r is not None]

    # Generate Reports
    if generate_reports and reports:
        json_path = JsonReportGenerator.generate(reports)
        csv_path = CsvReportGenerator.generate(reports)
        summary_path = BenchmarkSummaryGenerator.generate(reports, registry)
        html_path = HtmlReportGenerator.generate(reports)

        console.print("[bold green]Reports generated successfully:[/bold green]")
        console.print(f" - JSON: [cyan]{json_path}[/cyan]")
        console.print(f" - CSV:  [cyan]{csv_path}[/cyan]")
        console.print(f" - MD:   [cyan]{summary_path}[/cyan]")
        console.print(f" - HTML: [cyan]{html_path}[/cyan]\n")

    return reports


def print_summary_table(reports: List[TargetCrawlReport]):
    """Displays a rich terminal summary table of the crawl benchmark."""
    table = Table(title="Global Multi-Site Crawl Orchestration Benchmark", show_header=True, header_style="bold magenta")
    table.add_column("Retailer", style="bold")
    table.add_column("Country", justify="center")
    table.add_column("Grade", justify="center")
    table.add_column("Category", style="cyan")
    table.add_column("Target", justify="right")
    table.add_column("Discovered", justify="right")
    table.add_column("Validated", justify="right", style="green")
    table.add_column("Observed Coverage", justify="right")
    table.add_column("Block %", justify="right", style="yellow")
    table.add_column("Avg Latency", justify="right", style="dim")
    table.add_column("Best Strat", justify="center")

    for r in reports:
        cov = f"{round(r.sku_coverage * 100)}% ({r.validated_count}/{r.sample_size})"
        grade_style = "bold green" if r.capability_grade in ("A", "B") else "bold yellow" if r.capability_grade == "C" else "bold red"
        table.add_row(
            r.brand_name,
            r.country,
            f"[{grade_style}]{r.capability_grade}[/{grade_style}]",
            r.capability_category,
            str(r.target_skus),
            str(r.discovered),
            str(r.validated_count),
            cov,
            f"{round(r.block_rate * 100)}%",
            f"{int(r.avg_latency_ms)}ms",
            r.strategy_benchmark.best_strategy if hasattr(r, "strategy_benchmark") else r.primary_strategy
        )

    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="Multi-Site Crawl Orchestrator CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Command: list-retailers
    subparsers.add_parser("list-retailers", help="List all configured retailer targets")

    # Command: firecrawl-health
    subparsers.add_parser("firecrawl-health", help="Check status and connectivity of self-hosted Firecrawl service")

    # Command: benchmark-strategy
    strat_parser = subparsers.add_parser("benchmark-strategy", help="Run benchmark using a specific crawler strategy")
    strat_parser.add_argument("--strategy", type=str, required=True, choices=["auto", "http", "playwright", "firecrawl", "adapter", "scrapy"], help="Strategy to benchmark")
    strat_parser.add_argument("--limit", type=int, default=20, help="SKU sample limit (default: 20)")
    strat_parser.add_argument("--target", type=str, default=None, help="Optional specific target ID to test")
    strat_parser.add_argument("--headful", action="store_true", help="Run browser in headful mode")
    strat_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable HTML snapshots and logs")
    strat_parser.add_argument("--report", action="store_true", default=True, help="Generate JSON, CSV, MD, HTML reports")
    strat_parser.add_argument("--config", type=str, default="config/targets.yaml", help="Path to targets config YAML")

    # Command: benchmark-compare
    compare_parser = subparsers.add_parser("benchmark-compare", help="Run fair A/B comparison across identical real SKU URLs")
    compare_parser.add_argument("--strategies", type=str, default="http,playwright,firecrawl", help="Comma-separated strategies to compare (e.g. http,playwright,firecrawl)")
    compare_parser.add_argument("--limit", type=int, default=10, help="SKU sample limit per target (default: 10)")
    compare_parser.add_argument("--target", type=str, default=None, help="Optional specific target ID to test (default: all enabled)")
    compare_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable HTML snapshots and logs")
    compare_parser.add_argument("--report", action="store_true", default=True, help="Generate JSON, CSV, MD, HTML reports")
    compare_parser.add_argument("--config", type=str, default="config/targets.yaml", help="Path to targets config YAML")

    # Command: test-all
    test_all_parser = subparsers.add_parser("test-all", help="Test all configured retailer targets")
    test_all_parser.add_argument("--limit", type=int, default=20, help="SKU sample limit per target (default: 20)")
    test_all_parser.add_argument("--strategy", type=str, default="auto", choices=["auto", "http", "playwright", "firecrawl", "adapter", "scrapy"], help="Forced crawler strategy")
    test_all_parser.add_argument("--headful", action="store_true", help="Run browser in headful mode")
    test_all_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable HTML snapshots and logs")
    test_all_parser.add_argument("--report", action="store_true", default=True, help="Generate JSON, CSV, MD, HTML reports")
    test_all_parser.add_argument("--config", type=str, default="config/targets.yaml", help="Path to targets config YAML")

    # Command: test
    test_parser = subparsers.add_parser("test", help="Test a specific retailer target")
    test_parser.add_argument("retailer", type=str, help="Target ID (e.g. amazon-in, flipkart-in, walmart-us)")
    test_parser.add_argument("--limit", type=int, default=20, help="SKU sample limit (default: 20)")
    test_parser.add_argument("--strategy", type=str, default="auto", choices=["auto", "http", "playwright", "firecrawl", "adapter", "scrapy"], help="Forced crawler strategy")
    test_parser.add_argument("--headful", action="store_true", help="Run browser in headful mode")
    test_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable HTML snapshots and logs")
    test_parser.add_argument("--report", action="store_true", default=True, help="Generate JSON, CSV, MD, HTML reports")
    test_parser.add_argument("--config", type=str, default="config/targets.yaml", help="Path to targets config YAML")

    # Command: test-target (alias for test)
    test_target_parser = subparsers.add_parser("test-target", help="Test a specific retailer target")
    test_target_parser.add_argument("retailer", type=str, help="Target ID (e.g. amazon-in, flipkart-in, walmart-us)")
    test_target_parser.add_argument("--limit", type=int, default=20, help="SKU sample limit (default: 20)")
    test_target_parser.add_argument("--strategy", type=str, default="auto", choices=["auto", "http", "playwright", "firecrawl", "adapter", "scrapy"], help="Forced crawler strategy")
    test_target_parser.add_argument("--headful", action="store_true", help="Run browser in headful mode")
    test_target_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable HTML snapshots and logs")
    test_target_parser.add_argument("--report", action="store_true", default=True, help="Generate JSON, CSV, MD, HTML reports")
    # Command: benchmark-laptop-crawl
    laptop_parser = subparsers.add_parser("benchmark-laptop-crawl", help="Run 52-target laptop crawlability benchmark")
    laptop_parser.add_argument("--all-targets", action="store_true", default=True, help="Test all 52 enabled retailer targets")
    laptop_parser.add_argument("--all-discovery-methods", action="store_true", default=True, help="Run all 6 discovery phases")
    laptop_parser.add_argument("--strategies", type=str, default="http,playwright,firecrawl,adapter", help="Comma-separated strategies to test")
    laptop_parser.add_argument("--target", type=str, default=None, help="Optional comma-separated target IDs to test")
    laptop_parser.add_argument("--concurrency", type=int, default=4, help="Target concurrency (default: 4)")
    laptop_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save raw HTML and metadata evidence")
    laptop_parser.add_argument("--report", action="store_true", default=True, help="Generate CSV and Markdown reports")
    laptop_parser.add_argument("--config", type=str, default="config/targets.yaml", help="Path to targets config YAML")
    laptop_parser.add_argument("--run-id", type=str, default=None, help="Optional run identifier")

    # Command: benchmark-laptop-brightdata
    bd_laptop_parser = subparsers.add_parser("benchmark-laptop-brightdata", help="Run full-potential 52-target Bright Data laptop benchmark")
    bd_laptop_parser.add_argument("--all-targets", action="store_true", default=True, help="Test all 52 enabled retailer targets")
    bd_laptop_parser.add_argument("--discover", action="store_true", default=True, help="Run multi-tier laptop discovery")
    bd_laptop_parser.add_argument("--strategies", type=str, default="brightdata_unlocker,brightdata_browser,firecrawl", help="Comma-separated strategies to test")
    bd_laptop_parser.add_argument("--country-routing", action="store_true", default=True, help="Enable dynamic ISO country routing")
    bd_laptop_parser.add_argument("--multi-candidate", action="store_true", default=True, help="Evaluate multiple candidates per retailer")
    bd_laptop_parser.add_argument("--max-candidates", type=int, default=10, help="Max candidates to test per target (default: 10)")
    bd_laptop_parser.add_argument("--target", type=str, default=None, help="Optional comma-separated target IDs to test")
    bd_laptop_parser.add_argument("--concurrency", type=int, default=4, help="Target concurrency (default: 4)")
    bd_laptop_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable evidence")
    bd_laptop_parser.add_argument("--report", action="store_true", default=True, help="Generate 11-sheet Excel, CSV, JSON, MD reports")
    bd_laptop_parser.add_argument("--config", type=str, default="config/targets.yaml", help="Path to targets config YAML")

    # Command: diagnostic-amazon-brightdata
    amz_diag_parser = subparsers.add_parser("diagnostic-amazon-brightdata", help="Run dedicated Amazon multi-marketplace diagnostic")
    amz_diag_parser.add_argument("--report", action="store_true", default=True, help="Generate reports/amazon_brightdata_diagnostic.md")

    # Command: benchmark-laptop-full-potential
    fp_laptop_parser = subparsers.add_parser("benchmark-laptop-full-potential", help="Run redesigned 52-retailer full-potential Bright Data benchmark")
    fp_laptop_parser.add_argument("--all-targets", action="store_true", default=True, help="Test all 52 enabled retailer targets")
    fp_laptop_parser.add_argument("--discover", action="store_true", default=True, help="Run multi-method laptop discovery")
    fp_laptop_parser.add_argument("--max-candidates", type=int, default=10, help="Max candidates to test per target (default: 10)")
    fp_laptop_parser.add_argument("--limit", type=int, default=None, help="Limit number of targets to test")
    fp_laptop_parser.add_argument("--save-evidence", action="store_true", default=True, help="Save auditable evidence")
    fp_laptop_parser.add_argument("--report", action="store_true", default=True, help="Generate CSV, JSON, MD, and 11-sheet Excel reports")

    args = parser.parse_args()

    cfg_path = Path(getattr(args, "config", "config/targets.yaml"))
    if not cfg_path.exists():
        cfg_path = Path("config/targets.yaml")

    registry = TargetRegistry(config_path=cfg_path)

    if args.command == "firecrawl-health":
        from app.crawlers.firecrawl import FirecrawlCrawler
        from app.models.retailer import RetailerTargetConfig
        dummy_cfg = RetailerTargetConfig(
            target_id="health-check",
            retailer="firecrawl",
            brand_name="Firecrawl",
            base_url="http://localhost:3002",
            country="Global",
            domain="localhost",
            locale="en-US",
            currency="USD"
        )
        fc = FirecrawlCrawler(dummy_cfg)
        is_avail, status, details = asyncio.run(fc.check_health())
        if is_avail:
            console.print(f"[bold green]FIRECRAWL_STATUS={status}[/bold green]")
            console.print(f"Base URL: [cyan]{details.get('base_url')}[/cyan]")
            console.print(f"Endpoint: [cyan]{details.get('endpoint')}[/cyan]")
            console.print(f"Response Time: [dim]{details.get('latency_ms', 0):.2f}ms[/dim]")
            if "message" in details:
                console.print(f"Service Message: [green]{details['message']}[/green]")
        else:
            console.print(f"[bold red]FIRECRAWL_STATUS={status}[/bold red]")
            console.print(f"Base URL: [cyan]{details.get('base_url')}[/cyan]")
            console.print(f"Reason: [red]{details.get('error')}[/red]")
            console.print("[dim]Self-hosted Firecrawl instance is offline. Run 'docker compose -f firecrawl_repo/docker-compose.yaml up -d' to start the service.[/dim]")
        return

    if args.command == "benchmark-laptop-crawl":
        from app.reporting.laptop_benchmark import LaptopBenchmarkRunner
        target_list = []
        if getattr(args, "target", None):
            for tid in args.target.split(","):
                t = registry.get(tid.lower().strip())
                if t:
                    target_list.append(t)
        else:
            target_list = registry.all_targets(enabled_only=True)

        if not target_list:
            console.print(f"[bold red]No targets found matching criteria.[/bold red]")
            sys.exit(1)

        runner = LaptopBenchmarkRunner(
            targets=target_list,
            save_evidence=args.save_evidence,
            concurrency=args.concurrency
        )
        res = asyncio.run(runner.run(run_id=args.run_id))
        return

    if args.command == "benchmark-laptop-brightdata":
        from app.orchestrator.brightdata_laptop_benchmark import BrightDataLaptopBenchmarkRunner
        target_list = []
        if getattr(args, "target", None):
            for tid in args.target.split(","):
                t = registry.get(tid.lower().strip())
                if t:
                    target_list.append(t)
        else:
            target_list = registry.all_targets(enabled_only=True)

        if not target_list:
            console.print(f"[bold red]No targets found matching criteria.[/bold red]")
            sys.exit(1)

        runner = BrightDataLaptopBenchmarkRunner(
            targets=target_list,
            max_candidates=getattr(args, "max_candidates", 10),
            concurrency=getattr(args, "concurrency", 4)
        )
        res = asyncio.run(runner.run())
        return

    if args.command == "diagnostic-amazon-brightdata":
        from app.orchestrator.amazon_diagnostic_runner import AmazonDiagnosticRunner
        runner = AmazonDiagnosticRunner()
        res = asyncio.run(runner.run_diagnostic())
        return

    if args.command == "benchmark-laptop-full-potential":
        from app.orchestrator.brightdata_full_potential_orchestrator import FullPotentialLaptopOrchestrator
        target_list = registry.all_targets(enabled_only=True)
        runner = FullPotentialLaptopOrchestrator(
            targets=target_list,
            max_candidates=getattr(args, "max_candidates", 10)
        )
        res = asyncio.run(runner.run_benchmark(limit=getattr(args, "limit", None)))
        return

    if args.command == "benchmark-compare":
        from app.reporting.strategy_comparison import run_fair_strategy_comparison
        strats = [s.strip().upper() for s in args.strategies.split(",") if s.strip()]
        target_list = []
        if args.target:
            for tid in args.target.split(","):
                t = registry.get(tid.lower().strip())
                if t:
                    target_list.append(t)
        else:
            target_list = registry.all_targets(enabled_only=True)[:5]

        if not target_list:
            console.print(f"[bold red]No targets found matching criteria.[/bold red]")
            sys.exit(1)

        res = asyncio.run(run_fair_strategy_comparison(
            targets=target_list,
            strategies=strats,
            limit=args.limit,
            save_evidence=args.save_evidence
        ))
        return

    if args.command == "benchmark-strategy":
        strat_mode = args.strategy.upper()
        if args.target:
            t = registry.get(args.target.lower().strip())
            target_list = [t] if t else []
        else:
            target_list = registry.all_targets(enabled_only=True)

        if not target_list:
            console.print(f"[bold red]No targets found matching criteria.[/bold red]")
            sys.exit(1)

        reports = asyncio.run(run_targets(
            targets=target_list,
            registry=registry,
            limit=args.limit,
            strategy=strat_mode,
            headful=args.headful,
            save_evidence=args.save_evidence,
            generate_reports=args.report
        ))
        print_summary_table(reports)
        return

    if not args.command or args.command == "list-retailers":
        table = Table(
            title=f"Canonical Target Registry: {registry.unique_retailers} Brands | {registry.retailer_country_targets} Targets | {registry.countries} Countries",
            show_header=True
        )
        table.add_column("Target ID", style="cyan")
        table.add_column("Brand")
        table.add_column("Country")
        table.add_column("ISO", justify="center")
        table.add_column("Domain")
        table.add_column("Currency", justify="center")
        table.add_column("Locale")
        table.add_column("Timezone")
        for t in registry.all_targets():
            table.add_row(t.target_id, t.brand_name, t.country, t.iso_country, t.domain, t.currency, t.locale, t.timezone)
        console.print(table)
        return

    if args.command == "test-all":
        targets = registry.all_targets(enabled_only=True)
        reports = asyncio.run(run_targets(
            targets=targets,
            registry=registry,
            limit=args.limit,
            strategy=args.strategy,
            headful=args.headful,
            save_evidence=args.save_evidence,
            generate_reports=args.report
        ))
        print_summary_table(reports)

    elif args.command in ("test", "test-target"):
        target_id = args.retailer.lower().strip()
        target = registry.get(target_id)
        if not target:
            console.print(f"[bold red]Target '{target_id}' not found in canonical targets registry.[/bold red]")
            console.print(f"Available targets: {', '.join([t.target_id for t in registry.all_targets()[:10]])}...")
            sys.exit(1)

        reports = asyncio.run(run_targets(
            targets=[target],
            registry=registry,
            limit=args.limit,
            strategy=args.strategy,
            headful=args.headful,
            save_evidence=args.save_evidence,
            generate_reports=args.report
        ))
        print_summary_table(reports)


if __name__ == "__main__":
    main()
