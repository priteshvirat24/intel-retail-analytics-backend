> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

使用 Crawl API 有两种方式：

1. 基于 API 的数据采集
2. 无代码采集（通过控制面板）

## 基于 API 的数据采集

1. 通过简单的 HTTP POST [触发一次数据采集](/cn/api-reference/rest-api/scraper/asynchronous-requests) 任务
2. 指定 URL 和输出格式
3. 接收一个 `snapshot_id`，用于稍后获取结果

```sh Code Example theme={null}
curl -H "Authorization: Bearer API_KEY" -H "Content-Type: application/json" -d '[{"url":"https://example.com"},{"url":"https://example.com/1"}]' "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset_id>&include_errors=<true/false>&custom_output_fields=<custom_output_fields>"
```

### 查询参数：

<ParamField path="dataset_id" type="query" required>
  您的数据集 ID（例如：`gd_m6gjtfmeh43we6cqc`）
</ParamField>

<ParamField path="include_errors" type="query" default="true">
  在结果中包含错误日志
</ParamField>

<ParamField path="custom_output_fields" type="query">
  `markdown`, `html`, `ld_json` 等。 \\

  选择适合您工作流的格式：

  <CodeGroup>
    ```md markdown theme={null}
    # Main Article Title

    This is the introduction paragraph with **bold text** and *italics*.

    ## Subheading

    * List item one
    * List item two

    > This is a blockquote from the articlesh Code Example

    [Link text](https://example.com/more-info)
    ![Image description](https://example.com/image.jpg)

    ```

    ```html html2text theme={null}

    Main Article Title

    This is the introduction paragraph with bold text and italics.

    Subheading

    * List item one
    * List item two

    This is a blockquote from the articlesh Code Example


    Link text [https://example.com/more-info]
    [Image: Image description]
    ```

    ```html page_html theme={null}
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Example Article</title>
      <link rel="stylesheet" href="/styles.css">
      <script src="/analytics.js"></script>
    </head>
    <body>
      <header>
        <nav><!-- Navigation HTML --></nav>
      </header>
      <main>
        <h1>Main Article Title</h1>
        <p>This is the introduction paragraph with <strong>bold text</strong> and <em>italics</em>.</p>
        <h2>Subheading</h2>
        <ul>
          <li>List item one</li>
          <li>List item two</li>
        </ul>
        <blockquote>This is a blockquote from the article</blockquote>
        <a href="https://example.com/more-info">Link text</a>
        <img src="https://example.com/image.jpg" alt="Image description">sh Code Example
      </main>
    </body>
      <footer><!-- Footer HTML --></footer>
    </html>
    ```

    ```json ld_json theme={null}
    {
      "@context":"https://schema.org",
      "@type":"Article",
      "headline":"Main Article Title",
      "author":{
        "@type":"Person",
        "name":"Jane Smith"
      },
      "datePublished":"2023-08-15T12:00:00Z",
      "dateModified":"2023-08-15T14:22:31Z",
      "publisher":{
        "@type":"Organization",
        "name":"Example Publication",
        "logo":{
          "@type":"ImageObject",
          "url":"https://example.com/logo.png"
        }
      },
      "image":"https://example.com/image.jpg",
      "description":"This is the introduction paragraph with bold text and italics.",
      "mainEntityOfPage":"https://example.com/article"
    }
    ```
  </CodeGroup>
</ParamField>

## 数据投递

可将结果投递至：

* Webhooks
* 外部存储（S3、GCS 等）
* 通过 API 或控制面板直接下载

## 无代码爬虫（控制面板）

使用控制面板即可启动爬取任务，无需编写任何代码。
步骤：

1. 打开 Crawl API 控制面板
2. 输入目标域名或 URL
3. 选择输出格式
4. 启动爬取
5. 从仪表盘直接下载结果
