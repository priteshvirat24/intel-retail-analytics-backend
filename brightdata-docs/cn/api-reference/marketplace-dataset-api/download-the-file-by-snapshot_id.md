> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快照内容

> 获取数据集快照内容



## OpenAPI

````yaml cn-dca-api GET /datasets/snapshots/{id}/download
openapi: 3.1.0
info:
  title: Brightdata API
  description: 用于与数据集市场交互的 API
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/snapshots/{id}/download:
    get:
      description: 获取数据集快照内容
      parameters:
        - in: path
          name: id
          description: >-
            快照 ID 是特定数据快照的唯一标识符，用于通过 API 触发的数据采集任务中获取结果。更多信息请参阅 [Snapshot
            ID](/cn/api-reference/terminology#snapshot-id)。
          required: true
          schema:
            type: string
            example: snap_m2bxug4e2o352v1jv1
        - in: query
          name: format
          description: 响应格式
          schema:
            $ref: '#/components/schemas/DeliveredFileExt'
            default: jsonl
        - in: query
          name: compress
          description: 使用 gzip 格式压缩响应
          schema:
            type: boolean
            default: false
        - in: query
          name: batch_size
          description: 每个响应批次中包含的记录数量
          schema:
            type: integer
            minimum: 1000
        - in: query
          name: part
          description: 要返回的批次编号，编号从 1 开始
          schema:
            type: integer
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetSnapshotContent'
        '202':
          description: 快照未准备好
          content:
            text/html:
              schema:
                type: string
                example: 快照正在生成，请几分钟后重试
        '400':
          description: 错误请求
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: '#/components/schemas/ErrorBody'
                    example:
                      error: 快照未准备好
                  - $ref: '#/components/schemas/ValidationErrorBody'
                    example:
                      validation_errors:
                        - '"format" 必须是 [json, ndjson, jsonl, csv] 中之一'
                        - '"compress" 必须为布尔值'
                        - '"batch_size" 必须大于或等于 1000'
                        - '"part" 必须大于或等于 1'
        '404':
          description: 未找到快照
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: 未找到快照
components:
  schemas:
    DeliveredFileExt:
      type: string
      enum:
        - json
        - jsonl
        - csv
    DatasetSnapshotContent:
      type: object
      example:
        about: >-
          Bitstamp 是全球运营时间最长的加密货币交易所，自 2011
          年起持续支持比特币经济。凭借成熟的行业经验和良好的业绩记录，Bitstamp
          为超过四百万客户提供安全透明的交易平台，并通过经过时间验证的基础设施使合作伙伴能够进入新兴的加密市场。NMLS ID: 1905429 在
          NMLS 网站查看更多:
          https://www.nmlsconsumeraccess.org/EntityDetails.aspx/COMPANY/1905429
        affiliated: []
        company_id: '2734818'
        company_size: 501-1,000 名员工
        country_code: LU
        crunchbase_url: >-
          https://www.crunchbase.com/organization/bitstamp?utm_source=linkedin&utm_medium=referral&utm_campaign=linkedin_companies&utm_content=profile_cta_anon&trk=funding_crunchbase
        description: "Bitstamp | 30,341 位 LinkedIn 粉丝。全球运营时间最长的加密交易所 | Bitstamp 是全球运营时间最长的加密货币交易所，自 2011 年起持续支持比特币经济。凭借成熟的行业经验和良好的业绩记录，Bitstamp 为超过四百万客户提供安全透明的交易平台，并通过经过时间验证的基础设施使合作伙伴能够进入新兴的加密市场。\n\n\n\n\nNMLS ID:\t1905429\n在 NMLS 网站查看更多: https://www.nmlsconsumeraccess.org/EntityDetails.aspx/COMPANY/1905429"
        employees:
          - img: >-
              https://media.licdn.com/dms/image/D4E03AQGixwSI9R6RuQ/profile-displayphoto-shrink_100_100/0/1701888289576?e=2147483647&v=beta&t=JCC9EZgKl5VWFcV_qdHIlvE7ZScFDTQeMOcrMrmU5TA
            link: https://ae.linkedin.com/in/jsgreenwood?trk=org-employees
            subtitle: 执行领导与数字化转型
            title: James Greenwood
          - img: >-
              https://media.licdn.com/dms/image/C4E03AQGD22qBJsQ-qw/profile-displayphoto-shrink_100_100/0/1524161393516?e=2147483647&v=beta&t=OSS74hoSvrpwsPjEuuF0AmafkMxX9gf_-j5w4XHXG8o
            link: https://uk.linkedin.com/in/benjamin-parr-940491?trk=org-employees
            subtitle: 加密货币全球首席营销官
            title: Benjamin Parr
          - img: >-
              https://media.licdn.com/dms/image/C4D03AQFdUs4Av5rygg/profile-displayphoto-shrink_100_100/0/1516264422356?e=2147483647&v=beta&t=UOtNggS62Q8IyXGN4PosDnhqOhQjJN8AHRBB78zLlXs
            link: https://si.linkedin.com/in/dominikznidar?trk=org-employees
            subtitle: 高级后端开发工程师
            title: Dominik Znidar
          - img: >-
              https://media.licdn.com/dms/image/C4D03AQFFTmCpr_pIJQ/profile-displayphoto-shrink_100_100/0/1619005680916?e=2147483647&v=beta&t=Waxiqdk9WwM6YR2zD9c_k3KphlAocoylB8k2FU832pY
            link: >-
              https://lu.linkedin.com/in/stephen-bearpark-27aa5b?trk=org-employees
            subtitle: Bitstamp 首席财务官
            title: Stephen Bearpark
        employees_in_linkedin: 365
        followers: 30341
        formatted_locations:
          - 卢森堡, 卢森堡 L-2520, LU
        founded: 2011
        funding:
          last_round_date: '2023-06-24T00:00:00.000Z'
          last_round_type: 企业轮融资
          rounds: 3
        get_directions_url:
          - directions_url: >-
              https://www.bing.com/maps?where=Luxembourg+L-2520+Luxembourg+LU&trk=org-locations_url
        headquarters: 卢森堡, 卢森堡
        id: bitstamp
        image: >-
          https://media.licdn.com/dms/image/D4D3DAQFefkROuFwk5A/image-scale_191_1128/0/1697616530874/bitstamp_cover?e=2147483647&v=beta&t=R9eU5nQ8J-F3kbGES6-aVLhyLnQQ22lTFwhcNOd0fvg
        industries: 金融服务
        input:
          url: https://www.linkedin.com/company/2734818
        investors:
          - Ripple
        locations:
          - 卢森堡, 卢森堡 L-2520, LU
        logo: >-
          https://media.licdn.com/dms/image/D4D0BAQF_ZNbRZzKn0Q/company-logo_200_200/0/1704443361832/bitstamp_logo?e=2147483647&v=beta&t=ON2r3XfdPTbdlCABksfDNCedtHSkO2z9ReQCEI3ihN0
        name: Bitstamp
        organization_type: 私人持有
        similar:
          - Links: https://www.linkedin.com/company/krakenfx?trk=similar-pages
            subtitle: 金融服务
            title: Kraken Digital Asset Exchange
          - Links: https://vg.linkedin.com/company/bitfinex?trk=similar-pages
            subtitle: 金融服务
            title: Bitfinex
          - Links: https://sc.linkedin.com/company/kucoin?trk=similar-pages
            subtitle: 金融服务
            title: KuCoin Exchange
          - Links: https://www.linkedin.com/company/bybitexchange?trk=similar-pages
            subtitle: 金融服务
            title: Bybit
          - Links: https://www.linkedin.com/company/geminitrust?trk=similar-pages
            location: 纽约, NY
            subtitle: 金融服务
            title: Gemini
          - Links: https://www.linkedin.com/company/coinbase?trk=similar-pages
            subtitle: 互联网出版
            title: Coinbase
          - Links: https://www.linkedin.com/company/binance?trk=similar-pages
            subtitle: 软件开发
            title: Binance
          - Links: https://www.linkedin.com/company/okxofficial?trk=similar-pages
            subtitle: IT 服务与 IT 咨询
            title: OKX
          - Links: https://ky.linkedin.com/company/gateio?trk=similar-pages
            subtitle: 金融服务
            title: Gate.io
          - Links: >-
              https://sc.linkedin.com/company/htxglobalofficial?trk=similar-pages
            subtitle: 金融服务
            title: HTX
        slogan: 全球运营时间最长的加密交易所
        specialties: null
        sphere: 金融服务
        stock_info: null
        type: 私人持有
        updates:
          - comments_count: 5
            external_link: >-
              https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fen%2Ethebigwhale%2Eio%2Farticle-en%2Fjean-baptiste-graftieaux-bitstamp-we-are-going-to-launch-a-fully-regulated-derivatives-offering&urlhash=0UL3&trk=organization_guest_main-feed-card_feed-article-content
            images:
              - >-
                https://media.licdn.com/dms/image/sync/D4E27AQEZaBxV1lGFPQ/articleshare-shrink_800/0/1707981346426?e=2147483647&v=beta&t=Y3ZngwpKLa7Xoz6TzgVNzJZYmMk6Fdom59LHlvbZ3Ns
            likes_count: 89
            text: >-
              在接受 The Big Whale 独家采访时，我们的首席执行官 JB Graftieaux
              讨论了我们对企业服务扩展的承诺，并宣布“我们将推出完全受监管的衍生品服务。”JB Graftieaux 强调了 Bitstamp
              在推动支付技术演进中的作用，尤其是为希望接受加密货币的企业。Bitstamp 专注于为 B2B 和 B2B2C
              客户扩展服务，提供全面解决方案，赋能企业在当今快速发展的金融环境中取得成功。从与斯图加特证券交易所和 Revolut
              等市场参与者合作，到为银行提供白标解决方案，Bitstamp
              在推动机构采用加密货币方面处于前沿。秉持合规与以客户为中心的理念，我们致力于提供可信、安全和创新的解决方案，以满足客户的多样化需求。阅读全文:
              https://lnkd.in/dgW8FPtN
            time: 5天前
            title: Bitstamp
          - external_link: >-
              https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fconsensus2024%2Ecoindesk%2Ecom%2Fcommunity-session-voting%2F&urlhash=BzoD&trk=organization_guest_main-feed-card_reshare_feed-article-content
            images:
              - >-
                https://media.licdn.com/dms/image/sync/D5627AQE38PPAJZjCag/articleshare-shrink_800/0/1708030264958?e=2147483647&v=beta&t=pv8BCKVgL_XH4cEPcCCGrqax1jHeAGPQ1f16oSN24Bc
            likes_count: 1
            text: >-
              🔔 今天是为 CoinDesk Consensus 2024 的“DeFi for Capital
              Markets”小组投票的最后一天！如果您还没有投票，我们鼓励您立即投票！您的投票可能带来改变。🗳️ #DeFi
              #Consensus2024
            time: 5天前 3周
            title: Bitstamp
          - likes_count: 22
            text: >-
              从新兴人才到行业领袖。我们致力于赋能每个人的职业发展。想听听我们团队成员的声音？查看视频。想与我们一起培养您的潜力？探索当前的招聘岗位。🔹
              加密团队负责人 (斯洛文尼亚 & 克罗地亚): https://lnkd.in/dnMm3XWW 🔹 高级软件工程师 - 加密
              (斯洛文尼亚 & 克罗地亚): https://lnkd.in/d38sC7Ui 🔹 高级技术支持工程师 (斯洛文尼亚 &
              克罗地亚): https://lnkd.in/dv3vmP3P 🔹 云运维工程师 - 加密 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/d7M7_f5h 🔹 定价、流动性与市场经理 (斯洛文尼亚 & 英国):
              https://lnkd.in/dNSB4Tjp 🔹 业务运营与战略经理 - 资产上市 (斯洛文尼亚 & 英国):
              https://lnkd.in/g_7n_e3T 探索我们的招聘页面: https://lnkd.in/d6MTnSFi
              #WorkingAtBitstamp
            time: 6天前
            title: Bitstamp
            videos:
              - null
          - comments_count: 1
            likes_count: 31
            text: >-
              我们推出最新上市的加密资产：LMWR、PEPE、BLUR 和 VEXT。LMWR 赋能内容创作者，PEPE 为加密带来趣味，BLUR
              为 NFT 带来新意，VEXT
              推动社区决策。每个精选资产都丰富了我们的平台，展示了我们提供多样选择的承诺。了解更多资产和上市时间表:
              https://lnkd.in/dykJtR4a
            time: 1周前
            title: Bitstamp
            videos:
              - null
          - comments_count: 1
            images:
              - >-
                https://media.licdn.com/dms/image/D4E22AQEKWK29cExlpw/feedshare-shrink_2048_1536/0/1707825435726?e=2147483647&v=beta&t=Iv0y53aveHyYisxmD0PdAiOKe5t15QSrgfR7n5GO2p4
              - >-
                https://media.licdn.com/dms/image/D4E22AQEVuGD2tPJufA/feedshare-shrink_800/0/1707825436409?e=2147483647&v=beta&t=jAc4jsRxdEUHfV4Z7jy7JwbaZBieFDRq63UBz9l9tkk
              - >-
                https://media.licdn.com/dms/image/D4E22AQE4-eD8H1CzDA/feedshare-shrink_800/0/1707825440601?e=2147483647&v=beta&t=RbJSdDRDxL4mT5-j1UdR4YWjplzdlDBlexmQZTfU8qk
              - >-
                https://media.licdn.com/dms/image/D4E22AQEX_VenEJ3dPQ/feedshare-shrink_800/0/1707825438877?e=2147483647&v=beta&t=0bHUwuFXFmgslpdrMxFbdjznxnWpNRPhfhleS_PP3nw
              - >-
                https://media.licdn.com/dms/image/D4E22AQEQyP-Yyo1CyQ/feedshare-shrink_800/0/1707825439584?e=2147483647&v=beta&t=EG4XLvIM2-Y7LMTmpoIgG5zerGEVrWkyDG6lUW9mPqo
            likes_count: 59
            text: >-
              上周，Bitstamp 举办了题为“新全球与数字时代的支付技术演进”的圆桌讨论活动，与布鲁内尔伦敦大学合作，由 Qi
              主导。在此次动态活动中，我们探讨了支付的未来格局，桥接传统金融与加密货币的世界。衷心感谢点燃精彩讨论的嘉宾：Qi 的 Mann
              Matharu 和 Gurnam Selvarajah，布鲁内尔伦敦大学的 Monomita Nandy，Cardstream 的
              Nic Verdino，Zodia Markets 的 Nick Philpott，CMS 律师事务所的 Charles
              Kerrigan，The Atlantic Society 的 Kari Chaudhry，以及 Bitstamp 的 James
              Sullivan 和 Lenart
              Dolžan。我们的使命？为加密支付在市场的广泛采用铺路。借助这一系列首场圆桌会议，我们奠定了变革的基础。与 Qi
              合作，我们推动支付技术演进，为企业和消费者解锁新可能。通过深度讨论和战略合作，我们共同塑造金融的未来。欢迎加入我们！
            time: 1周前
            title: Bitstamp
          - comments_count: 2
            likes_count: 26
            text: >-
              您是否在寻找一个工作具有挑战性、时间受到尊重的地方？在这里，您被鼓励在不牺牲个人生活的情况下专业成长。这就是我们在 Bitstamp
              的目标。观看视频，看看平衡如何成为我们日常的一部分。如果这听起来是您能茁壮成长的理想环境，请查看当前招聘岗位: ◼ 产品运营经理
              (斯洛文尼亚): https://lnkd.in/d2vQ9tPi ◼ 加密团队负责人 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/dnMm3XWW ◼ 软件工程师 - 加密 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/dxqXTKpk ◼ 高级软件工程师 - 加密 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/d38sC7Ui ◼ 高级技术支持工程师 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/dv3vmP3P ◼ QA 工程师 - 交易 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/dsQVU7ji ◼ 云运维工程师 - 加密 (斯洛文尼亚 & 克罗地亚):
              https://lnkd.in/d7M7_f5h ◼ 定价、流动性与市场经理 (斯洛文尼亚 & 英国):
              https://lnkd.in/dNSB4Tjp ◼ 业务运营与战略经理 - 资产上市 (斯洛文尼亚 & 英国):
              https://lnkd.in/g_7n_e3T 探索我们的招聘页面: https://lnkd.in/d6MTnSFi
              #WorkingAtBitstamp
            time: 1周前
            title: Bitstamp
            videos:
              - null
          - images:
              - >-
                https://media.licdn.com/dms/image/D5622AQGaDA-jWHS00w/feedshare-shrink_800/0/1707396968499?e=2147483647&v=beta&t=Edse9Bu4qZfP8yWlB6XM6xhLQYS0D1UUNlyusH-afiM
            likes_count: 19
            text: >-
              我们迫不及待地等待今晚与 Copper.co
              的活动，我们将为嘉宾举办专属小组讨论和品酒体验。准备好探索如何在加密领域中导航最新见解。我们的战略合作与企业发展负责人 Eva
              Gartner
              将加入专家小组，深入讨论加密托管中的安全性、风险缓解和流动性等关键主题。为复杂的加密托管与精致的品酒体验举杯庆祝，在数字资产世界中创造成功的交响曲！请注意，今晚的活动已满员。如有兴趣参加，请联系团队以加入候补名单。
            time: 1周前 编辑
            title: Bitstamp
          - external_link: >-
              https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fblog%2Ebitstamp%2Enet%2Fpost%2Fbitstamp-monthly-briefing-january-2024%2F&urlhash=q2zL&trk=organization_guest_main-feed-card_feed-article-content
            images:
              - >-
                https://media.licdn.com/dms/image/sync/D4D27AQHQLNtdTnqyXA/articleshare-shrink_800/0/1707322864200?e=2147483647&v=beta&t=ln_cWSvNOtrGWj2CqbsT2wwV5b-Mx0M44JlUOFmHE2s
            likes_count: 19
            text: >-
              Bitstamp 一月加密洞察来了。⬇
              本月简报深入探讨重塑加密世界的市场动态，并详细分析加密借贷的细节。我们旨在为这些关键领域提供有价值的见解，帮助读者在 2024
              年做出明智决策。阅读最新月度简报: https://lnkd.in/dEuMg8Rz
            time: 1周前
            title: Bitstamp
          - comments_count: 2
            images:
              - >-
                https://media.licdn.com/dms/image/D4D22AQF-6xcJCu5tyQ/feedshare-shrink_800/0/1707307881815?e=2147483647&v=beta&t=SeY1P70tTqomRvQanx4bGWuoRQYvVaACw1VzmEwvMDs
            likes_count: 29
            text: >-
              提醒注册我们的首场 LinkedIn 音频活动！📢 🗓️ 时间: 2 月 8 日星期四 15:00
              GMT！加入我们，深入探讨“机构采用加密货币：2024 年的法规与增长机会”，嘉宾阵容包括: 🎙️ Simon Barnby,
              Chloé Nightingale, Amor Sexton, Soledad Contreras, Kevin de
              Patoul, Danny Bailey, Coby L., Radoslav Poljasevic 以及 Olly Wilson
              🤝 由 Blockchain.com 赞助 🔗 请点击活动链接中的“参加”: https://lnkd.in/dYNDebUY
            time: 2周前
            title: Zebu Live - London Web3 Conference
          - external_link: >-
              https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fcryptonews%2Ecom%2Fexclusives%2Fbobby-zagotta-ceo-of-bitstamp-on-bitcoin-etf-the-halving-defi-for-capital-markets-and-2024-predictions-ep-304%2Ehtm&urlhash=72HL&trk=organization_guest_main-feed-card_feed-article-content
            images:
              - >-
                https://media.licdn.com/dms/image/sync/D5627AQEzMtolOYZaJg/articleshare-shrink_800/0/1708013936402?e=2147483647&v=beta&t=crppgb7R5w6HQ0GUEpkXYLhFsVWBu-K1Y9ta7I7Idn4
            likes_count: 38
            text: >-
              我最近与 Cryptonews 的 Matt Zahab 进行交流，讨论了一系列话题，包括比特币 ETF
              的潜力、即将到来的减半影响，以及 DeFi 如何塑造资本市场的未来。我还分享了一些对 2024
              年加密领域的看法。这是一次发人深省的对话，为对金融未来感兴趣的人提供了宝贵见解。阅读全文:
              https://lnkd.in/gtyUtMGt #Podcast #Bitcoin Bitstamp
            time: 2周前
            title: Bobby Zagotta
        url: https://www.linkedin.com/company/bitstamp
        website: https://www.bitstamp.net/
    ErrorBody:
      type: object
      properties:
        error:
          type: string
    ValidationErrorBody:
      type: object
      properties:
        validation_errors:
          type: array
          items:
            type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        在 Authorization 头中使用您的 Bright Data API Key 作为 Bearer token。


        **认证方法:**

        1. 从 Bright Data 账户设置获取您的 API Key:
        https://brightdata.com/cp/setting/users

        2. 在请求的 Authorization 头中包含 API Key

        3. 格式: `Authorization: Bearer YOUR_API_KEY`


        **示例:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        了解如何获取 Bright Data API Key:
        https://docs.brightdata.com/cn/api-reference/authentication#如何生成新的-api-key？
      bearerFormat: API Key

````