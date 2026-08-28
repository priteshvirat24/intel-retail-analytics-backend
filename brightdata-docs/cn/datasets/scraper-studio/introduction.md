> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 了解 Scraper Studio

> Bright Data Scraper Studio 是构建自定义网页爬虫的云端 IDE，包含 AI Agent 和运行在 Bright Data 代理与解封基础设施上的 JavaScript IDE。

Bright Data Scraper Studio 是用于构建、运行和管理自定义网页爬虫的云端环境。Scraper Studio 完全运行在 Bright Data 的代理与解封基础设施之上，因此无需自行搭建服务器、管理代理轮换或编写重试逻辑。

阅读完本页后，您将了解哪种 Bright Data Scraper Studio 模式适合您的使用场景，以及如何从控制面板打开它。

## 工作原理

Bright Data Scraper Studio 中的每个爬虫都执行两项核心操作：

* **Interaction（交互）**：导航到目标 URL，处理分页、点击元素或发送 HTTP 请求
* **Parsing（解析）**：读取页面内容（HTML），并按已定义的输出 schema（JSON / CSV / NDJSON / JSONL）提取结构化字段

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/YJFytWtplv0" title="Scrape ANY website - Scraper Studio by Bright Data" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## 开发模式

Bright Data Scraper Studio 提供两种构建爬虫的方式：

| 模式       | 工作方式                                             | 最适合        |
| -------- | ------------------------------------------------ | ---------- |
| AI Agent | 用自然语言描述您想要的数据。Bright Data AI 自动生成 schema 并编写爬虫代码 | 无代码用户、快速原型 |
| IDE      | 在基于浏览器的代码编辑器中直接编写并测试 JavaScript，配套调试工具           | 需要完全控制的开发者 |

两种模式生成的是同一类爬虫：您不会被某一种方式锁定。AI Agent 构建的爬虫可以随时在 IDE 中打开并编辑，任何爬虫也都可以通过[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)进行更新。

## 何时使用 Scraper Studio，何时使用其他 Bright Data 产品

当您需要的数据不在 [Datasets Marketplace](/cn/datasets/marketplace/overview) 中、希望掌握爬虫逻辑的所有权，并且不想自行管理代理或基础设施时，请使用 Scraper Studio。

| 场景                                    | 推荐产品                                                       |
| ------------------------------------- | ---------------------------------------------------------- |
| 需要从主流站点获取数据且零搭建                       | [Datasets Marketplace](/cn/datasets/marketplace/overview)  |
| 需要由 Bright Data 构建并维护爬虫               | [Managed Services](/cn/datasets/scrapers/managed-services) |
| 需要在 Bright Data 基础设施上使用 AI 或代码构建自定义爬虫 | Scraper Studio                                             |

## AI Agent 与 IDE 的核心权衡

|       | AI Agent     | IDE             |
| ----- | ------------ | --------------- |
| 搭建时间  | 几分钟，描述即可运行   | 较长，需要编写、测试和调试   |
| 代码控制  | 由 AI 生成代码    | 您拥有每一行代码        |
| 自定义方式 | 通过自我修复工具的提示词 | 直接编辑 JavaScript |
| 最适合   | 快速创建爬虫、非技术用户 | 复杂逻辑、多阶段爬虫      |

## 如何访问 Scraper Studio

**前提条件：** 已激活的 Bright Data 账户

1. 前往 [www.bright.cn/cp](https://www.bright.cn/cp) 并登录
2. 在左侧菜单中，点击 **Scrapers**
3. 点击 **Scraper Studio**

**预期结果：** Scraper Studio 会打开并显示您的爬虫列表，新用户则会看到空白工作区。

<Note>
  菜单中看不到 Scraper Studio？您的账户可能没有访问权限。请联系 [Bright Data 支持](https://help.brightdata.com/hc/en-us/requests/new)。
</Note>

## 常见问题

<AccordionGroup>
  <Accordion title="我应该使用 AI Agent 还是 IDE 模式？">
    如果您想快速上手，或者不是开发者，请使用 AI Agent。如果您需要完全控制爬虫逻辑，或正在构建复杂的多阶段爬虫，请使用 Bright Data IDE 模式。
  </Accordion>

  <Accordion title="可以在 AI Agent 与 IDE 之间切换吗？">
    可以。任何以 AI Agent 模式创建的爬虫都可以在 IDE 中打开并编辑。您也可以使用[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)通过自然语言提示词更新爬虫。
  </Accordion>

  <Accordion title="Scraper Studio 与 Scrapers Library 有什么区别？">
    [Scrapers Library](https://www.bright.cn/products/web-scraper) 提供面向主流站点的预构建爬虫。Bright Data Scraper Studio 用于在目标站点不在库内时从零构建自定义爬虫。
  </Accordion>

  <Accordion title="我需要自行管理代理或服务器吗？">
    不需要。Bright Data Scraper Studio 会自动处理所有代理管理与基础设施。
  </Accordion>
</AccordionGroup>

## 下一步

<CardGroup cols={2}>
  <Card title="使用 AI Agent 构建" icon="robot" href="/cn/datasets/scraper-studio/ai-agent">
    使用自然语言提示词构建您的第一个爬虫
  </Card>

  <Card title="探索 IDE" icon="code" href="/cn/datasets/scraper-studio/scraper-studio-ide-interface">
    了解基于浏览器的代码编辑器
  </Card>

  <Card title="Worker 类型" icon="server" href="/cn/datasets/scraper-studio/worker-types">
    了解 Scraper Studio 如何运行您的任务
  </Card>
</CardGroup>

## 了解更多

<CardGroup cols={1}>
  <Card title="Scraper Studio 规格说明" icon="file-lines" href="/cn/datasets/scraper-studio/specifications">
    查看基础设施限制、计费模式和数据保留规则
  </Card>
</CardGroup>
