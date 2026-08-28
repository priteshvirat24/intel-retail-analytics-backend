> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题解答

<AccordionGroup>
  <Accordion title="我在哪里可以找到我的凭证，例如主机名、用户名和密码？">
    您的凭证可以在您创建的每个区域 (Zone) 的“概览 (Overview)”选项卡中找到。

    1. 在侧边栏中，点击“代理与爬虫 (Proxies and Scraping)”，然后
    2. 您将看到您创建的所有现有产品的表格。
    3. 点击每一行即可查看每个产品的凭证。
    4. 点击“概览 (Overview)”选项卡，您将看到访问该产品所需的用户名和密码。
  </Accordion>

  <Accordion title="成本结构是否因国家/地区而异？">
    不，所有国家/地区每 GB 的收费标准都相同。
  </Accordion>

  <Accordion title="对于不同的域名，我的收费是否不同？">
    某些域名需要特殊的权限或产品。

    如果您不确定哪种产品适合您的用例，最好联系您的专属客户经理或支持团队进行集成会话。
  </Accordion>

  <Accordion title="我可以限制我的每日使用量吗？">
    是的。

    在 [区域 (Zone) 页面](https://www.bright.cn/cp/zones)中，“使用支出限制 (Usage spent limit)”列下，可以通过 2 种方式限制您的每日使用量：

    * 带宽 (bytes)
    * 支出金额 (Dollars)

    一旦达到每日使用量，区域将自动暂停。

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/account/billing-and-pricing/cost-structure/limit-daily-usage.gif?s=067051d119536104bf05678133142492" alt="limit-daily-usage.gif" width="1636" height="930" data-path="images/general/account/billing-and-pricing/cost-structure/limit-daily-usage.gif" />
    </Frame>

    <Tip>
      区域限制每 15 分钟计算一次，不会立即生效，因此区域可能会超出其限制 15 分钟的使用量。
    </Tip>

    <Note>
      当负载较高时，统计数据计算可能会有延迟。为了手动更新您的区域中的使用统计数据，请点击区域名称打开区域，转到“统计数据 (Statistics)”表格，然后按下所需日期旁边的 `recalc` 按钮。等待屏幕顶部的红色“正在加载...”通知消失，然后刷新页面。此时统计数据将是最新的。
    </Note>
  </Accordion>

  <Accordion title="我可以在没有月度承诺的情况下使用 Bright Data 吗？">
    当然可以！

    您可以在没有月度承诺的情况下使用 Bright Data 数据中心、ISP、住宅和移动网络。\
    只需点击区域名称旁边的铅笔图标，将计划调整为“即用即付 (Pay-As-You-Go)”

    <Note>
      如果 IP 类型是按 IP/专用类型或 gips 付费，您将需要为分配给该区域的 IP 付费。
    </Note>
  </Accordion>

  <Accordion title="谁有资格获得免费试用？">
    每个注册 Bright Data 的用户都会自动获得免费试用，可用于所有 Bright Data 产品。每个新账户还会获得一个每月循环的[免费套餐](/cn/general/account/billing-and-pricing/free-tier)，可在 Web Unlocker API、SERP API、Web Scraper API 和 Scraper Studio 上使用 5,000 个信用额度，按月续期。

    有关更多详细信息，请[参阅此处](/cn/general/faqs#什么是-playground-模式)。

    <Info>
      以帮助进行试用配置。
    </Info>
  </Accordion>

  <Accordion title="你们有任何高级定价计划吗？">
    是的，我们的数据中心和 ISP 计划涵盖无限数据量。\\

    <Info>
      请联系您的客户经理以获取每月无限流量计划的信息
    </Info>
  </Accordion>

  <Accordion title="如何管理我的账单详情？">
    要管理您的账单详情，请访问 [https://www.bright.cn/cp/billing/settings](https://www.bright.cn/cp/billing/settings) 。在那里，您可以添加新的付款方式、删除现有的付款方式、设置您的账户的主要付款方式，并配置您的余额提醒。
  </Accordion>

  <Accordion title="支持哪些付款方式？" defaultOpen="false">
    Brightdata 支持通过以下方式付款：

    * PayPal
    * 支付宝 (AliPay)
    * Payoneer
    * 信用卡 (Credit Card)：VISA、MasterCard、American Express
    * 电汇 (Wire transfer)
    * 亚马逊应用商店 (Amazon Marketplace)

    我们**不**支持通过加密货币付款。
  </Accordion>

  <Accordion title="带宽如何计算？ " defaultOpen="false">
    Bandwidth is calculated based on the data transmitted through the proxy peer. For instance, if a webpage has a size of 100 KB, the billed bandwidth will include this 100 KB along with a minimal additional amount to account for network overhead, such as the TCP handshake and other related operations. Billing is precise and measured down to the megabyte (MB), with no rounding up of bandwidth usage. To see a detailed breakdown of your costs consumption, please see: [Billing Overview](https://www.bright.cn/cp/billing/overview) and there click on the 'breakdown' link.

    <Note>
      If a request is passed through the super proxy it will not be billed
    </Note>
  </Accordion>

  <Accordion title="为什么我收到“付款失败”错误？ " defaultOpen="false">
    The payment failed error could occur due to several reasons, to see the exact cause in your case you should check your [transactions table](https://www.bright.cn/cp/billing/transactions), there you will find instructions on how to resolve your issue.  If you require any further assistance, you can contact or sales department at [sales@brightdata.com](mailto:sales@brightdata.com)
  </Accordion>

  <Accordion title="为什么我的促销代码不适用，并收到“已达到最大激活次数”错误？">
    这意味着该促销代码的激活次数过多。请等到第二天再试，或联系我们的支持团队。
  </Accordion>
</AccordionGroup>
