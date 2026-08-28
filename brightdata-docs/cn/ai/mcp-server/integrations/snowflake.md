> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Snowflake 集成

> 如何将 Bright Data 的 Bright Data MCP 服务器与 Snowflake 集成，以启用安全的企业级网络自动化。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

<Steps>
  <Step title="获取您的 Bright Data API 令牌">
    1. 转到 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 令牌（格式如下：`2dceb1aa0***************************`）
    3. 妥善保管 - 连接到 MCP 时需要使用它
  </Step>

  <Step title="安装 Bright Data MCP 应用">
    1. 在您的 Snowflake 界面中导航到**应用**
    2. 找到并点击 **Bright Data MCP**
    3. 点击**安装**将该应用程序添加到您的账户
  </Step>

  <Step title="配置外部访问">
    1. 打开已安装的应用
    2. 您将看到 **Bright Data 外部访问**的请求
    3. 点击**审查**以查看网络配置
    4. 点击**连接** - 这将自动创建必要的网络规则
    5. 点击**激活**以启用外部访问集成

    该应用现在拥有运行所需的所有资源。
  </Step>

  <Step title="启动 MCP 服务并获取端点">
    启动应用程序并检索 MCP 端点 URL。

    ```sql expandable theme={null}
    -- 启动应用
    CALL <application-name>.app_public.start_app();

    -- 检查应用状态
    CALL <application-name>.app_public.service_status();

    -- 获取端点 URL
    SHOW ENDPOINTS IN SERVICE <application-name>.core.mcp_service;
    ```

    从输出中复制端点 URL — 您需要它来连接您的 MCP 客户端。
  </Step>

  <Step title="创建 Snowflake 个人访问令牌 (PAT)">
    1. 在 Snowflake 中，转到**设置**
    2. 导航到**身份验证** → **程序化访问令牌**
    3. 点击**生成新令牌**
    4. 妥善保存令牌 — 它将用于 MCP 身份验证
  </Step>

  <Step title="连接到 Bright Data MCP">
    在您的 MCP 客户端中使用以下端点格式：

    ```text theme={null}
    https://<endpoint>.snowflakecomputing.app/mcp?token=<BRIGHT_DATA_API_TOKEN>
    ```

    包含所需的身份验证标头：

    ```text theme={null}
    Authorization: Snowflake Token="YOUR_SNOWFLAKE_PAT"
    ```

    替换：

    * `<endpoint>` 为上一步中的 Snowflake 端点
    * `<BRIGHT_DATA_API_TOKEN>` 为您的 Bright Data API 令牌
    * `YOUR_SNOWFLAKE_PAT` 为您的 Snowflake 个人访问令牌
  </Step>

  <Step title="测试集成">
    1. 从您的 MCP 兼容客户端（例如 Claude Desktop）连接到 MCP 端点
    2. 调用工具，例如网页浏览或网页抓取
    3. 确认成功返回响应
  </Step>

  <Step title="监控使用情况">
    1. 在您的 Bright Data 仪表板中访问[我的区域](https://www.bright.cn/cp/zones)
    2. 跟踪请求量和使用情况
    3. 您的免费层包括**每月 5,000 个请求**
  </Step>
</Steps>
