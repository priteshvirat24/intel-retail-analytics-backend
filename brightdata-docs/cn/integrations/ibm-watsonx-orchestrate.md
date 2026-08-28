> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IBM Watsonx Orchestrate

> 通过 MCP Server 方法，将 Bright Data 强大的网页抓取和数据提取能力集成到 IBM watsonx Orchestrate 中。

## 概述

此集成为您的代理提供企业级的网页抓取能力，以及带有反机器人保护绕过功能的多引擎搜索操作。

## 前置条件

在开始之前，请确保您拥有：

* IBM watsonx Orchestrate 的访问权限
* 一个有效订阅的 Bright Data 账号
* 您的 Bright Data API 密钥

## 入门步骤

<Steps>
  <Step title="获取 Bright Data API 密钥">
    * 登录到您的 [Bright Data 控制面板](https://www.bright.cn/cp)
    * 进入 [账户设置](https://www.bright.cn/cp/setting/users)
    * 如果尚未生成，[生成一个 API 密钥](/cn/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)
    * 复制并安全保存您的 API 密钥，用于接下来的步骤
  </Step>

  <Step title="打开 Agent 工具集">
    * 在 IBM watsonx Orchestrate 中导航到 **Manage Agents**
    * 选择您的代理
    * 在左侧菜单中点击 **Toolset**
    * 点击 **Add Tool**

          <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at10.12.52.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=e49c0ec24c00835bb73e97ba930ca74c" alt="Screenshot 2025-10-20 at 10.12.52.png" width="872" height="373" data-path="images/Screenshot2025-10-20at10.12.52.png" />
  </Step>

  <Step title="添加 MCP Server 连接">
    在 “Add tool” 对话框中：

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at10.14.58.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=6a43ba42ae0d67061e9b5a59187abd49" alt="Screenshot 2025-10-20 at 10.14.58.png" width="686" height="482" data-path="images/Screenshot2025-10-20at10.14.58.png" />

    * 选择 **Add from file or MCP server**
    * 选择 **Import from MCP Server**
    * 填写配置字段：
      * **Name**：填写描述性的名称（例如：`Bright Data MCP`）
      * **Connection**：选择 `None`
      * **Install Command**：输入以下命令，将 `<your_api_token>` 替换为您的实际密钥：

    ```bash theme={null}
    npx mcp-remote https://mcp.brightdata.com/sse?token=<your_api_token>
    ```

    * 点击 **Install** 启动连接
  </Step>

  <Step title="启用可用的功能">
    安装完成后，多个功能会显示在代理的工具集中。请启用以下内容：

    `search_engine`

    `scrape_as_markdown`
  </Step>

  <Step title="测试您的连接">
    验证集成是否成功：

    * 打开代理的聊天界面
    * 让代理执行一个简单任务（例如：“Search for recent AI trends”）
    * 确认代理能够成功从 Bright Data 检索并处理数据
  </Step>
</Steps>

## 下一步

您的代理现已连接至 Bright Data，可用于：

* 从主要平台提取结构化数据
* 执行地理定向的网页搜索
* 在绕过机器人保护的情况下抓取网站内容
* 处理大规模数据提取任务

## 支持

需要帮助？请联系 Bright Data 支持团队，或参考 [Bright Data 文档](/cn) 获取更详细的 API 参考和故障排查指南。
