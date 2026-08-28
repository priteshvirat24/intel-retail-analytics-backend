> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用浏览器扩展程序入门

> 通过本快速指南开始使用 Bright Data 浏览器扩展程序。

## 快速开始

按照以下步骤开始使用 Bright Data 浏览器扩展程序：

<Steps>
  <Step title="在账户中设置一个活跃的 Zone">
    要开始使用扩展程序，你需要在 Bright Data 账户中至少拥有 **一个活跃的 Zone**。

    * 前往 [My Proxies](https://www.bright.cn/cp/zones) 页面查看你现有的 Zones。
    * 如果你还没有 Zone，点击 **Add** 创建一个新的 Zone。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/active-proxy.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=96dea99593dc6aa2b89465944f9824ff" alt="active-proxy.png" width="1283" height="237" data-path="images/scraping-automation/browser-extension/quickstart/active-proxy.png" />
    </Frame>

    <Tip>
      若需查看创建 Zone 的详细说明，请参阅以下指南: [Datacenter](/cn/proxy-networks/data-center/introduction)、[ISP](/cn/proxy-networks/isp/introduction)、[Residential](/cn/proxy-networks/residential/introduction)、以及 [Mobile](/cn/proxy-networks/residential/introduction)。
    </Tip>
  </Step>

  <Step title="选择你的活跃 Zone">
    在扩展程序中，从下拉菜单中选择你想要使用的 Zone。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/select-the-zone.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=f0f6cc3a985a0d436f694dd2e3bd2ec7" alt="select-the-zone.png" width="398" height="538" data-path="images/scraping-automation/browser-extension/quickstart/select-the-zone.png" />
    </Frame>
  </Step>

  <Step title="为 Residential Zones 安装 SSL 证书（如需）">
    如果你选择 **Residential** Zone，并看到提示 *"Certificate or approved KYC are required to use residential zone"*，则需要在 Chrome 中安装我们的 SSL 证书。

    * 请参阅 [Chrome 证书安装指南](/cn/general/account/ssl-certificate#installation-instructions)。
    * 若想进一步了解 Residential 网络的接入模式，请查看 [Residential 接入指南](/cn/proxy-networks/residential/network-access)。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/kyc-certificate.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=1bfeed1e94e89be37a244cc430f1196c" alt="kyc-certificate" width="387" height="558" data-path="images/scraping-automation/browser-extension/quickstart/kyc-certificate.png" />
    </Frame>
  </Step>

  <Step title="选择国家和城市">
    选择你希望用于该 Zone 的国家，以及在可用情况下选择城市。

    <Note>
      城市级定位仅适用于 **Residential** 和 **Mobile** Zones。

      配置说明请参阅 [如何启用城市选择](/cn/proxy-networks/browser-extension/quickstart#如何启用城市选择)。
    </Note>

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/select-country.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=2f95a504620d63d6201a3f4a6b7723e8" alt="select-country.png" width="385" height="562" data-path="images/scraping-automation/browser-extension/quickstart/select-country.png" />
    </Frame>
  </Step>

  <Step title="开启代理">
    在扩展程序中开启代理，即可开始使用你选择的 Zone 浏览网页。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/turn-on-the-proxy.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=0e1d6e6be4f851065c53b720b275cb78" alt="turn-on-the-proxy.png" width="383" height="523" data-path="images/scraping-automation/browser-extension/quickstart/turn-on-the-proxy.png" />
    </Frame>
  </Step>
</Steps>

## 如何启用城市选择

1. 在控制面板中，前往 [My Proxies](https://www.bright.cn/cp/zones) 页面。
2. 打开你希望启用城市选择的 **Residential** 或 **Mobile** Zone。

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/enable-proxy.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=11b1b39ccb95a46045e4471561bfd619" alt="enable-proxy.png" width="1409" height="280" data-path="images/scraping-automation/browser-extension/quickstart/enable-proxy.png" />
</Frame>

3. 在 **Geolocation targeting** 下选择 **City**。

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/geolocation-targetting.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=1a409d283d5b94cfd160eec67dadae35" alt="geolocation-targetting.png" width="573" height="292" data-path="images/scraping-automation/browser-extension/quickstart/geolocation-targetting.png" />
</Frame>

4. 保存更改。
