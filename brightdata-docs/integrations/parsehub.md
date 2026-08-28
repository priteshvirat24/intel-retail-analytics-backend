> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Bright Data with ParseHub

> Integrate Bright Data proxies (400M+ IPs) with ParseHub for secure, anonymous web scraping access, reducing the risk of detection and IP bans at scale.

<Accordion title="Expand to get your Bright Data Proxy Access Information">
  ### Your proxy access information

  Bright Data proxies are grouped in "Proxy zones". Each zone holds the configuration for the proxies it holds.

  To get access to the proxy zone:

  1. Login to Bright Data control panel
  2. Select the proxy zone or setup a new one
  3. Click on the new zone name, and select the **Overview** tab.
  4. In the overview tab, under **Access details** you can find the proxy access details, and copy them to clipboard on click.
  5. You will need: Proxy Host, Proxy Port, Proxy Zone username and Proxy Zone password.
  6. Click on the copy icons to copy the text to your clipboard and paste in your tool's proxy configuration.

  ### Access Details Section Example

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### Residential proxy access

  To access Bright Data's **Residential Proxies** you must be a KYC-verified business account. Complete KYC verification with the Bright Data compliance team; there is no automatic or no-KYC path. Without KYC, use ISP or Datacenter proxies. [Read more...](/proxy-networks/residential/network-access)

  ### Targeting search engines?

  If you target a search engine like google, bing or yandex, you need a special Search Engine Results Page (**SERP**) proxy API. Use Bright Data SERP API to target search engines.
  [Click here to read more about Bright Data SERP proxy API.](/scraping-automation/serp-api/introduction)

  ### Correct setup of proxy test to avoid "PROXY ERROR"

  In many tools you will see a "test proxy" function, which performs a conncectivity test to your proxy, and some add a geolocation test as well, to identify the location of the proxy.
  To correctly test your proxy you should target those search queries to:
  `https://geo.brdtest.com/welcome.txt` .

  Some tools use popular search engines (like google.com) as a default test target. Bright Data will block those requests and you tool will show **proxy error** although your proxy is perfectly fine.

  If your proxy test fails, this is probably the reason. Make sure that your test domain is not a search engine (this is done in the tool configuration, and not controlled by Bright Data).
</Accordion>

## What is ParseHub?

ParseHub stands out as a user-friendly, powerful web scraping tool that revolutionizes data extraction from the web. Its intuitive design allows users to effortlessly interact with complex sites, manage AJAX and JavaScript elements, and navigate through forms and infinite scrolls, all without writing a single line of code. By integrating Bright Data proxies with ParseHub, users gain an unmatched advantage, seamlessly handling even the most challenging data extraction tasks with ease. This combination ensures not only efficient data scraping but also a high level of privacy and security, making it an ideal solution for professionals seeking comprehensive data collection capabilities.

## Bright Data Proxies: Empowering Your ParseHub Experience

