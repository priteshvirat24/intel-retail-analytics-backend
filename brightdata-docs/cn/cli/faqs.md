> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题

> Bright Data CLI 的常见问题和故障排除。

## 常规

<AccordionGroup>
  <Accordion title="`brightdata` 和 `bdata` 之间有什么区别？">
    它们是相同的 - `bdata` 是与 `brightdata` 一起安装的快捷别名。使用你喜欢的任何一个。
  </Accordion>

  <Accordion title="使用 CLI 需要 Bright Data 账户吗？">
    是的。CLI 连接到 Bright Data 的基础设施来处理网络请求。你可以[免费注册](https://www.bright.cn/?hs_signup=1\&utm_source=docs)并开始使用免费套餐。
  </Accordion>

  <Accordion title="我可以从哪些平台提取数据？">
    CLI 通过 `pipelines` 命令支持 40+ 个平台，包括 Amazon、LinkedIn、Instagram、TikTok、YouTube、Facebook、Reddit、Google Maps、Walmart、eBay 等。运行 `brightdata pipelines list` 查看完整列表。
  </Accordion>

  <Accordion title="支持哪些输出格式？">
    * **Scrape:** `markdown`（默认）、`html`、`json`、`screenshot`
    * **Search:** 格式化表格（默认）、`json`、`pretty`
    * **Pipelines:** `json`（默认）、`csv`、`ndjson`、`jsonl`

    所有命令都支持 `-o <path>` 将输出写入文件。
  </Accordion>

  <Accordion title="我可以在脚本和 CI/CD 管道中使用 CLI 吗？">
    可以。CLI 完全支持管道。当 stdout 不是 TTY 时，颜色和加载动画会自动禁用。使用 `--json` 获得机器可读的输出，并使用 `BRIGHTDATA_API_KEY` 环境变量进行非交互式身份验证。
  </Accordion>
</AccordionGroup>

## 身份验证

<AccordionGroup>
  <Accordion title="我的凭据存储在哪里？">
    凭据存储在您的本地计算机上：

    | 操作系统    | 路径                                                              |
    | ------- | --------------------------------------------------------------- |
    | macOS   | `~/Library/Application Support/brightdata-cli/credentials.json` |
    | Linux   | `~/.config/brightdata-cli/credentials.json`                     |
    | Windows | `%APPDATA%\brightdata-cli\credentials.json`                     |

    该文件的权限设置为 `0o600`（仅所有者读/写）。
  </Accordion>

  <Accordion title="如何在没有浏览器的远程服务器上登录？">
    使用设备流：

    ```bash theme={null}
    brightdata login --device
    ```

    这会打印一个 URL 和验证码。在任何有浏览器的设备上打开 URL，输入代码，服务器上的身份验证即可完成。
  </Accordion>

  <Accordion title="如何在 Bright Data 账户之间切换？">
    运行 `brightdata logout`，然后使用���账户运行 `brightdata login`。或直接传递不同的 API 密钥：

    ```bash theme={null}
    brightdata login --api-key <new_key>
    ```
  </Accordion>
</AccordionGroup>

## 故障排除

<AccordionGroup>
  <Accordion title="&#x22;未指定 Web Unlocker 区域&#x22;">
    这意味着没有配置默认区域。通过以下方式修复：

    ```bash theme={null}
    # 重新运行登录（自动创建区域）
    brightdata login

    # 或手动设置区域
    brightdata config set default_zone_unlocker <zone_name>
    ```
  </Accordion>

  <Accordion title="&#x22;API 密钥无效或已过期&#x22;">
    您存储的 API 密钥不再有效。重新进行身份验证：

    ```bash theme={null}
    brightdata login
    ```
  </Accordion>

  <Accordion title="&#x22;访问被拒绝&#x22;">
    您的 API 密钥没有请求的区域或操作的权限。在 [Bright Data 控制面板](https://www.bright.cn/cp)中检查区域权限。
  </Accordion>

  <Accordion title="&#x22;超过速率限制&#x22;">
    您已达到区域的速率限制。选项：

    * 稍等片刻后重试
    * 使用 `--async` 处理大型作业以避免阻塞
    * 联系您的客户经理以提高限额
  </Accordion>

  <Accordion title="Pipeline 作业超时">
    默认轮询超时为 600 秒（10 分钟）。对于大型数据集，请增加它：

    ```bash theme={null}
    # 按命令
    brightdata pipelines amazon_product "<url>" --timeout 1200

    # 通过环境变量
    export BRIGHTDATA_POLLING_TIMEOUT=1200
    ```
  </Accordion>

  <Accordion title="终端中的颜色或加载动画显示异常">
    CLI 自动检测 TTY 支持。如果检测失败，通过 `cat` 进行管道处理以强制纯文本输出：

    ```bash theme={null}
    brightdata scrape https://example.com | cat
    ```

    或使用 `--json` 获得干净、可解析的输出。
  </Accordion>
</AccordionGroup>

## 配置

<AccordionGroup>
  <Accordion title="如何更改默认输出格式？">
    ```bash theme={null}
    brightdata config set default_format json
    ```

    有效值：`markdown`、`json`。
  </Accordion>

  <Accordion title="配置优先级顺序是什么？">
    设置按此顺序解析（优先级从高到低）：

    1. **CLI 标志** - 例如 `--zone my_zone`
    2. **环境变量** - 例如 `BRIGHTDATA_UNLOCKER_ZONE`
    3. **config.json** - 例如 `default_zone_unlocker`
    4. **默认值** - 内置回退值
  </Accordion>

  <Accordion title="如何重置所有配置？">
    删除配置目录：

    ```bash theme={null}
    # Linux
    rm -rf ~/.config/brightdata-cli/

    # macOS
    rm -rf ~/Library/Application\ Support/brightdata-cli/
    ```

    然后运行 `brightdata login` 从头开始。
  </Accordion>
</AccordionGroup>
