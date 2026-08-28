> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Railway 上部署 Bright Data 和 OpenClaw

> 通过一键模板在 Railway 上部署预装 66 个 Bright Data 网络工具的 OpenClaw AI 代理，无需 CLI 设置或手动安装插件。

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

本指南介绍如何使用一键模板在 Railway 上部署带有官方 Bright Data 插件的 [OpenClaw](https://openclaw.ai/) AI 代理，让您的代理无需 CLI 设置、无需手动安装插件即可获得 66 个 Bright Data 网络工具。

[![在 Railway 上部署](https://railway.com/button.svg)](https://railway.com/deploy/openclaw-bright-data)

该 Railway 模板预装并预配置了 **Bright Data 的 OpenClaw 插件**。首次启动时，容器会安装插件、注册所有工具并生成持久网关令牌，让您的代理获得实时网络搜索、机器人绕过抓取、浏览器自动化，以及覆盖 Amazon、LinkedIn 和 Instagram 等平台的 50+ 结构化数据工具。

<Note>
  该插件注册了 **66 个工具**，分为五个类别：搜索、抓取、批量操作、浏览器自动化和结构化网络数据。
</Note>

<Tip>
  想在现有的 OpenClaw 实例上自行安装插件？请参阅 [如何将 Bright Data 与 OpenClaw 集成](/cn/integrations/openclaw) 中的手动 CLI 安装方法。
</Tip>

## 前置条件

* 具有 API 密钥的 [Bright Data 账户](https://brightdata.com)
* 一个 [Railway 账户](https://railway.com)（提供免费试用）
* 一个 AI 提供商 API 密钥：[OpenRouter](https://openrouter.ai/keys)（免费）、OpenAI、Anthropic 或 Gemini

<Note>
  推荐使用 OpenRouter。其免费的 Nemotron 模型提供 262K 上下文窗口，这是处理 66 工具插件清单且不触发速率限制错误所必需的。
</Note>

## 如何在 Railway 上部署模板

<Steps>
  <Step title="获取您的 Bright Data API 密钥">
    * 登录您的 [Bright Data 仪表板](https://www.bright.cn/cp)。
    * 转到 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请[生成 API 密钥](/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)。
  </Step>

  <Step title="在 Railway 上部署">
    点击 **Deploy on Railway**。Railway 会根据该模板创建一个新项目。

    <Warning>
      在部署之前或部署后立即在服务设置中添加一个**挂载到 `/data` 的持久卷**。否则，网关将无法存储其配置。
    </Warning>
  </Step>

  <Step title="设置环境变量">
    在 Railway 的 **Variables** 选项卡中设置以下变量：

    | 变量                                                        | 说明                    | 是否必填   |
    | --------------------------------------------------------- | --------------------- | ------ |
    | `BRIGHTDATA_API_TOKEN`                                    | 您的 Bright Data API 密钥 | **必填** |
    | `SETUP_PASSWORD`                                          | `/setup` 状态页面的密码      | **必填** |
    | `OPENROUTER_API_KEY`                                      | 推荐的 AI 提供商            | 推荐     |
    | `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `GEMINI_API_KEY` | 备选 AI 提供商             | 可选     |
  </Step>

  <Step title="等待初始化">
    首次启动需要 3 到 5 分钟。容器会安装插件、注册全部 66 个工具并生成持久网关令牌。
  </Step>

  <Step title="打开设置页面并复制网关令牌">
    打开 `https://your-app.up.railway.app/setup`，输入您的 `SETUP_PASSWORD` 并等待状态变为 **DONE**。复制**网关令牌**。
  </Step>

  <Step title="连接 OpenClaw UI">
    从设置页面打开 OpenClaw UI 并粘贴网关令牌。全部 66 个 Bright Data 工具会立即可用。
  </Step>
</Steps>

## 包含哪些 Bright Data 工具？

该插件注册了 66 个工具，分为五个类别：搜索、抓取、批量操作、浏览器自动化和结构化网络数据（Amazon、LinkedIn、Instagram、TikTok、YouTube、Reddit、Zillow 等）。

如需完整的工具列表、参数和示例提示，请参阅 [OpenClaw 集成页面上的工具参考](/cn/integrations/openclaw#可用工具)。

## 故障排除

**我需要添加卷吗？**

需要。在部署之前或部署后立即添加一个挂载到 `/data` 的持久卷。否则，OpenClaw 网关无法存储其配置，并且不会在重启后保留网关令牌。

**为什么推荐使用 OpenRouter 而非其他提供商？**

OpenRouter 上的免费 Nemotron 模型提供 262K 上下文窗口，这是处理 66 工具插件清单且不触发速率限制错误所必需的。如果改为设置其 API 密钥，OpenAI、Anthropic 和 Gemini 也同样适用。

**设置页面尚未显示我的工具**

在打开 OpenClaw UI 之前，请等待 `/setup` 页面报告状态 **DONE**。首次启动需要 3 到 5 分钟，期间容器会安装插件、注册全部 66 个工具并生成网关令牌。

## 其他资源

* [如何将 Bright Data 与 OpenClaw 集成](/cn/integrations/openclaw)：用于现有 OpenClaw 实例的手动 CLI 安装
* [AI 集成概述](/cn/integrations/ai-integrations)
* [OpenClaw 文档](https://docs.openclaw.ai)
* [GitHub 上的模板源代码](https://github.com/ReallyGreatTech/brightdata-railway)
