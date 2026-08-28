> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VS Code MCP 服务器集成

> 如何将 VS Code 与 Bright Data 的 MCP 服务器集成，以增强 AI 功能。

## 快速安装

点击下面的按钮，可在 VS Code 中自动安装并配置 Bright Data MCP 服务器：

## 自托管 MCP

<Steps>
  <Step title="前提条件">
    开始之前，请确保您拥有以下内容：

    * [Node.js](https://nodejs.org/en/download) 已安装并为最新版本
    * [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)（新用户可获得测试用免费额度，然后按使用付费）
    * **API 密钥**，可在 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取（新用户将在欢迎邮件中收到 **API 密钥**）

    <Tip>
      如果您希望使用不同的区域名称，可以在配置中通过 `WEB_UNLOCKER_ZONE` 环境变量指定
    </Tip>
  </Step>

  <Step title="基础配置">
    点击 VS Code 图标以自动安装 Bright Data MCP：

    <a href="vscode:mcp/install?%7B%22name%22%3A%22the-web-mcp%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22%40brightdata%2Fmcp%22%5D%2C%22env%22%3A%7B%22API_TOKEN%22%3A%22%24input%3Aapi-token%22%7D%7D" target="_blank">
      <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/visual-studio-code-svgrepo-com.svg?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=cccfaa4a4f07cdb90715cc438d6987a5" alt="在 VS Code 中安装" noZoom={true} height="0" className="mr-auto" title="" style={{ width: "5%", margin: "0", padding: "0" }} data-path="visual-studio-code-svgrepo-com.svg" />
    </a>
  </Step>
</Steps>
