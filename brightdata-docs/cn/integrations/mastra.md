> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Mastra 集成

Bright Data SDK 集成现已在 Mastra 中提供，为 AI agent 带来强大的网页抓取与数据提取能力。该集成支持从 40+ 平台中提取结构化数据，包括 Amazon、LinkedIn 以及 Google、Bing、Yandex 等主流搜索引擎。

Mastra agents 可以执行网页抓取（带防封机制）、搜索查询、Amazon 产品数据提取、LinkedIn 数据收集等任务——几乎无需配置即可运行。这让你能够轻松构建具备推理、执行和实时数据抓取能力的智能代理，用于研究、自动化和竞品分析。

## 如何将 Bright Data 与 Mastra 集成

<Steps>
  <Step title="前置条件">
    * Node.js
    * 最新版本的 npm
    * Bright Data API 密钥
    * OpenAI API 密钥（用于 GPT-4o-mini）
    * Bright Data 区域会在需要时自动创建
  </Step>

  <Step title="获取 Bright Data API 密钥">
    * 登录你的 [Bright Data 控制台](https://www.bright.cn/cp)
    * 前往 [账户设置](https://www.bright.cn/cp/setting/users)
    * 如果你还没有 API 密钥，请[生成一个](/cn/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)
    * 为你的 API 密钥启用 SDK 访问权限
  </Step>

  <Step title="获取 OpenAI API 密钥">
    * 访问 [OpenAI 平台](https://platform.openai.com)
    * 前往 API Keys 页面
    * 创建新的 API 密钥
    * 确保你拥有 GPT-4o-mini 的访问权限
  </Step>

  <Step title="使用模板创建 Mastra 项目">
    使用 Bright Data Mastra 模板创建新项目：

    ```bash theme={null}
    npx create-mastra@latest --template brightdata-mastra-tools
    cd brightdata-mastra-tools
    npm install
    ```

    <Note>
      或者，你也可以直接克隆仓库：

      ```bash theme={null}
      git clone https://github.com/brightdata/brightdata-mastra-tools
      cd brightdata-mastra-tools
      npm install
      ```
    </Note>
  </Step>

  <Step title="配置环境变量">
    编辑 `.env` 文件，填入你的 API 密钥：

    ```env theme={null}
    OPENAI_API_KEY=your_openai_api_key_here
    BRIGHTDATA_API_KEY=your_brightdata_api_key_here
    ```
  </Step>

  <Step title="启动开发服务器">
    运行带热重载的 Mastra 开发服务器：

    ```bash theme={null}
    npm run dev
    ```

    你的 Bright Data 加持的 Web Agent 已准备就绪！
  </Step>

  <Step title="示例用法">
    该 Web Agent 自带四个强大的工具。下面是 Agent 的工作方式：

    ```typescript theme={null}
    import { Agent } from '@mastra/core/agent';
    import { Memory } from '@mastra/memory';
    import { LibSQLStore } from '@mastra/libsql';
    import { brightDataTools } from './tools/web-tools';

    const apiKey = process.env.BRIGHTDATA_API_KEY ?? '';
    const brightTools = brightDataTools({ apiKey });

    export const webAgent = new Agent({
      name: 'Web Agent',
      instructions: `
        你是一个具备 Bright Data 能力的通用网页研究助手。
        
        工具使用指南：
        - 使用搜索工具构建上下文或查找可信来源。
        - 使用抓取工具从具体页面提取详细内容。
        - 当需要价格、库存或评论总结时，调用 Amazon 产品工具。
        - 当用户需要职业背景信息时，调用 LinkedIn Profiles 工具。
      `,
      model: 'openai/gpt-4o-mini',
      tools: {
        searchTool: brightTools.search!,
        scrapeTool: brightTools.scrape!,
        amazonProductTool: brightTools.amazonProduct!,
        linkedinCollectProfilesTool: brightTools.linkedinCollectProfiles!,
      },
      memory: new Memory({
        storage: new LibSQLStore({
          url: 'file:../mastra.db',
        }),
      }),
    });
    ```

    **示例查询：**

    * “搜索量子计算的最新进展”
    * “抓取 example.com 的价格信息”
    * “获取此 Amazon 产品的详情和评论：\[URL]”
    * “收集某公司高管的 LinkedIn 资料”
  </Step>

  <Step title="可用工具">
    集成提供以下四类强大工具：

    **1. 搜索工具**

    * 支持 Google、Bing、Yandex
    * 返回 Markdown 或 HTML
    * 自动防封与反机器人
    * 支持国家代码以获取本地化结果

    **2. 抓取工具**

    * 获取网页内容并转换成干净的 Markdown
    * 自动绕过 CAPTCHA 和机器人检测
    * 支持国家级代理

    **3. Amazon 产品工具**

    * 价格、评分、评论、规格
    * 支持 ZIP 码本地化
    * 全量产品信息

    **4. LinkedIn Profiles 工具**

    * 获取职业背景、经验、教育
    * 支持批量
    * 详细技能与工作记录
  </Step>

  <Step title="自定义工具">
    你可以选择性地启用或禁用工具：

    ```typescript theme={null}
    const brightTools = brightDataTools({
      apiKey: process.env.BRIGHTDATA_API_KEY!,
      excludeTools: ['linkedinCollectProfiles'] // 禁用某些工具
    });
    ```
  </Step>
</Steps>

## 项目结构

```

your-project/
├── src/
│   └── mastra/
│       ├── agents/
│       │   └── web-agent.ts           # 主 AI Agent
│       ├── tools/
│       │   └── web-tools.ts           # Bright Data SDK 工具
│       └── index.ts                   # Mastra 配置
├── .env                               # API 密钥（勿提交）
├── .env.example                       # 环境变量模板
├── package.json                       # 依赖
└── tsconfig.json                      # TypeScript 配置

```

## 关键特性

* **AI 智能推理**：使用 OpenAI GPT-4o-mini
* **Bright Data SDK 深度集成**
* **多数据源支持**：搜索引擎、网页抓取、Amazon、LinkedIn
* **自动防封机制**
* **持久化记忆**（LibSQL）
* **TypeScript 强类型支持**

## 生产部署

```bash theme={null}
npm run build
npm run start
```

## 故障排查

**“初始化工具需要 Bright Data API 密钥”**

* 检查 `.env` 中的 `BRIGHTDATA_API_KEY`
* 确认 API 密钥具有 SDK 权限
* 检查密钥是否已过期

**“OpenAI API key not found”**

* 检查 `.env` 中的 `OPENAI_API_KEY`
* 确保你有 GPT-4o-mini 的权限
* 检查账户是否有余量

**工具初始化失败**

* 集成默认启用 `autoCreateZones: true`
* 检查 Bright Data 控制台中的区域是否已创建

## 更多资源

* [Mastra 文档](https://mastra.ai/en/docs)
* [Bright Data SDK 文档](/cn/api-reference/SDK-JS)
* [GitHub 仓库](https://github.com/brightdata/brightdata-mastra-tools)
