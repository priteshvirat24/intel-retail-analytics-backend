> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Bright Data with SaleFreaks

> Integrate Bright Data proxies (400M+ IPs) with SaleFreaks to manage dropshipping automation securely, protect seller accounts and reduce IP-related risks.

<Warning>
  **Account management is not a supported use case** on the Bright Data platform as of April 1, 2026. This includes managing accounts on platforms like TikTok, Instagram, or similar services. Bright Data proxies cannot be used for this purpose. See [Acceptable Use Policy](https://brightdata.com/acceptable-use-policy) for details.
</Warning>

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

## What is SaleFreaks?

SaleFreaks is an automation platform built for dropshippers to manage online stores more efficiently. It helps automate key workflows such as product sourcing, order fulfillment, and inventory synchronization. SaleFreaks commonly integrates with marketplaces like eBay and Amazon, where stable IP usage is critical to avoid account flags or suspensions.

Using Bright Data proxies with SaleFreaks improves account safety, enables geo-targeted operations, and ensures long-term automation stability.

***

## Why Use Bright Data With SaleFreaks?

* **Account Protection**: Reduce the risk of marketplace bans by using dedicated, consistent IPs
* **Geo-Targeting**: Operate seller accounts from specific countries or cities
* **High Stability**: Dedicated datacenter or ISP proxies ensure uninterrupted automation
* **Scalability**: Manage multiple seller accounts with isolated proxy identities

***

## Steps to Integrate SaleFreaks With Bright Data Proxies

### Step 1. Sign Up to Bright Data

1. Log in to your Bright Data dashboard
2. Navigate to **Proxy & Scraping Infrastructure**
3. Click **Add** to create a new proxy **Zone**

<Frame caption="Proxy management interface with active proxies and Add button">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/add-zone-2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=9b45ed83ff4aa731930224ee9af281c9" alt="add-zone-2.png" width="1000" height="324" data-path="images/integrations/add-zone-2.png" />
</Frame>

***

### Step 2. Select Proxy Type

For SaleFreaks, **Datacenter or ISP proxies** are recommended for maximum account stability.

<Frame caption="Web interface for managing proxies and scraping infrastructure">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/SaleFreaks-4.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=d2210679975d1ffac389094e248ad654" alt="Step 2. Select Proxy Type" width="500" height="313" data-path="images/integrations/SaleFreaks-4.png" />
</Frame>

***

### Step 3. Name the Proxy Zone

Choose a clear name for your proxy zone (for example, `salefreaks-ebay-us`).

<Frame caption="Form to choose IP type, showing Dedicated option selected">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/select-ip-type.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=db2ae14cb6a13064b924d5650d8a074d" alt="select-ip-type.png" width="1000" height="333" data-path="images/integrations/select-ip-type.png" />
</Frame>

***

### Step 4. Select IP Count

Specify the number of IPs required.\
Best practice: **one IP per seller account**.

<Frame>
  <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/number-of-ips-1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=ed22621245c0c438c393a0cd69a6a4bd" alt="number-of-ips-1.png" width="1000" height="164" data-path="images/integrations/number-of-ips-1.png" />
</Frame>

***

### Step 5. Country & City Selection

Select the country and city that best match your marketplace region.

<Frame caption="Geolocation targeting options for United States and New York City">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/city-ip.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=2858c27db7a0741e425d6081424a12bc" alt="city-ip.png" width="1000" height="197" data-path="images/integrations/city-ip.png" />
</Frame>

***

### Step 6. Add the Zone

Click **Add** to create and activate the proxy zone.

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/click-add.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=26b354b896ceb869c81fa6abb0f0f362" alt="click-add.png" width="1000" height="288" data-path="images/integrations/click-add.png" />
</Frame>

***

### Step 7. Zone Is Ready

Click on the zone name to view configuration details.\
You can edit settings or add more proxies from the **Configuration** page.

<Frame caption="Proxies and Scraping dashboard with various proxy options listed">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/zone-ready.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=59c246a377932194d96f2c306bc74738" alt="zone-ready.png" width="500" height="313" data-path="images/integrations/zone-ready.png" />
</Frame>

***

### Step 8. Add a New Proxy Password

Navigate to **Access parameters** and click **Add password** to generate a new proxy password.

<Frame caption="Interface showing proxy configuration settings">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/adding-new-pass.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=92201ddd7ef7c1f746871cc5827e1517" alt="adding-new-pass.png" width="500" height="313" data-path="images/integrations/adding-new-pass.png" />
</Frame>

***

### Step 9. Open the Configuration Page

After adding a password, go back to the configuration page to manage IP access.

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxy-config.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=7174f4b8ef22b41a3cd1f7fd963901c1" alt="proxy-config.png" width="500" height="313" data-path="images/integrations/proxy-config.png" />
</Frame>

***

### Step 10. Review Allocated IPs

Click **Show allocated IPs** to view your assigned IP addresses.

<Frame caption="Settings page showing IP allocation details">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/allocated-ips.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=1e0d7054f3fbfac8e1f5c506b3aa21d2" alt="allocated-ips.png" width="500" height="313" data-path="images/integrations/allocated-ips.png" />
</Frame>

***

### Step 11. Download the IP List

Download the allocated IPs list for use in SaleFreaks.

<Frame caption="Interface showing IP allocation options and download link">
  <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/download-ips.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=a8eaf4ce246f98b02e08366a8dd28a07" alt="download-ips.png" width="500" height="313" data-path="images/integrations/download-ips.png" />
</Frame>

<Tip>
  If you added a new password, wait a few minutes before downloading the IP list to allow the password to sync correctly.
</Tip>

***

### Step 12. Open the IP File

Open the downloaded file in a text editor of your choice.

<Frame caption="Text file with proxy IP addresses on screen">
  <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/file-editor.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=60672925a7aef134bd61ff59081937cf" alt="file-editor.png" width="500" height="313" data-path="images/integrations/file-editor.png" />
</Frame>

***

### Step 13. Review Required Proxy Fields

Use the following values when configuring SaleFreaks:

* **Proxy Type**: `HTTP`
* **Proxy IP / Host**: `brd.superproxy.io`
* **Proxy Port**: `44445`
* **Proxy Username**:\
  `lum-customer-{your_customer_id}-zone-{your_zone}-ip-{allocated_ip}`
* **Proxy Password**:\
  Your generated proxy password

<Frame caption="Text file screenshot showing proxy server details">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/requried-fileds.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=f1fb0e7c25212f417b1e06e948798af0" alt="requried-fileds.png" width="500" height="313" data-path="images/integrations/requried-fileds.png" />
</Frame>

***

### Step 14. Log In to SaleFreaks

Log in to your SaleFreaks account.\
When prompted to add a marketplace account, choose **Provide my own proxy**.

<Frame caption="Dialog box for adding an eBay account on SaleFreaks">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/salefreaks-logins.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=28f42d1226ee8cdde079121d078ed467" alt="salefreaks-logins.png" width="500" height="313" data-path="images/integrations/salefreaks-logins.png" />
</Frame>

***

### Step 15. Enter Proxy Details in SaleFreaks

Paste the proxy details from the Bright Data IP file into the SaleFreaks proxy fields.

<Frame caption="Form for adding eBay account with proxy settings">
  <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/fill-in-info.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=a3c7ef0d8ecdefe09a6a38c935295411" alt="fill-in-info.png" width="500" height="313" data-path="images/integrations/fill-in-info.png" />
</Frame>

***

### Step 16. Enable Auto-Recharge (Recommended)

To avoid losing access to allocated IPs, enable **auto-recharge** in your Bright Data billing settings.

<Frame caption="Enable auto recharge confirmation pop-up on billing page">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/autorecharge.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=1dd9ebff44fa5be9531538a5bdae8442" alt="autorecharge.png" width="500" height="284" data-path="images/integrations/autorecharge.png" />
</Frame>

***

<Warning>
  **Important Note**

  If you are using Bright Data **Residential Proxies**, **Web Unlocker API**, or **SERP API**, you must install an SSL certificate to enable secure connections.

  Follow the instructions in this guide to complete the setup:\
  [https://docs.brightdata.com/general/account/ssl-certificate#installation-of-the-ssl-certificate](https://docs.brightdata.com/general/account/ssl-certificate#installation-of-the-ssl-certificate)
</Warning>

***

## Best Practices

* Use **one dedicated IP per seller account**
* Avoid reusing IPs across multiple marketplaces
* Monitor SaleFreaks logs for proxy-related errors
* Use ISP or Datacenter proxies for long-term account safety
* Keep auto-recharge enabled to prevent service interruptions

***

## Conclusion

By integrating Bright Data proxies with SaleFreaks, you create a stable and secure automation environment for dropshipping operations. This setup protects seller accounts, enables geo-specific workflows, and ensures reliable performance across sourcing, fulfillment, and inventory management, allowing you to scale your business with confidence.
