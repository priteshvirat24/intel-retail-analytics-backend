> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting started with Browser extension

> Install and configure the Bright Data Browser Extension for Chrome (port 44445) to route browser traffic with 1-click country switching across 195 countries.

## Quick Start

Follow these steps to start using the Bright Data Browser Extension:

<Steps>
  <Step title="Set up an active zone in your account">
    To start using the extension, you need at least **one active zone** in your Bright Data account.

    * Check your existing zones on the [My Proxies](https://brightdata.com/cp/zones) page.
    * If you don’t have a zone yet, click **Create Proxy** to create a new zone.

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/active-proxy.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=96dea99593dc6aa2b89465944f9824ff" alt="active-proxy.png" width="1283" height="237" data-path="images/scraping-automation/browser-extension/quickstart/active-proxy.png" />
    </Frame>

    <Tip>
      For detailed instructions on creating zones, see our guides for [Datacenter](/proxy-networks/data-center/introduction), [ISP](/proxy-networks/isp/introduction), [Residential](/proxy-networks/residential/introduction), and [Mobile](/proxy-networks/residential/introduction).
    </Tip>
  </Step>

  <Step title="Select your active zone">
    In the extension, select the zone you want to use from the dropdown.

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/select-the-zone.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=f0f6cc3a985a0d436f694dd2e3bd2ec7" alt="select-the-zone.png" width="398" height="538" data-path="images/scraping-automation/browser-extension/quickstart/select-the-zone.png" />
    </Frame>
  </Step>

  <Step title="Install SSL certificate for Residential zones (if required)">
    If you select a **Residential** zone and see the message *"Certificate or approved KYC are required to use residential zone"*, you need to install our SSL certificate in Chrome.

    * Follow the [Chrome certificate installation guide](/general/account/ssl-certificate#installation-instructions).
    * To learn more about Residential network access modes, see the [Residential access guide](/proxy-networks/residential/network-access).

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/kyc-certificate.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=1bfeed1e94e89be37a244cc430f1196c" alt="kyc-certificate" width="387" height="558" data-path="images/scraping-automation/browser-extension/quickstart/kyc-certificate.png" />
    </Frame>
  </Step>

  <Step title="Select country and city">
    Choose the country and, if available, the city you want to use for your zone.

    <Note>
      City-level targeting is only available for **Residential** and **Mobile** zones.

      For setup instructions, see [How to enable city selection](/proxy-networks/browser-extension/quickstart#how-to-enable-city-selection).
    </Note>

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/select-country.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=2f95a504620d63d6201a3f4a6b7723e8" alt="select-country.png" width="385" height="562" data-path="images/scraping-automation/browser-extension/quickstart/select-country.png" />
    </Frame>
  </Step>

  <Step title="Turn on the proxy">
    Turn on the proxy in the extension to start browsing with your selected zone.

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/turn-on-the-proxy.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=0e1d6e6be4f851065c53b720b275cb78" alt="turn-on-the-proxy.png" width="383" height="523" data-path="images/scraping-automation/browser-extension/quickstart/turn-on-the-proxy.png" />
    </Frame>
  </Step>
</Steps>

## How to enable city selection

1. In your Control Panel, go to the [My Proxies](https://brightdata.com/cp/zones) page
2. Open the **Residential** or **Mobile** zone where you want to enable city selection.

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/enable-proxy.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=11b1b39ccb95a46045e4471561bfd619" alt="enable-proxy.png" width="1409" height="280" data-path="images/scraping-automation/browser-extension/quickstart/enable-proxy.png" />
</Frame>

3. Under **Geolocation targeting**, choose **City**.

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/quickstart/geolocation-targetting.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=1a409d283d5b94cfd160eec67dadae35" alt="geolocation-targetting.png" width="573" height="292" data-path="images/scraping-automation/browser-extension/quickstart/geolocation-targetting.png" />
</Frame>

4. Save your changes.
