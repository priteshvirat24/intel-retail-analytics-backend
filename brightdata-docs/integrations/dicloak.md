> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Bright Data with DICloak

> Set up Bright Data proxies in DICloak anti-detect browser for anonymous browsing with dynamic fingerprinting and profile management. Covers 195+ countries.

<Warning>
  **Account management is not a supported use case** on the Bright Data platform as of April 1, 2026. This includes managing accounts on platforms like TikTok, Instagram, or similar services. Bright Data proxies cannot be used for this purpose. See [Acceptable Use Policy](https://brightdata.com/acceptable-use-policy) for details.
</Warning>

## DICloak Proxy Integration

DICloak is a powerful anti-detect browser designed to provide secure and anonymous internet browsing. It offers dynamic fingerprinting, profile management, and robust proxy support, making it an essential tool for professionals seeking enhanced privacy and data collection capabilities.

## DICloak and Bright Data: A Powerful Integration for Secure Browsing

Integrating DICloak with Bright Data’s proxy solutions creates a robust combination for privacy-focused professionals. Here’s how Bright Data enhances DICloak:

* **Global Proxy Coverage:** Access 400M+ monthly residential IPs across 195+ countries for region-specific browsing, the largest proxy network in the world.
* **Enhanced Privacy:** Secure and anonymous browsing with reliable proxy support.
* **Geo-Bypassing:** Easily access restricted content for international projects.
* **Optimized Speed:** High-performance proxies ensure fast connections.
* **Versatile Applications:** Suitable for web scraping, data collection, and more.

Integrating DICloak with Bright Data's proxy services ensures optimal performance and security for your web scraping and browsing tasks. This article provides a step-by-step guide to integrate Bright Data with DICloak seamlessly.

## How to Integrate Bright Data With DICloak

<Steps>
  <Step title="Download and Install DICloak">
    1. [Download](https://dicloak.com/download) the DICloak browser suitable for your operating system.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/download-dicloak.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=baf6e727718f805300324a359daea103" alt="download-dicloak" width="1880" height="863" data-path="images/integrations/dicloak/download-dicloak.png" />
    </Frame>

    2. Install DICloak and launch the app.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/launch-dicloak.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=e0abebf8db26a6d0a8316912e6ba28ea" alt="launch-dicloak" width="1999" height="1250" data-path="images/integrations/dicloak/launch-dicloak.png" />
    </Frame>
  </Step>

  <Step title="Create a New Profile">
    1. Click on the **+ Create Profile** button.

    <Frame>
      <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/dicloak/create-profile.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ae7dc5314f8acad0aae5ac418655128b" alt="create-profile" width="1785" height="903" data-path="images/integrations/dicloak/create-profile.png" />
    </Frame>

    2. Set up the basic profile:

    * Enter a **Profile Name**.
    * Choose the browser and operating system.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/setup-basic-profile.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=b55efb8f4e07aa9797a97d6ed6c561d6" alt="setup-basic-profile" width="1999" height="1250" data-path="images/integrations/dicloak/setup-basic-profile.png" />
    </Frame>
  </Step>

  <Step title="Proxy Configuration in DICloak">
    1. Scroll down to the **Proxy** section and set proxy details:

    * From the **Proxy Type** dropdown, select `HTTP`.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/proxy-config.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=90d8b5ec4b7150a1c7d9837d0f043d62" alt="proxy-config" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-config.png" />
    </Frame>

    2. Enter the following details:

       * **Host:** `brd.superproxy.io`
       * **Port:** `44445`
       * **Account Name:** Enter your Bright Data username.
       * **Password:** Enter your Bright Data password.

           <Tip>
             Learn how to find your Bright Data username and password in [this guide](/integrations/bright-data).
           </Tip>

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/proxy-connection.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=5ae68ffa62fc767ba546f0cb74011cd0" alt="proxy-connection" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-connection.png" />
    </Frame>
  </Step>

  <Step title="Test your Proxy">
    1. Click on the **Check Proxy** button to test the connection.

    <Frame>
      <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/dicloak/check-proxy.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=b68cc53091b50de0fafde36fc03667f2" alt="check-proxy" width="1999" height="1250" data-path="images/integrations/dicloak/check-proxy.png" />
    </Frame>

    2. Ensure the connection test is successful and confirm the settings.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/proxy-test-success.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=8523da5097a09339ebe614a47c89090c" alt="proxy-test-success" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-test-success.png" />
    </Frame>
  </Step>

  <Step title="Start Browsing">
    1. To use the proxy, click on the **Open** button.

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/open-browser.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=68502c89c8c3107f5527f0151c913eb0" alt="open-browser" width="1999" height="1250" data-path="images/integrations/dicloak/open-browser.png" />
    </Frame>

    2. A browser will open with your preferred settings and the configured proxy.

    <Frame>
      <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/dicloak/browser-open.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=b4c844ccf0802123c437d654e529964f" alt="browser-open" width="1999" height="1250" data-path="images/integrations/dicloak/browser-open.png" />
    </Frame>
  </Step>
</Steps>

***

## What else to keep in mind

* **Session Control:** Bright Data allows session customization. Configure session persistence to maintain the same IP or rotate IPs as needed for your tasks.
* **Proxy Pooling:** Utilize Bright Data’s proxy pool for larger data collection projects.
* **DICloak Enhancements:** Leverage DICloak’s unique anti-detect features to mimic human-like browsing behavior.

By following this guide, you can effectively integrate Bright Data with DICloak for secure, efficient, and anonymous browsing and data collection.
