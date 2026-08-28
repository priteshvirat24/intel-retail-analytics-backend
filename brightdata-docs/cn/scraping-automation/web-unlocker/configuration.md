> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Unlocker API 配置

> 使用 Premium Domains、地理位置以及高级设置（自定义 headers、cookies、自动限速）来配置 Web Unlocker API。

## Premium Domains

有些域名比其他域名更难解锁，因此我们为[这些域名](/cn/scraping-automation/web-unlocker/features#current-list-of-premium-domains)提供了独立的高级定价层级。启用后，高级价格将显示在 “Estimated cost” 区域中。\
<Note>即使启用了该功能，也只有对这些域名的特定请求会按高级价格计费。对其他域名的请求仍按默认的低价 tier 计费。</Note>

## 高级选项

### 异步请求

请求会在后台无缝处理，使您可以在更方便的时间通过指定的 endpoint 获取响应，从而提高稳定性、灵活性和效率。

了解更多关于[异步请求](/cn/scraping-automation/serp-api/asynchronous-requests)。

### 自定义 Web Unlocker API

覆盖自动 headers/cookies，并发送您自己的自定义值，以便定位网站的特定版本。

<Note>
  启用 **Custom Headers & Cookies** 会导致以下情况：

  <AccordionGroup>
    <Accordion title="访问预批准的 Headers/Cookies 列表">
      您将获得一个预批准的 headers 和 cookies 列表。您可以浏览此列表以确认目标站点所需的 headers 和 cookies 是否已被允许。
    </Accordion>

    <Accordion title="提交新 Headers/Cookies 的申请">
      如果所需的 headers 或 cookies 不在预批准列表中，您可以提交表单给我们的合规团队进行审批。此流程需要提供这些 headers/cookies 的用途相关信息。审批完成后，我们的合规团队会通知您。
    </Accordion>

    <Accordion title="对所有请求收费">
      与普通 Web Unlocker API 仅对成功请求收费不同，启用此功能后，您将对 100% 的请求计费（包含成功和失败）。这是因为 Bright Data 对整个过程及其表现没有完全控制权。
    </Accordion>
  </AccordionGroup>
</Note>

#### 允许自定义 Headers & Cookies

1. 访问您的控制面板：登录 Bright Data 控制面板。
2. 选择您的 Zone：选择您希望启用此功能的具体 zone。
3. 启用功能：在 **Advanced Options** 中找到并激活 zone 设置中的 “Custom headers & cookies” 权限。

#### 控制自动限速（Auto-Throttling）

Web Unlocker API 内置自动限速机制，以维持高效 scraping 和稳定性能。该系统按以下方式运行：

<Tabs>
  <Tab title="自动调整">
    系统会自动搜索并应用表现更好的配置。
  </Tab>

  <Tab title="当成功率较低时">
    如果目标站点的成功率低于某个百分比，系统将开始限制请求，以避免在失败配置上浪费资源。
  </Tab>

  <Tab title="可自定义阈值">
    该机制的默认阈值为 70%。

    但是，如果您启用了 “Custom headers & cookies” 权限，您可以根据需求将此阈值调整为任意百分比，尤其是因为无论请求成功与否都将计费。
  </Tab>
</Tabs>
