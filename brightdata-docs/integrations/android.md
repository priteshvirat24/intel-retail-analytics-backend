> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Bright Data on Android

> Configure Bright Data proxies on Android for both mobile data (APN) and Wi-Fi networks. Bright Data proxies span 195 countries.

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

Setting up Bright Data on Android allows you to route your device traffic through secure proxy connections. You can configure Bright Data for **mobile data (APN)** or **Wi-Fi networks**, depending on your use case. Follow the instructions below based on your preferred network type.

***

## Prerequisites

Before you begin, ensure you have:

* An active **Bright Data account**
* Your Bright Data **proxy credentials** (host, port, username, password)
* An Android device with permission to edit network settings

***

## Configuring a Proxy for a Mobile Network (APN)

### Step 1. Access Network Settings

Open **Settings**, then navigate to **Network & Internet** (or **Connections**, depending on your device).

### Step 2. Locate APN Settings

Tap **Mobile Networks**, then select **Access Point Names (APNs)**.

<Frame as="div" style={{ width: "50%", height: "auto" }}>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/android3.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=03b7382fec084060727bf61e3dcd2e0e" alt="Step 2. Locate APN Settings" width="300" height="525" data-path="images/integrations/android3.png" />

  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/android4.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=a5e5c9f07ef71bcdeaf346479d458953" alt="Step 2. Locate APN Settings" width="300" height="349" data-path="images/integrations/android4.png" />
</Frame>

### Step 3. Edit APN Details

Select your active APN and update the following fields:

<Frame as="div" style={{ width: "50%", height: "auto" }}>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/android5.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=4856af0c56eedf28810e82c5b6549a00" alt="Step 3. Edit APN Details" width="300" height="156" data-path="images/integrations/android5.png" />
</Frame>

* **Proxy**: `brd.superproxy.io`
* **Port**: `44445`
* **Username**: Your Bright Data proxy username
* **Password**: Your Bright Data proxy password

<Frame as="div" style={{ width: "50%", height: "auto" }}>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/android6.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ad354718e25cf741ef81c9afd2516f6f" alt="Step 3. Edit APN Details" width="300" height="398" data-path="images/integrations/android6.png" />
</Frame>

### Step 4. Save and Reconnect

Save the APN settings and toggle **Mobile Data** off and back on to apply the changes.

***

## Configuring a Proxy for a Wi-Fi Network

### Step 1. Access Wi-Fi Settings

Open **Settings** → **Network & Internet (or Connections)** → **Wi-Fi**.

<Frame as="div" style={{ width: "50%", height: "auto" }}>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/android1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ed6ff1b2944f28968813081ee5df151c" alt="Step 1. Access Wi-Fi Settings" width="300" height="534" data-path="images/integrations/android1.png" />
</Frame>

### Step 2. Select Your Connected Network

Tap your connected Wi-Fi network and choose **Settings** or **Edit**.

<Frame as="div" style={{ width: "50%", height: "auto" }}>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/android2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=4e77bf2d82e5f74fae9c47f464e49850" alt="Step 2. Select Your Connected Network" width="300" height="210" data-path="images/integrations/android2.png" />
</Frame>

### Step 3. Enable Manual Proxy Configuration

Scroll to **Advanced options** and set **Proxy** to **Manual**.

### Step 4. Enter Proxy Details

Provide the following information:

* **Host**: `brd.superproxy.io`
* **Port**: `44445`

Tap **Save** to apply the configuration.

***

## Verify the Proxy Connection

After setup, open a browser on your device and visit:

[http://brdtest.com/myip.json](http://brdtest.com/myip.json)

Confirm that the displayed IP and location match your Bright Data proxy settings.

***

## Best Practices

* Use **ISP or Datacenter proxies** for better stability on mobile devices
* Avoid frequently switching networks when running proxy-dependent tasks
* Keep your Bright Data credentials secure
* Re-verify proxy settings after OS updates

***

## Conclusion

You’ve successfully configured **Bright Data on Android**. Your device traffic is now routed through secure, private proxy connections, ideal for privacy, geo-restricted access, and protected browsing. Enjoy a safer and more flexible mobile experience.
