> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 NGINX 中设置 Bright Data

> 将 Bright Data 与 NGINX 集成，可高效地路由流量、隐藏域名，并安全地管理连接。按照本指南配置 NGINX 以使用 Bright Data 代理，提升性能和灵活性。

<Accordion title="展开以获取您的 Bright Data 代理访问信息">
  ### 您的代理访问信息

  Bright Data 代理按“代理区域”（Proxy zones）进行分组。每个区域包含其对应的代理配置。&#x20;

  要获取代理区域的访问权限：&#x20;

  1. 登录 Bright Data 控制面板
  2. 选择现有代理区域或新建一个代理区域
  3. 点击新的区域名称，并选择 **概览（Overview）** 选项卡
  4. 在概览选项卡中，找到 **访问详情（Access details）**，并单击复制图标将代理访问信息复制到剪贴板&#x20;
  5. 您需要以下信息：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）
  6. 点击复制图标，将文本复制到剪贴板，并粘贴到您的工具的代理配置中&#x20;

  ### 访问详情示例

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### 住宅代理访问

  要使用 Bright Data 的 **住宅代理（Residential Proxies）**，您必须是经过 KYC 验证的企业账户。请与 Bright Data 合规团队完成 KYC 验证；不存在自动或无需 KYC 的访问方式。尚未完成 KYC 时，请使用 ISP 或数据中心代理。[了解更多...](/proxy-networks/residential/network-access)

  ### 目标是搜索引擎？

  如果您的目标是 Google、Bing 或 Yandex 等搜索引擎，则需要使用专门的搜索引擎结果页（**SERP**）代理 API。请使用 Bright Data SERP API 来访问搜索引擎。\
  [点击此处了解 Bright Data SERP 代理 API。](/scraping-automation/serp-api/introduction)

  ### 避免工具中的 `PROXY ERROR`

  一些工具会使用搜索引擎作为代理测试目标：如果您的代理测试失败，这可能就是原因。请确保您的测试目标域名不是搜索引擎（此设置在工具配置中，而非 Bright Data 代理的控制范围内）。
</Accordion>

## 什么是 NGINX？

**NGINX** 是一个高性能的 Web 服务器和反向代理，常用于负载均衡、缓存和安全连接管理。通过将 NGINX 与 **Bright Data** 集成，您可以隐藏代理域名、无缝路由流量，并优化基础设施以提高性能。

## 如何在 NGINX 中设置 Bright Data

<Steps>
  <Step title="安装 NGINX">
    1. 根据 [官方安装指南](https://nginx.org/en/download.html) 在您的服务器上安装 **NGINX**。
    2. 确保您的版本为 **1.15.10 或更高**。
    3. 确保您的服务器 IP **未** 被添加到 Bright Data 代理白名单，以避免冲突。
  </Step>

  <Step title="配置 NGINX 核心设置">
    1. 打开主 NGINX 配置文件：

    ```bash theme={null}
    sudo nano /etc/nginx/nginx.conf
    ```

    2. 更新以下参数：
       * **将 `worker_processes`** 设为 `auto`，以实现动态优化。
       * **将 `worker_connections`** 设为 `200`（或更多，具体取决于所需的端口数量）。

    3. 在 `http` 部分的末尾添加：

    ```nginx theme={null}
    include /etc/nginx/sites-enabled/*;
    ```

    4. 保存更改并退出编辑器。
    5. 更新后的 `nginx.conf` 应如下所示：

    ```nginx theme={null}
    worker_processes  auto;
    user              www-data;

    error_log         /var/log/nginx/error.log info;
    events {
        worker_connections 200;
    }

    http {
        include         /etc/nginx/mime.types;
        access_log      /var/log/nginx/access.log combined;

        server {
            server_name   localhost;
            listen        127.0.0.1:80;
            error_page    500 502 503 504  /50x.html;
        }

        include /etc/nginx/sites-enabled/*;
    }
    ```
  </Step>

  <Step title="创建代理配置文件">
    1. 创建自定义配置目录：

    ```bash theme={null}
    sudo mkdir -p /etc/nginx/sites-enabled
    ```

    2. 创建新配置文件：

    ```bash theme={null}
    sudo nano /etc/nginx/sites-enabled/brightdata.conf
    ```

    3. 添加以下配置，根据需要调整端口范围：

    ```nginx theme={null}
    server {
        listen 24000-24100;
        location / {
            resolver 8.8.8.8;
            proxy_pass http://127.0.0.1:$server_port;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
    ```

    4. 保存并关闭文件。
  </Step>

  <Step title="重启 NGINX">
    1. 通过以下命令应用更改并重启 NGINX：

    ```bash theme={null}
    sudo service nginx restart
    ```
  </Step>

  <Step title="测试代理配置">
    1. 运行以下命令验证代理连接，将 `10.0.2.15` 替换为您的服务器 IP：

    ```bash theme={null}
    curl --proxy http://10.0.2.15:24000 "http://brdtest.com/myip.json" -v
    ```

    2. 确保响应包含预期的代理 IP 和位置信息。

       **预期输出：**

       ```json theme={null}
       {
         "ip": "43.252.31.41",
         "country": "US",
         "asn": {
           "asnum": 207990,
           "org_name": "HostRoyale Technologies Pvt Ltd"
         },
         "geo": {
           "city": "Chicago",
           "region": "IL",
           "region_name": "Illinois",
           "postal_code": "60602",
           "latitude": 41.8874,
           "longitude": -87.6318,
           "tz": "America/Chicago",
           "lum_city": "chicago",
           "lum_region": "il"
         }
       }
       ```
  </Step>

  <Step title="监控 NGINX 流量">
    1. 确保流量通过 NGINX 路由，监控代理管理日志。
    2. 确保 "sent from" IP 与您的 NGINX 服务器 IP 匹配。
  </Step>
</Steps>

您的 **Bright Data** 现已成功集成到 **NGINX**，提供安全、高效的流量路由和域名隐藏功能。此设置非常适合优化网页抓取、负载均衡和安全代理管理。享受更顺畅的操作体验吧！
