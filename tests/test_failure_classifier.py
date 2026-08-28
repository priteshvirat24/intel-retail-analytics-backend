import pytest
from app.evaluation.failures import FailureClassifier
from app.crawlers.base import CrawlerResponse
from app.models.failure import FailureCategory, SpecificReason, CrawlStage


def test_classify_captcha_challenge():
    resp = CrawlerResponse(
        url="https://example.com/item",
        final_url="https://example.com/item",
        status_code=403,
        html="<html><body><h1>Please verify you are a human</h1><div class='g-recaptcha'></div></body></html>",
        is_captcha=True
    )
    diag = FailureClassifier.classify_crawl_failure(resp, stage=CrawlStage.CONTENT_AVAILABILITY)
    assert diag.category == FailureCategory.ACCESS
    assert diag.specific_reason == SpecificReason.CAPTCHA_CHALLENGE
    assert diag.stage == CrawlStage.CONTENT_AVAILABILITY
    assert "CAPTCHA" in diag.failure_reason_human


def test_classify_bot_protection():
    resp = CrawlerResponse(
        url="https://example.com/item",
        final_url="https://example.com/item",
        status_code=403,
        html="<html><body><h1>Access Denied</h1><p>Protected by Cloudflare</p></body></html>",
        is_blocked=True
    )
    diag = FailureClassifier.classify_crawl_failure(resp, stage=CrawlStage.URL_REACHABILITY)
    assert diag.category in (FailureCategory.ACCESS, FailureCategory.HTTP_STATUS)
    assert diag.specific_reason == SpecificReason.BOT_PROTECTION


def test_classify_javascript_required():
    resp = CrawlerResponse(
        url="https://example.com/item",
        final_url="https://example.com/item",
        status_code=200,
        html="<html><body><noscript>You need to enable JavaScript to run this app.</noscript></body></html>"
    )
    diag = FailureClassifier.classify_crawl_failure(resp, stage=CrawlStage.CONTENT_AVAILABILITY)
    assert diag.category == FailureCategory.CONTENT
    assert diag.specific_reason == SpecificReason.JAVASCRIPT_REQUIRED
    assert diag.stage == CrawlStage.CONTENT_AVAILABILITY
    assert diag.recommended_escalation == "PLAYWRIGHT"


def test_classify_http_404():
    resp = CrawlerResponse(
        url="https://example.com/item",
        final_url="https://example.com/item",
        status_code=404,
        html="<html><body>404 Not Found</body></html>"
    )
    diag = FailureClassifier.classify_crawl_failure(resp, stage=CrawlStage.URL_REACHABILITY)
    assert diag.category == FailureCategory.HTTP_STATUS
    assert diag.specific_reason == SpecificReason.HTTP_404_NOT_FOUND
    assert diag.is_recoverable is False