Integrating Bright Data [proxies](https://brightdata.com/proxy-types) with ParseHub transforms your web scraping capabilities, bringing a new level of efficiency and reliability to your data extraction tasks. Here’s why Bright Data’s proxy solutions are an ideal match for ParseHub’s powerful scraping features:

**Extensive Proxy Network**

* Global Reach: Access 400M+ monthly residential IPs across 195+ countries, ensuring you can scrape data from any geographic region.
* Diverse Proxy Types: Choose from residential, datacenter, static residential, and mobile proxies to fit the specific needs of your scraping projects.

**Enhanced Anonymity and Security**

* Robust Privacy: Protect your scraping activities from detection and blocking, maintaining the anonymity of your operations.
* Secure Data Collection: Confidently scrape sensitive data with the assurance of Bright Data’s advanced security measures.

**High Performance and Reliability**

* Speed and Efficiency: Experience fast and efficient data extraction, even from complex, JavaScript-heavy websites.
* Reliable Connectivity: Minimize disruptions and maintain consistent performance with Bright Data’s stable proxy infrastructure.

**Versatile and Scalable Solutions**

* Adaptable to Various Use Cases: Whether for market research, web scraping, SEO analysis, or competitive intelligence, Bright Data’s proxies are versatile enough to handle diverse scraping scenarios.
* Scalability: Effortlessly scale your scraping operations to handle large volumes of data without compromising on speed or accuracy.

**User-Friendly Integration**

* Simple Setup: Easily integrate Bright Data proxies with ParseHub, regardless of your technical expertise.
* Comprehensive Support: Benefit from Bright Data’s extensive documentation and customer support for a smooth integration process.

## How to integrate ParseHub proxies:

<Steps>
  <Step title="Sign up to Bright Data">
    1. After signing up, go to the Bright Data dashboard
    2. Navigate to the “**Proxy & Scraping Infrastructure**” section
    3. **Add** a new designated **Zone** for your proxy usage.

    <Frame caption="Proxy management interface with active proxies and Add button">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-add-zone-2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=197765d86c20c519d8341682518d6170" alt="ph-add-zone-2.png" width="1000" height="324" data-path="images/integrations/ph-add-zone-2.png" />
    </Frame>
  </Step>

  <Step title="Select proxy type">
    In this example, we will show how to set up ISP proxies.

    <Frame caption="Proxy and scraping infrastructure dashboard with various options displayed">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-proxy-types.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=2bac00cbe6079383b2490aac6c31a7f1" alt="ph-proxy-types.png" width="500" height="257" data-path="images/integrations/ph-proxy-types.png" />
    </Frame>
  </Step>

  <Step title="Name proxy solution">
    <Frame caption="Form to choose IP type, showing Dedicated option selected">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-select-ip-type.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=f3535eac3bbfe28248d22cb1f9b7c216" alt="ph-select-ip-type.png" width="1000" height="333" data-path="images/integrations/ph-select-ip-type.png" />
    </Frame>
  </Step>

  <Step title="Select IP count">
    Fill in the number of IPs you need.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-number-of-ips-1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=7e1254af4ec21f6036eb51e7df1ef726" alt="ph-number-of-ips-1.png" width="1000" height="164" data-path="images/integrations/ph-number-of-ips-1.png" />
    </Frame>
  </Step>

  <Step title="Country & city selection">
    Choose your desired country and city for the IP location.

    <Frame caption="Geolocation targeting options for United States and New York City">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-city-ip.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=caeb7a9b784c6287d981fbbe0ad13f2b" alt="ph-city-ip.png" width="1000" height="197" data-path="images/integrations/ph-city-ip.png" />
    </Frame>
  </Step>

  <Step title="Choose domain">
    Use specific domains or use ‘All domains’ for one IP to target websites using the same IP.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-domains.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=96e7b41ab1ac33940e6e295b1a3b80a4" alt="ph-domains.png" width="1000" height="178" data-path="images/integrations/ph-domains.png" />
    </Frame>
  </Step>

  <Step title="Add zone">
    Click the “**Add**” button to create the Zone.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-click-add.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=c4b8f9bee7d223b394710884cc7d6509" alt="ph-click-add.png" width="1000" height="288" data-path="images/integrations/ph-click-add.png" />
    </Frame>
  </Step>

  <Step title="Access parameters">
    Click on the name of your Zone, navigate to the “Access Parameters” tab, and note down the proxy credentials:

    <Frame caption="Proxy service access parameters screen with host and username">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-access-parameters.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=641c5bc22d5b53de680b12d37f420b26" alt="ph-access-parameters.png" width="1000" height="625" data-path="images/integrations/ph-access-parameters.png" />
    </Frame>

    1. host: brd.superproxy.io
    2. port: 44445
    3. username: `your-zone-username`
    4. password: `your-zone-password`
  </Step>

  <Step title="Download and Install ParseHub">
    <Frame caption="ParseHub download options: Mac, Windows, Linux">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-parsehub.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=26a4e7b84f81389e54365fa7e41dac44" alt="ph-parsehub.png" width="512" height="320" data-path="images/integrations/ph-parsehub.png" />
    </Frame>

    * Visit the official website of ParseHub, download, and install the ParseHub application suitable for your operating system.
    * Launch ParseHub and either create a new account or log into your existing account.
  </Step>

  <Step title="Create a New Project">
    Click on the “+ New Project” button from the ParseHub home screen.

    <Frame caption="Dashboard with project creation and tutorials screen">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-create-a-new-project.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=5dc6014906f4e0c87b989da860a98c1f" alt="ph-create-a-new-project.png" width="512" height="280" data-path="images/integrations/ph-create-a-new-project.png" />
    </Frame>
  </Step>

  <Step title="Start a New Project with a URL">
    Insert a URL from which you wish to scrape data (for example, instagram.com) and press “Start project on this URL”.

    <Frame caption="Web scraping tool interface with tutorials and instructions">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-start-new-project.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=e03035acadca14abdc74fa4861c80cc2" alt="ph-start-new-project.png" width="512" height="280" data-path="images/integrations/ph-start-new-project.png" />
    </Frame>
  </Step>

  <Step title="Navigate to Proxy Configuration in ParseHub">
    Switch to the Browser mode, slider turns green to indicate browsing mode.

    <Frame caption="Instagram login page with an image preview displayed">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-broswer-mode.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=5c29f24f34fb23a6bd00f234752d920d" alt="ph-broswer-mode.png" width="512" height="280" data-path="images/integrations/ph-broswer-mode.png" />
    </Frame>
  </Step>

  <Step title="Settings">
    Open the settings located at the top-right side of the Browser interface and click on “options”.

    <Frame caption="Instagram webpage with phone screen simulation tool">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-open-settings.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=550402f843bf17bc4082f98e6453f91f" alt="ph-open-settings.png" width="512" height="280" data-path="images/integrations/ph-open-settings.png" />
    </Frame>
  </Step>

  <Step title="Access Advanced Network Settings">
    Select the “Advanced” tab.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-advanced-network-settings.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=8a63d3438cc170cc330220ac3732fd22" alt="ph-advanced-network-settings.png" width="512" height="280" data-path="images/integrations/ph-advanced-network-settings.png" />
    </Frame>
  </Step>

  <Step title="Click on the “Network” tab">
    Under “Connection” choose “Settings”.

    <Frame caption="Browser settings and error messages shown">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-connection-settings.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=83d24dca9b797ca1d968869e9788b56c" alt="ph-connection-settings.png" width="512" height="280" data-path="images/integrations/ph-connection-settings.png" />
    </Frame>
  </Step>

  <Step title="Configure Manual Proxy Settings">
    In the network settings, select “Manual proxy configuration”.

    <Frame caption="Configuring manual proxy settings in browser options">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-configure-manual-settings.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=62fadde37cc60af7ce1b0d95aa258932" alt="ph-configure-manual-settings.png" width="512" height="280" data-path="images/integrations/ph-configure-manual-settings.png" />
    </Frame>
  </Step>

  <Step title="Proxy settings">
    Under HTTP Proxy field enter the Bright Data proxy URL **brd.superproxy.io** and port as **44445**.

    <Frame caption="Proxy configuration settings in a browser window screenshot">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-proxy-and-port.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=be4f9035fa8ccedf36fd2615b2600e00" alt="ph-proxy-and-port.png" width="512" height="280" data-path="images/integrations/ph-proxy-and-port.png" />
    </Frame>
  </Step>

  <Step title="Switch to SOCKS v4 and click ok">
    After you switched to the SOCKS v4, click the ‘OK’ button.

    <Frame caption="Configuring proxy settings in the browser options window">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-switch-to-socks.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=4893c75686e8f77617c8355808294351" alt="ph-switch-to-socks.png" width="512" height="280" data-path="images/integrations/ph-switch-to-socks.png" />
    </Frame>
  </Step>

  <Step title="Proxy zone credentials">
    Insert your proxy zone’s credentials , they can be found on your proxy zone’s access parameters.

    <Frame caption="Password authentication popup window on a computer screen">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-access-param-parsehub.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=90f80976925911bb3f4df0bb8a544a15" alt="ph-access-param-parsehub.png" width="512" height="274" data-path="images/integrations/ph-access-param-parsehub.png" />
    </Frame>
  </Step>

  <Step title="Format Proxy Configuration">
    * Format your proxy details as IPAddress:Port:Username:Password:Realm.
    * In case of Bright Data Proxies it will be:\
      `brd.superproxy.io:44445:brd-customer-hl_******-zone-isp_proxy6:b1s*****:BrightData`

    Apply Configured Proxy to ParseHub Project:

    * Navigate to your project settings in ParseHub.

    <Frame caption="Instagram webpage with settings menu open">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-project-settings.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=a4d81fb681c8d98bd9a07440a515db14" alt="ph-project-settings.png" width="512" height="280" data-path="images/integrations/ph-project-settings.png" />
    </Frame>
  </Step>

  <Step title="Enable Custom Proxies">
    Check “Rotate IP Addresses” to enable the “Custom Proxy” text box.

    <Frame caption="Instagram scraping tool interface for data extraction">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-custom-proxies.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=99528333076421d33ea098e5f63fdf0b" alt="ph-custom-proxies.png" width="512" height="280" data-path="images/integrations/ph-custom-proxies.png" />
    </Frame>
  </Step>

  <Step title="Custom proxies field">
    Paste your formatted proxy into the “Custom Proxies” field. For multiple proxies, list each one on a separate line.

    <Frame caption="Instagram interface showing user conversation and login page">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-custom-proxies-field.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=46d85411a758d47aca315bf8bf0ab4a2" alt="ph-custom-proxies-field.png" width="512" height="280" data-path="images/integrations/ph-custom-proxies-field.png" />
    </Frame>
  </Step>

  <Step title="Save your project settings">
    After saving, run it with your Bright Data Proxies.

    <Frame caption="Instagram login page with phone message interface">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ph-save-project.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=d931726e622c0074eb3fe4f72f20d894" alt="ph-save-project.png" width="512" height="280" data-path="images/integrations/ph-save-project.png" />
    </Frame>
  </Step>
</Steps>

<Warning>
  **Important note**:

  If you are using Bright Data’s Residential Proxies, Web Unlocker API or SERP API, you need to install an SSL certificate to enable end-to-end secure connections to your target website(s).

  This is a simple process, see [this guide](/general/account/ssl-certificate#installation-of-the-ssl-certificate) for instructions.
</Warning>
