> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何开始使用代理管理器

> 通过选择云服务器或本地部署，开始使用 Bright Data 的代理管理器，然后开始管理和自定义代理以获得最佳性能。

<Tip>
  如果您尚未注册 Bright Data，则可以免费注册，添加付款方式时，您将获得价值 \$5 的积分以开启服务！\
  [https://www.bright.cn/](https://www.bright.cn/)
</Tip>

<Steps>
  <Step title={<a href="https://www.bright.cn/cp/start">登录</a>} />

  <Step title="选择您的首选方法">
    <CardGroup cols={2}>
      <Card title="云服务器（推荐）" href="/proxy-networks/proxy-manager/configuration#bright-data-cloud-hosting" icon="cloud" />

      <Card title="本地部署" href="/proxy-networks/proxy-manager/configuration#local-remote-installation" icon="house">
        您负责安装、管理和监控
      </Card>
    </CardGroup>

    <Accordion title="云服务器的优势">
      * 无需安装或服务器设置 - 从任何地方直接登录我们的[Web 应用程序](https://www.bright.cn/cp/zones/lpm)
      * 端到端托管解决方案
      * 由 Bright Data 24/7 全天候团队进行的实时服务器状态监控。要查看有关安装和设置的更多信息，请参阅[介绍视频](https://www.bright.cn/webinar/how-to-start-using-the-bright-data-proxy-manager)。
      * 支持 SSL 分析，可选择 OpenSSL 或 BoringSSL。BoringSSL 是 Bright Data 自研实现，可提供额外的解锁能力。
    </Accordion>
  </Step>

  <Step title="开始管理您的代理">
    安装代理管理器后，您可以登录并开始管理您的代理，使用您的区域设置所配置的端口进行设置 。
  </Step>

  <Step title="实现规则和标头">
    现在您可以[实施规则和标头](/cn/proxy-networks/proxy-manager/configuration#规则和标头配置)来根据您的需求自定义您的代理。这将确保带宽使用更具成本效益，并获得更准确的结果。
  </Step>
</Steps>
