> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# NVIDIA NeMo Agent Toolkit 集成

> 如何将 NVIDIA NeMo Agent Toolkit 与 Bright Data 的 The Bright Data MCP 服务器集成，以增强 AI 代理功能。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

## 概述

NVIDIA NeMo Agent Toolkit 是一个用于构建、分析和优化 AI 代理和工作流的开源框架。它提供与框架无关的架构、基于 YAML 的配置、内置 MCP 支持以及跨多代理系统的统一监控。

## 托管 MCP

<Steps>
  <Step title="获取您的 API 令牌">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 令牌（格式如下：`2dceb1aa0***************************`）
  </Step>

  <Step title="安装 NeMo Agent Toolkit">
    ```bash theme={null}
    pip install nvidia-nat[mcp]
    ```
  </Step>

  <Step title="创建工作流配置">
    创建一个名为 `brightdata-mcp-config.yml` 的文件：

    ```yaml expandable theme={null}
    function_groups:
      brightdata_web:
        _type: mcp_client
        server:
          transport: streamable-http
          url: "https://mcp.brightdata.com/mcp?token=<YOUR_BRIGHTDATA_API_TOKEN>"
        tool_call_timeout: 120  # Increase timeout for web requests
        auth_flow_timeout: 300
        reconnect_enabled: true
        reconnect_max_attempts: 3


    llms:
      nim_llm:
        _type: nim
        model_name: "meta/llama-3.1-8b-instruct"
        temperature: 0.0
        api_key: "${env:NVIDIA_API_KEY}"

    workflow:
      _type: react_agent
      tool_names:
        - brightdata_web
      llm_name: nim_llm
      max_iterations: 10
      verbose: true
    ```

    将 `YOUR_BRIGHTDATA_API_TOKEN` 替换为第 1 步中的实际令牌。
  </Step>

  <Step title="设置环境变量">
    ```bash theme={null}
    # 设置您的 NVIDIA API 密钥（用于 NIM 或 NGC）
    export NVIDIA_API_KEY="your-nvidia-api-key"
    ```
  </Step>

  <Step title="验证 MCP 连接">
    测试与 Bright Data 的 MCP 服务器的连接：

    ```bash theme={null}
    nat mcp client ping --url "https://mcp.brightdata.com/mcp?token=YOUR_BRIGHTDATA_API_TOKEN"
    ```

    预期输出：

    ```
    Successfully connected to MCP server
    Server version: 1.0
    Available tools: 15
    ```
  </Step>

  <Step title="列出可用工具">
    检查 Bright Data MCP 提供的工具：

    ```bash theme={null}
    nat mcp client tool list --url "https://mcp.brightdata.com/mcp?token=YOUR_TOKEN"
    ```
  </Step>

  <Step title="运行您的第一个代理">
    使用查询执行工作流：

    ```bash theme={null}
    nat run --config_file brightdata-mcp-config.yml \
      --input "Search for the latest NVIDIA GPU releases and extract their specifications"
    ```

    代理将使用 Bright Data 的网页抓取工具来搜索和提取信息。
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 仪表板中的 [My Zones](https://www.bright.cn/cp/zones) 查看您的 API 使用情况
    2. 您的免费层包括每月 5,000 个请求
    3. 使用以下命令在日志中监控工具调用：`nat run --config_file brightdata-mcp-config.yml`
  </Step>
</Steps>

## 资源

* [NeMo Agent Toolkit 文档](https://docs.nvidia.com/nemo/agent-toolkit/)
* [NeMo Agent Toolkit GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit)
* [Bright Data MCP 文档](/mcp-server/)
