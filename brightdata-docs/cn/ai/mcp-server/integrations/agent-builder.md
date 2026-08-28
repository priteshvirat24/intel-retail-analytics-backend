> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Agent Builder MCP 服务器集成

> 如何将 Agent Builder 与 Bright Data MCP 服务器集成，以创建 AI 代理。

**要求：**

* [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)
* 拥有 [已验证组织](https://help.openai.com/en/articles/10910291-api-organization-verification) 的 OpenAI 账户

<Steps>
  <Step title="创建新流程">
    前往 [Agent Builder](https://platform.openai.com/agent-builder) 并创建一个新流程

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.27.55.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=d2a01b3168c6893dfa7f1ce7aa628e27" alt="Screenshot 2025-10-10 at 10.27.55.png" width="1431" height="510" data-path="images/Screenshot2025-10-10at10.27.55.png" />
  </Step>

  <Step title="点击代理节点">
    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.30.51.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=d5976fe7f250e820a05f9ffe1f10a8dc" alt="Screenshot 2025-10-10 at 10.30.51.png" width="1339" height="618" data-path="images/Screenshot2025-10-10at10.30.51.png" />

    点击代理节点后，代理配置面板将显示在屏幕左侧。
  </Step>

  <Step title="点击工具以添加 MCP">
    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.32.45.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=6a2d661ee2579fdb4759d4ce65d2c42b" alt="Screenshot 2025-10-10 at 10.32.45.png" width="375" height="529" data-path="images/Screenshot2025-10-10at10.32.45.png" />
  </Step>

  <Step title="选择 MCP 并添加 Bright Data MCP 服务器">
    将以下 URL 复制并粘贴到 URL 栏中：

    ```
    https://mcp.brightdata.com/mcp?token=YOUR_API_KEY
    ```

    将 `YOUR_API_KEY` 替换为您的 Bright Data API 密钥。

    <Note>
      您也可以从 [控制面板](https://www.bright.cn/cp/mcp) 获取预填充 API 密钥的 URL
    </Note>

    然后点击 Connect 按钮。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.40.55.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=9ea53ee4e9d2af8a4966ecd3586cfdb0" alt="Screenshot 2025-10-10 at 10.40.55.png" width="524" height="668" data-path="images/Screenshot2025-10-10at10.40.55.png" />
  </Step>

  <Step title="选择所需工具并添加">
    在此处，您可以选择要向代理公开的相关工具，或者通过点击 Add 按钮添加所有工具。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.44.46.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=8097c3fc0506a306bb67ec580b16025d" alt="Screenshot 2025-10-10 at 10.44.46.png" width="522" height="566" data-path="images/Screenshot2025-10-10at10.44.46.png" />
  </Step>

  <Step title="为代理配置名称和说明">
    为您的代理命名，提供指令集，选择推理努力等级，然后点击 Preview 按钮进行测试。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.48.31.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=9a88d7f85801d5287b52e44bd76bc09a" alt="Screenshot 2025-10-10 at 10.48.31.png" width="356" height="556" data-path="images/Screenshot2025-10-10at10.48.31.png" />
  </Step>

  <Step title="测试您的代理">
    向您的代理提出任何需要实时网页数据的问题，并立即获取答案。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.52.31.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=539f67c417dc1812e378d976683f1086" alt="Screenshot 2025-10-10 at 10.52.31.png" width="1672" height="746" data-path="images/Screenshot2025-10-10at10.52.31.png" />
  </Step>
</Steps>
