> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 禁用验证码解决器

> 默认情况下，作为我们完整代理解锁解决方案的一部分，抓取浏览器还会解决在返回您的代理请求时遇到的验证码。

禁用验证码解决器时，我们的解锁算法仍然会负责寻找最佳代理网络、自定义标头、指纹识别等整个不断变化的流程，但故意不自动解决验证码，从而为您的团队提供轻量级、简化的解决方案，扩大潜在抓取机会的范围。

最适合：

* 在不被屏蔽的情况下从网站抓取数据
* 模拟真实用户的网络行为
* 内部没有解锁基础架构且不希望其抓取工具自动解决验证码的团队

<Accordion title="如何开始使用？">
  要禁用验证码解决功能，只需打开相关区域，转到“配置”选项卡并打开高级设置，您将在其中找到“自动验证码解决”控制器。 要禁用验证码解决功能，只需关闭开关。

  <Frame>
    <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/scraping-browser/features/captcha-solver/automatic-captcha-solving.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=1bc61d0fe66ce42bc4641973f26340ed" alt="automatic-captcha-solving.png" width="641" height="325" data-path="images/scraping-automation/scraping-browser/features/captcha-solver/automatic-captcha-solving.png" />
  </Frame>
</Accordion>

<Note>
  如果您想自行通过 CDP 命令手动配置我们的默认验证码解决器，请参阅自定义 CDP 函数:\
  [https://docs.brightdata.com/cn/scraping-automation/scraping-browser/cdp-functions/custom](https://docs.brightdata.com/cn/scraping-automation/scraping-browser/cdp-functions/custom)
</Note>
