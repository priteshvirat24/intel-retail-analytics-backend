> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 编码助手提示词

> 可直接复制的 Claude Code、Cursor 和 Codex 提示词，用于构建 Bright Data Scraper Studio 爬虫：一个简单的构建并运行提示词，以及完整的自我修复流程。

使用这些可直接复制的提示词，通过 Claude Code、Cursor 或 Codex 构建 Bright Data Scraper Studio 爬虫。如果您只想快速得到一个爬虫，请从一个提示词的构建并运行开始：换上您的 URL 和想要的字段，粘贴，完成。下面更长的流程则增加了完整的构建、运行、修复、批准、再运行循环，用于需要原地扩展爬虫数据结构的场景。

## 前提条件

* 一个 Bright Data 账户（[免费注册](https://www.bright.cn/?hs_signup=1\&utm_source=docs)，无需信用卡）。
* Node.js 20 或更高版本，这是通过 `npx` 运行 Bright Data CLI 所需的全部条件。
* 一个具备终端访问能力的编码助手：Claude Code、Cursor 或 Codex。

您无需提前安装 Bright Data CLI。下面的提示词通过 `npx` 运行它，按需获取最新版本，因此没有任何需要维护的全局依赖。

## 用一个提示词构建爬虫

如果您只想快速得到一个爬虫，粘贴下面这个提示词，并替换尖括号中的两个值：目标 URL 和您想要的字段。编码助手通过 `npx` 运行 Bright Data CLI，然后构建爬虫并运行一次。不含自我修复。

```text Prompt theme={null}
构建并运行一个 Bright Data 爬虫。所有 Bright Data CLI 命令都通过 `npx -p @brightdata/cli` 运行，因此无需任何全局安装。替换 <TARGET_URL> 和 <FIELDS TO EXTRACT>，然后按顺序执行每个步骤，如果某个步骤失败则停止：

1. 运行 `npx -p @brightdata/cli bdata login` 进行身份验证。npx 会按需获取 CLI，因此无需安装任何东西。
2. 为 <TARGET_URL> 创建一个 Bright Data 爬虫，提取：<FIELDS TO EXTRACT>。返回 Collector ID。
3. 在同一个 URL 上运行该爬虫并美化输出结果。
```

例如，要抓取一个商品页面，填好后的第 2 步如下：

```text Prompt theme={null}
2. 为 https://shopalto.xyz/product/aurora-wireless-headphones 创建一个 Bright Data 爬虫，提取：产品名称、价格、描述和评分。返回 Collector ID。
```

> **预期结果：** 编码助手返回一个类似 `c_mpohus372o5tmid1jk` 的 Collector ID，然后打印一个 JSON 数组，其中一行包含您所要求的字段。

<Tip>
  保存 Collector ID。复用它即可在新的 URL 上运行该爬虫，或在之后用下面的自我修复流程扩展其数据结构。
</Tip>

## 用一个提示词构建、运行并自我修复

如需查看完整的构建、运行、修复、批准、再运行循环的实际效果，粘贴下面这一个提示词，让编码助手逐步完成每个步骤。这种模式是有意为之：先构建一个最小爬虫，再通过修复扩展数据结构，这样修复信封中的 `preview_result` 就更容易对照一个已知良好的基线进行验证。编码助手通过 `npx` 运行所有 Bright Data CLI 命令，因此无需任何全局安装。

```text Prompt theme={null}
端到端地构建、运行、修复并验证一个 Bright Data 爬虫。所有 Bright Data CLI 命令都通过 `npx -p @brightdata/cli` 运行，因此无需任何全局安装。请按顺序执行每个步骤，如果某个步骤失败则停止：

1. 运行 `npx -p @brightdata/cli bdata login` 进行身份验证。npx 会按需获取 CLI，因此无需安装任何东西。
2. 为 https://shopalto.xyz/product/aurora-wireless-headphones 创建一个 Bright Data 爬虫，仅提取两个字段：产品名称和价格。返回 Collector ID。
3. 在同一个 URL 上运行该爬虫并美化输出结果。预期返回一行包含 name 和 price 的数据。
4. 原地修复该爬虫，在现有的 name 和 price 之外，再捕获 description、image url 和 rating。保持相同的 Collector ID，将修复锚定在同一个 URL 上，并显示批准信封。
5. 当预览显示全部五个字段时，在同一个 URL 上批准该修复。
6. 再次在同一个 URL 上运行该爬虫，确认全部五个字段都已返回：name、price、description、image_url 和 rating。
```

> **预期结果：** 编码助手最终返回一行 JSON，包含 `name`、`price`、`description`、`image_url` 和 `rating`，且 Collector ID 与第 2 步相同。

## 逐步运行流程

当您希望在继续之前检查每个 Collector ID、运行结果和修复信封时，请逐条执行下面的提示词。

<Steps>
  <Step title="提示编码助手对 CLI 进行身份验证">
    ```text Prompt theme={null}
    所有 Bright Data CLI 命令都通过 `npx -p @brightdata/cli` 运行，因此无需任何全局安装。运行 `npx -p @brightdata/cli bdata login` 进行身份验证，然后在继续之前用 `npx -p @brightdata/cli bdata --version` 确认版本号。
    ```

    > **预期结果：** 编码助手打印出 `bdata` 的版本号并确认已完成身份验证。npx 会按需获取 CLI，因此无需任何全局安装。
  </Step>

  <Step title="提示编码助手构建一个最小爬虫">
    ```text Prompt theme={null}
    为 https://shopalto.xyz/product/aurora-wireless-headphones 创建一个 Bright Data 爬虫，仅提取两个字段：产品名称和价格。完成后向我显示 Collector ID。
    ```

    > **预期结果：** 编码助手返回一个类似 `c_mpohus372o5tmid1jk` 的 Collector ID。请保存它；后续提示词都会复用同一个 ID。
  </Step>

  <Step title="提示编码助手运行爬虫">
    ```text Prompt theme={null}
    在 https://shopalto.xyz/product/aurora-wireless-headphones 上运行该爬虫并美化输出结果。
    ```

    > **预期结果：** 一个 JSON 数组，包含一行数据，仅填充 `name` 和 `price`。
  </Step>

  <Step title="提示编码助手修复并添加更多字段">
    ```text Prompt theme={null}
    原地扩展该爬虫。修复它，在现有的 name 和 price 之外，再捕获 description、image url 和 rating。保持相同的 Collector ID。将修复锚定在 https://shopalto.xyz/product/aurora-wireless-headphones 上，并在准备就绪时向我显示批准信封。
    ```

    > **预期结果：** 编码助手返回 `status: "awaiting_approval"`，其 `preview_result` 行现在显示五个字段。
  </Step>

  <Step title="提示编码助手批准修复">
    ```text Prompt theme={null}
    预览看起来没问题。批准该修复，锚定在 https://shopalto.xyz/product/aurora-wireless-headphones 上。
    ```

    > **预期结果：** `status` 推进到 `done`。Collector ID 保持不变。
  </Step>

  <Step title="提示编码助手验证扩展后的数据结构">
    ```text Prompt theme={null}
    再次在 https://shopalto.xyz/product/aurora-wireless-headphones 上运行该爬虫，确认全部五个字段现在都已返回：name、price、description、image_url 和 rating。
    ```

    > **预期结果：** 与之前运行相同的 JSON 结构，每行现在多出三个字段。
  </Step>
</Steps>

<Tip>
  如需无人值守的变体，让编码助手在修复调用中添加 `--auto-approve`。编码助手会跳过批准环节，一步轮询直至 `done`。仅在您信任无需人工审核的修复时使用它。
</Tip>

## 相关内容

<CardGroup cols={2}>
  <Card title="使用 Bright Data CLI 构建爬虫" icon="terminal" href="/cn/datasets/scraper-studio/build-with-the-cli">
    权威的 CLI 教程：安装、登录、创建、运行、修复
  </Card>

  <Card title="自我修复工具" icon="screwdriver-wrench" href="/cn/datasets/scraper-studio/self-healing-tool">
    从 Bright Data 控制面板修复爬虫
  </Card>

  <Card title="Scraper Studio API 快速开始" icon="code" href="/cn/datasets/scraper-studio/quickstart">
    通过 cURL、Python 或 Node.js 触发现有爬虫
  </Card>

  <Card title="Bright Data CLI 命令" icon="book" href="/cn/cli/commands">
    scraper create、heal 和 approve 的参数参考
  </Card>
</CardGroup>
