> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API 常见问题

> 通过详细的常见问题解答，了解如何高效使用 Bright Data 的 SERP API，包括设置、故障排查及高级搜索技巧，如 Google 图片和酒店数据抓取。

<AccordionGroup>
  <Accordion title="为什么要使用 Bright Data 的 SERP API？">
    Bright Data SERP API 解决方案让你专注于最重要的事情——数据。它提供了一个三合一代理解锁方案，自动处理 **代理管理**（选择何时使用哪个代理）、**解锁逻辑**（验证码破解、指纹识别、重试、最佳请求头等）以及 **抓取** 功能。

    <Tab title="易于集成">
      在代码中，只需将常规代理请求的一行替换为 SERP API 请求即可。
    </Tab>

    <Tab title="只为成功请求付费">
      仅为成功请求付费。
    </Tab>

    <Tab title="稳定且可预测的计费">
      因为按页面数计费（每千次请求价格），请求的带宽无影响。
    </Tab>

    <Tab title="高精度">
      使用真实用户设备，进行精确的地理定位（包括城市级）采集主要搜索引擎的搜索结果页 (SERPs)。
    </Tab>

    <Tab title="支持高流量和扩展">
      Bright Data 能支持增长中的流量需求和高峰期请求，成功率高，响应时间优异（低于 5 秒）。
    </Tab>

    <Tab title="降低成本">
      节省数据抓取工程师和 IT 人员成本，无需担心服务器维护。
    </Tab>

    <Tab title="避免运营问题">
      每个请求使用不同 IP，确保不被封禁。
    </Tab>

    <Tab title="结构化数据响应">
      获取解析或未解析的 JSON 或 HTML 响应，方便集成到任何系统。
    </Tab>

    <Tab title="高度自定义">
      支持多种参数以满足搜索需求，包括不同搜索类型、设备、每页结果数等。
    </Tab>

    <Tab title="真实住宅 IP">
      可访问每月 4 亿+ 住宅 IP，覆盖所有地理位置。
    </Tab>
  </Accordion>

  <Accordion title="如何使用 SERP API 进行 &#x22;Google 图片搜索&#x22;？">
    使用 Bright Data SERP API 可以轻松收集 Google 图片搜索数据。

    Google 反向图片搜索（官方称为 "Google Search by Image"）允许用户 **以图片作为起点** 进行搜索，而非文字或语音查询。

    <Note>
      JSON 响应包含以 base64 编码的图片。
    </Note>

    <CodeGroup>
      ```sh 使用图片 URL 搜索 theme={null}
      curl -v --compressed --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> "https://www.google.com/searchbyimage?image_url={TARGET_IMAGE_URL}"
      ```

      ```sh 使用本地图片搜索 theme={null}
      curl -v --compressed --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> 'http://www.google.com/searchbyimage/upload' -o results_page.html -F 'encoded_image=@{FULL_IMAGE_FILE_PATH}'
      ```

      ```sh 为图片添加查询 theme={null}
      <insert-code-here>
      ```
    </CodeGroup>

    查看更多 [Google 图片 SERP 功能](/cn/scraping-automation/serp-api/query-parameters/google#lens)。
  </Accordion>

  <Accordion title="如何使用 SERP API 抓取酒店数据？">
    Bright Data SERP API 可轻松收集酒店数据，如价格、可用性、评价等。

    **抓取酒店数据有两种方式：**

    <Tabs>
      <Tab title="Google 搜索酒店知识图谱">
        **提供每家酒店的有限价格和日期信息**

        当你在 Google 搜索特定酒店时，酒店详情和评价会显示在右侧知识图谱/小部件中：

        <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/parsing-search-results/hotels-html.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=6a834af11c875e8f6c1f574001d92ab8" alt="hotels-html.png" width="1485" height="825" data-path="images/scraping-automation/serp-api/parsing-search-results/hotels-html.png" />

        可设置入住/退房日期、入住人数及比较价格。

        使用 SERP API，可通过专用参数设置这些字段以收集不同价格组合。完整酒店参数和功能见 [API 文档](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results#hotels)。

        <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/parsing-search-results/hotels-availability.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=af4125e17dcdd6e64e0093a9fb33eb88" alt="hotels-availability.png" width="548" height="666" data-path="images/scraping-automation/serp-api/parsing-search-results/hotels-availability.png" />
      </Tab>

      <Tab title="Google Travel 酒店页面">
        **提供酒店全量详情、价格及日期**

        SERP API 还可抓取 Google Travel 酒店页面（Google.\*/travel/hotels/…），可获取更多价格并按额外参数搜索（如入住/退房日期、成人和儿童人数、儿童年龄、是否可免费取消）。

        <Note>
          仅支持 //Google.\*/travel/hotels/… URL。
        </Note>

        在控制面板 [API 指南](https://www.bright.cn/cp/serp_api/api/google/hotels) 查看如何抓取该页面及可用参数，或查看 [API 文档](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results#hotels)。

        <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/faqs/hotel-info.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=6591b859a7defea8130d061cd40a445e" alt="hotel-info.png" width="1234" height="807" data-path="images/scraping-automation/serp-api/faqs/hotel-info.png" />
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="如何在不使用 SSL 证书的情况下发送 SERP API HTTPS 请求？">
    针对 HTTPS，URL 数据是加密的。因此，为了让 SERP API 解密数据并返回结果，你需要下载并安装 [Bright Data 证书]()。

    示例代码：

    <CodeGroup>
      ```sh Shell theme={null}
      curl "https://www.google.com/search?q=pizza&lum_json=1" -v --insecure --compressed --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
      ```

      ```js NodeJS theme={null}
      process.env.NODE_TLS_REJECT_UNAUTHORIZED = 0;
      ```

      ```java Java theme={null}
      -Dcom.sun.net.ssl.checkRevocation=false
      ```

      ```cs C# theme={null}
      ServicePointManager.ServerCertificateValidationCallback += (sender, cert, chain, sslPolicyErrors) => true;
      ```

      ```python Python theme={null}
      # 对原生 request 库:
      import ssl
      ssl._create_default_https_context = ssl._create_unverified_context

      # 对 requests 库，可在 .get() 方法中直接关闭 SSL 检查：
      # requests.get(url, proxies=proxies, verify=False)
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="如何发送带 SSL 验证的 HTTPS 请求？">
    <Tabs>
      <Tab title="Shell">
        使用 `--cacert` 标志加上证书路径：

        ```sh Shell theme={null}
        curl -v --compressed "https://www.google.com/search?q=pizza&lum_json=1" --cacert “{证书路径}“ --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
        ```
      </Tab>

      <Tab title="Java">
        将证书导入 Java Keystore，例如使用 keytool：

        <CodeGroup>
          ```java Java theme={null}
          %JAVA_HOME% Keystore（通常在 ..\lib\security\cacerts）
          ```

          ```sh Keytool 示例 theme={null}
          keytool -import -alias <cert alias> -file <cert name>.cer -keystore <keystore filename> -storepass <keystore password>
          # 执行后提示信任证书，输入 'y'
          ```
        </CodeGroup>
      </Tab>

      <Tab title="其他编程语言">
        按照文章 [下载并安装 Bright Data 证书](/cn/general/account/ssl-certificate) 指导，将证书添加到本地受信任根证书。

        ```sh Shell theme={null}
        T_ID&zone={ASYNC_ZONE}&output={output_fomat_html/json}&response_id={response_id} -H "Authorization: Bearer {API_KEY}" -o {Your_result_ouput_file}
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="如何解析 SERP API 返回的 JSON？">
    请参考文章：[解析搜索结果](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results)
  </Accordion>

  <Accordion title="如何在同一 API 请求中发送多查询？">
    SERP API 支持在单个 API 请求中使用 `multi` 参数发送 2 个并行查询。

    这些并行请求使用相同 IP 和会话，可用于收集额外数据、对比测试等。

    <Note>
      **条件：**

      * 仅支持启用 [异步请求](/cn/scraping-automation/serp-api/asynchronous-requests) 的 zone
      * 仅支持 Google 搜索
      * 限制为 2 个请求
      * 按 2 个请求计费
    </Note>

    <CodeGroup>
      ```json 不同 num 参数 theme={null}
      multi:[
        {"keyword":"pizza","num":20},
        {"keyword":"pizza","num":100}
      ]
      ```

      ```json 不同关键词 theme={null}
      multi:[
        {"keyword":"pizza"},
        {"keyword":"burger"}
      ]
      ```
    </CodeGroup>

    <CodeGroup>
      ```sh 发送请求 theme={null}
      curl -v --compressed "https://api.brightdata.com/serp/req" -H "Content-Type: application/json" -H "Authorization: Bearer $API_KEY" -d "{\"zone\":\"$ZONE\",\"country\":\"us\",\"multi\":[{\"keyword\":\"pizza\",\"num\":20},{\"keyword\":\"pizza\",\"num\":100}]}"
      ```

      ```sh 收集响应 theme={null}
      curl -k -v --compressed "https://api.brightdata.com/serp/get_result?customer={customer_id&zone={ASYNC_ZONE}&response_id={response_id}" -H "Authorization: Bearer $API_KEY" -o {Your_result_ouput_file}
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="Google 最近停止支持 `num` 参数，我该怎么办？">
    自 2025 年 9 月 10 日起，Google 已开始逐步弃用 `num` 参数。

    我们建议需要更多 Google SERP 页面（超过第一页）的客户使用 Bright Data 的 Scrapers（Google SERP – 100 Results）一次获取前 100 个结果，无需手动分页，可通过 start\_page/end\_page 控制深度（1..10 ≈ 前 100）。

    [了解如何一次获取前 100 条结果](/cn/scraping-automation/serp-api/get-top-100-google-results)
  </Accordion>

  <Accordion title="SERP API 的常见使用场景有哪些？">
    <Tab title="自然排名监测">
      监测公司在不同地区的关键词排名
    </Tab>

    <Tab title="品牌保护">
      追踪公司品牌及商标的搜索结果
    </Tab>

    <Tab title="价格比较">
      对在线购物网站商品进行搜索并比较不同供应商价格
    </Tab>

    <Tab title="市场调研">
      收集公司、联系人、地点等信息
    </Tab>

    <Tab title="版权侵权检测">
      搜索图片或其他受版权保护的内容
    </Tab>

    <Tab title="广告情报">
      查看不同国家关键词展示的广告，包括 DoubleClick 和 Google 广告服务
    </Tab>
  </Accordion>

  <Accordion title="如何对 Microsoft Bing 进行日期过滤查询？">
    以下内容分析 Bing 上不同日期搜索查询选项及使用方法。

    ## 日期过滤查询类型

    <Tabs>
      <Tab title="所有日期">
        不使用日期过滤

        * URL: [https://www.bing.com/search?q=YOUR\_QUERY](https://www.bing.com/search?q=YOUR_QUERY)
      </Tab>

      <Tab title="过去 24 小时">
        URL 加上 `filters=ex1%3a"ez1"`

        * URL: [https://www.bing.com/search?q=YOUR\_QUERY\&filters=ex1%3a"ez1](https://www.bing.com/search?q=YOUR_QUERY\&filters=ex1%3a"ez1)"
      </Tab>

      <Tab title="过去一周">
        URL 加上 `filters=ex1%3a"ez2"`

        * URL: [https://www.bing.com/search?q=YOUR\_QUERY\&filters=ex1%3a"ez2](https://www.bing.com/search?q=YOUR_QUERY\&filters=ex1%3a"ez2)"
      </Tab>

      <Tab title="过去一年">
        URL 加上 `filters=ex1%3a"ez3"`

        * URL: [https://www.bing.com/search?q=YOUR\_QUERY\&filters=ex1%3a"ez3](https://www.bing.com/search?q=YOUR_QUERY\&filters=ex1%3a"ez3)"
      </Tab>

      <Tab title="精确匹配">
        指定精确日期范围，URL 添加 `filters=ex1:"ez5_StartDateSequence_EndDateSequence"`

        * URL: [https://www.bing.com/search?q=YOUR\_QUERY\&filters=ex1:"ez5\_StartDateSequence\_EndDateSequence](https://www.bing.com/search?q=YOUR_QUERY\&filters=ex1:"ez5_StartDateSequence_EndDateSequence)"

        <Tip>
          `StartDateSequence` 和 `EndDateSequence` 可按以下逻辑计算。
        </Tip>
      </Tab>
    </Tabs>

    ## 精确匹配日期序列计算

    <Steps>
      <Step title="以已知序列为起点">
        使用 2024 年 1 月 1 日为起点，已知序列为 `19723`
      </Step>

      <Step title="计算 StartDateSequence">
        * 统计从 1 月 1 日到目标开始日期的天数
        * 将统计天数加到起点序列数，得到 `StartDateSequence`

        <Tip>
          计数从 0 开始，例如 0, 1, 2 ...
        </Tip>

        > #### 示例：
        >
        > 计算 2024 年 2 月 4 日序列：
        >
        > * 1 月 1 日到 2 月 4 日共 35 天
        > * 35 - 1 = 34
        > * 2 月 4 日序列: 19723 + 34 = 19757 (`StartDateSequence`)
      </Step>

      <Step title="计算 EndDateSequence">
        将日期范围天数加到 `StartDateSequence`，得到 `EndDateSequence`。

        > #### 示例：
        >
        > 2 月 4 日序列: 19757
        > 2 月 4 日到 2 月 20 日天数: 17
        > 17 - 1 = 16
        > 2 月 20 日序列: 19757 + 16 = 19773 (`EndDateSequence`)
      </Step>

      <Step title="构建序列字符串">
        * 格式：`ez5_StartDateSequence_EndDateSequence`
        * 替换起始序列和结束序列

        > #### 示例：
        >
        > * 起始序列: 19757
        > * 结束序列: 19773
        > * 序列字符串: `ez5_19757_19773`
        > * 查询 pizza 的 URL: \
        >   [https://www.bing.com/search?q=pizza\&filters=ex1:"ez5\_19757\_19773](https://www.bing.com/search?q=pizza\&filters=ex1:"ez5_19757_19773)"

        <Frame>
          <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/faqs/bing-exact-date-filter.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=909cf877fad46c2ae624f890de7cc538" alt="bing-exact-date-filter.png" width="1022" height="233" data-path="images/scraping-automation/serp-api/faqs/bing-exact-date-filter.png" />
        </Frame>
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="为什么会出现错误: &#x22;400 this endpoint is not supported&#x22;?" defaultOpen="false">
    SERP API 仅支持部分搜索引擎相关域名/端点，某些子域或端点可能不支持。例如：`https://trends.google.com/trends` 不支持，而 `https://trends.google.com/trends/explore` 支持。

    建议查看 [SERP Playground](https://www.bright.cn/cp/zones/serp_playground) 和 [SERP 文档](/cn/scraping-automation/serp-api/query-parameters) 了解支持的域名和路径示例。
  </Accordion>

  <Accordion title="如何在 Google 搜索结果中查看更多广告？" defaultOpen="false">
    如果你在监控 Google 搜索广告并希望最大化可见性，可在 Google.com SERP API 请求中使用 Enhanced Ads 功能。

    默认 SERP 行为：

    * 获取广域内的自然搜索结果和广告。
      启用 Enhanced Ads：
    * 扩展搜索结果和广告范围，模拟无 Cookie 的隐身浏览体验。

    在控制面板 [SERP API zone](https://www.bright.cn/cp/zones) 配置页启用该功能。

    [了解更多](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results#ads)
  </Accordion>

  <Accordion title="如何提高 SERP API 响应速度？">
    使用 `"data_format": "parsed_light"` 可获取 [前 10 条结果更快](/cn/scraping-automation/serp-api/introduction#get-only-top-10-results-faster-response)，或联系 [sales@brightdata.com](mailto:sales@brightdata.com) 了解 [sub-1 秒高级路由](/cn/scraping-automation/serp-api/introduction#sub-1-second-response-time)。
  </Accordion>
</AccordionGroup>
