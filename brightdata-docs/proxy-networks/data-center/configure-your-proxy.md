> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to configure your Datacenter proxy

> Configure your datacenter proxy settings across 195 countries, select IP types, set geolocation targeting and enable advanced features in this guide.

To access your proxy configuration, open your zone in the "Configuration" tab.

## Which IP type to choose

Bright Data offers 3 types of datacenter proxies:

<Card title="Shared" icon="square-1" horizontal="true">
  A rotating proxy over a pool of \~40,000 proxies, paid by usage GBs.
</Card>

<Card title="Shared unlimited" icon="square-2" horizontal="true">
  A set of specific proxies, shared with others, with unlimited bandwidth, paid by proxy.
</Card>

<Card title="Dedicated unlimited" icon="square-3" horizontal="true">
  A set of specific proxies, exlcusive for you, with unlimited bandwidth, paid by proxy.
</Card>

## Shared (rotating) proxy configuration

### Default countries selection

When selecting countries in shared pool configuration, we will assign proxies only from the countries you select. You can select none (which meand we will assign the next random proxy from the pool), one or more countries. [Read more...](/api-reference/proxy/geolocation-targeting#default-countries-selection)

To select a specific country for your peer during rotation, use the flag -country in the proxy user name parameter with an ISO-3166 country code.

[FAQ: Where can I see the list of country codes?](/general/faqs#where-can-i-see-the-list-of-country-codes)

## Shared & Dedicated unlimited proxy configuration

### Number of IPs

<Tip>
  For unlimited proxies we offer a discount based on amount of proxies you purchase per zone. The more you buy, less your pay per proxy. Click on the "Show rates" link in your zone setup to see rates.
</Tip>

Number of IPs to be allocated as your pool of available IPs.

### How to select a country

Geolocation targeting allows you to target specific `Country`.
Select the preferred countries from the drop-down menu.

Once selected, we will assign proxies from those countries. If we do not have enough proxies to cover your requirement, we will assign the amount we have and you can submit an order for the full amount of proxies (we do not allow single proxy orders - we will take in large orders only).
Changing this selection means re-allocating proxies, which will incur a **Refresh charge** .

### How does multiple countries selection work?

If you select multiple countries, we assign proxies in **available countries** at the moment of assignment. For example: if you choose proxies from Germany, France & Italy, we will provide proxies from **either** of these countries. We will try to distribute the assignment evenly across the countries you selected, yet if there are not enough proxies in one of the countries, some countries will have more proxies than other.

So referring to that example, if you request 30 proxies from Germany, France & Italy and we have only 6 available proxies in Italy you will get: 12 proxies from Germany, 12 from France and 6 from Italy.

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/data-center/geotargeting.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=f849e3eb3e6630cdd9e2c95dfb6ba930" alt="Geolocation Targeting" width="572" height="358" data-path="images/proxy-networks/data-center/geotargeting.png" />
</Frame>

### How to change your country selection

It is possible to change the country you selected for your proxies. Once you change the country, Bright Data will assign new proxies from the selected countries. Since this is a replacement of proxy you will recieve a new IP.

Changing country is similar to IP refresh action and is charged the same.

## Access your allocated Proxies' IP addresses

In all proxy types, you can download, view and copy to clipboard the IPs allocated to you by following these steps:

1. Navigate to the [Zones page](https://brightdata.com/cp/zones).
2. Select a zone with allocated IPs.
3. In the overview tab click 'Download', 'View' or 'Copy'.

<img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/data-center/configure-your-proxy/your-proxy-list.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=31997c6595461a3b94ce0c4f8b873cd4" alt="your-proxy-list" width="1465" height="607" data-path="images/proxy-networks/data-center/configure-your-proxy/your-proxy-list.png" />

***

## How to configure advanced options

### How to enable automatic failover

In case we cannot reach the proxy peer for your request, we will route the request to another available peer. Automatic failover does not apply when you choose default countries: if we cannot find a peer in the country you selected, we will fail the request with error.

Enabling automatic failover assures execution of the request, regardless of the availability of a specific peer.

***

### Special Ports & Protocols

Ports `80` and `443` are available by default, supporting HTTP and HTTPS & SOCKS5 protocols. We also support all ports over `1024` in our Datacenter proxy network. [Read more on ports and protocols...](/proxy-networks/faqs#how-to-see-supported-ports-and-protocols)

<Accordion title="Request Additional ports">
  Bright Data can support additional ports by request. A dedicated and additional compliance process with the Bright Data compliance team will follow every request to support a new port.
  If you would like additional port permissions, you can contact Bright Data Support.
  Examples of ports that require Bright Data compliance review before activation:

  | Port | Protocol |
  | ---- | -------- |
  | `70` | HTTP     |
  | `98` | HTTPS    |
</Accordion>

### Zone usage limit

Set usage limit to your zone: you can limit spending or traffic. This provides additional layer of control to your budget and bandwidth consumption, mostly over our rotating shared pool proxies.
