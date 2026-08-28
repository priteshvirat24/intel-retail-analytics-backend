> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bright Data's Scraping Shield

抓取盾牌提供有关客户传出代理流量的数据，以使他们能够更好地控制流量；此外，它还允许在满足某些条件时触发预定义的操作，例如：发送电子邮件警报，阻止请求等。

## 抓取盾牌功能

### 域分类

域分类功能将来自客户代理操作的传出流量分为购物、社交媒体和旅行等组别。客户可以查看每个类别的流量，向下钻取以查看特定的域名。 他们还可以设置规则，阻止特定类别或域使用代理，并在有人尝试访问时提醒指定用户。

<Accordion title="我可以在域分类页面看到什么？">
  在域分类页面，您可以查看显示您账户中所有传出代理流量的图表。 此图表可以按分类、域或区域进行细分。

  <Frame>
    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/bright-shield/scraping-shield/traffic-chat.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=df526d3f630e8b027ee705e6305efb41" alt="流量图" width="473" height="381" data-path="images/scraping-automation/bright-shield/scraping-shield/traffic-chat.png" />
  </Frame>

  此外，还有一个表格显示按分类细分的所有流量。 客户可以展开此表的每一行，查看所使用的特定域或区域，以及请求数量和这些域/区域的流量。

  <Frame>
    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/bright-shield/scraping-shield/classification-table.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=d2d65bd7dc2d9a9fd868d3f3a383cd96" alt="分类表" width="1280" height="281" data-path="images/scraping-automation/bright-shield/scraping-shield/classification-table.png" />
  </Frame>

  客户还可以添加规则，在针对特定类别/域时执行特定操作。
</Accordion>

### 添加和使用规则

规则可使客户能够根据传出流量的分类或域设置特定的操作或警报。 这些规则包括阻止对某些分类或域的请求以及在针对特定类别或域时设置警报的功能。

有两种添加规则的方法：

<Tabs>
  <Tab title="从头开始创建规则">
    * 登录您的账户，转到域分类页面。
    * 选择页面顶部的 “规则” 选项卡。
    * 点击 “添加规则”
    * 选择规则应适用于整个分类还是特定域
    * 启用“阻止请求”复选框后，将会阻止对所选分类/域的所有请求。
    * 当向所选分类/域发送最少数量的请求时，“通知...” 复选框将允许您向指定用户发送警报。

          <Frame>
            <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/bright-shield/scraping-shield/create-rule-from-scratch.gif?s=158838dfb66b425be3183647a15ca520" alt="从头开始创建规则" width="1388" height="738" data-path="images/scraping-automation/bright-shield/scraping-shield/create-rule-from-scratch.gif" />
          </Frame>
  </Tab>

  <Tab title="根据统计表创建规则">
    * 登录您的账户，转到域分类页面。
    * 查看图表下方的表格，并选择要添加规则的分类或域。
    * 将鼠标悬停在所选分类或域的规则单元格上，然后点击“+”图标。
    * 启用“阻止请求”复选框后，将会阻止对所选分类/域的所有请求。
    * 当向所选分类/域发送最少数量的请求时，“通知...” 复选框将允许您向指定用户发送警报。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/bright-shield/scraping-shield/create-rule-from-table.gif?s=99d00317289150c259f65459e3155986" alt="根据统计表创建规则" width="1388" height="768" data-path="images/scraping-automation/bright-shield/scraping-shield/create-rule-from-table.gif" />
    </Frame>
  </Tab>
</Tabs>

***

<Accordion title="正在下载示例请求">
  您可以查看从您的账户发送到所选域的示例请求，其中包括请求的时间戳、源 IP、区域、带宽（以字节为单位）和请求的总持续时间。
</Accordion>

## 抓取盾牌 - 计费

抓取盾牌的定价最低为每月 1 万美元。而对于每月使用成本超过 20 万美元的客户，价格将会使其使用成本增加 5％。（实际使用成本，而非月度承诺本身）。

例如，使用成本为每月 15 万美元的客户每月支付最低 1 万美元，而每月使用成本为 22 万美元的客户每月支付 1.1 万美元。

使用成本是使用服务所花费的总金额，仅考虑与抓取盾牌使用相关的产品：所有代理产品、网页抓取工具 IDE和自定义数据集。（除市场数据集之外的所有产品）

<Tip>
  [点击这里](/cn/api-reference/scraping-shield-api/all-classification-data) 了解 Scraping Shield API 参考文档
</Tip>
