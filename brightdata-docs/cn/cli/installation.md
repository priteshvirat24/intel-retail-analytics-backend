> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 安装和设置

> 在一分钟内安装 Bright Data CLI 并对您的帐户进行身份验证。

## 安装 CLI

运行 Bright Data CLI 最快的方式是使用 `npx`，它会执行最新版本，无需全局安装：

```bash theme={null}
npx -p @brightdata/cli brightdata --version
```

在本文档的任意命令前加上 `npx -p @brightdata/cli` 即可以同样的方式运行，无需维护任何全局依赖。Bright Data CLI 需要 Node.js 20 或更高版本。

如果希望获得持久可用的 `brightdata` 命令和更快的启动速度，请改为全局安装 CLI：

<CodeGroup>
  ```bash npm (recommended) theme={null}
  npm install -g @brightdata/cli
  ```

  ```bash yarn theme={null}
  yarn global add @brightdata/cli
  ```

  ```bash pnpm theme={null}
  pnpm add -g @brightdata/cli
  ```
</CodeGroup>

验证全局安装：

```bash theme={null}
brightdata --version
```

<Tip>
  快捷别名 `bdata` 同样可用，既可通过 `npx -p @brightdata/cli bdata` 使用，也可在全局安装后使用 - 使用您喜欢的任何一个。
</Tip>

## 更新 CLI

使用与安装时相同的包管理器升级到最新版本：

<CodeGroup>
  ```bash npm theme={null}
  npm install -g @brightdata/cli@latest
  ```

  ```bash yarn theme={null}
  yarn global add @brightdata/cli@latest
  ```

  ```bash pnpm theme={null}
  pnpm add -g @brightdata/cli@latest
  ```
</CodeGroup>

将已安装版本与 npm 上发布的最新版本进行对比：

```bash theme={null}
brightdata --version               # 您已安装的版本
npm view @brightdata/cli version   # npm 上的最新版本
```

<Tip>
  新命令会随 CLI 版本发布。例如，`scraper heal` 和 `scraper approve` 在 v0.3.1 中加入。运行上面的更新命令即可获取它们。各版本的变更详情参见[发布说明](https://github.com/brightdata/cli/releases)。
</Tip>

## 身份验证

运行登录命令以连接您的 Bright Data 帐户：

```bash theme={null}
brightdata login
```

这将打开您的浏览器进行安全的 OAuth 身份验证。完成后，CLI 将：

1. 验证并在本地存储您的 API 密钥
2. 自动创建所需的代理区域（`cli_unlocker`、`cli_browser`）
3. 设置合理的默认值，以便您立即开始

<Check>
  您只需登录**一次**。所有后续命令都会自动进行身份验证。
</Check>

### 替代身份验证方法

<AccordionGroup>
  <Accordion title="无头/SSH 环境" icon="server">
    当没有可用的浏览器时，使用设备流：

    ```bash theme={null}
    brightdata login --device
    ```

    这会打印一个 URL 和一个代码。在任何设备上打开该 URL，输入代码，CLI 即可完成身份验证。
  </Accordion>

  <Accordion title="直接 API 密钥" icon="key">
    对于 CI/CD 管道或非交互式环境，直接传递您的 API 密钥：

    ```bash theme={null}
    brightdata login --api-key YOUR_API_KEY
    ```

    您可以在 [Bright Data 控制面板](https://www.bright.cn/cp/setting) 中找到您的 API 密钥。
  </Accordion>

  <Accordion title="环境变量" icon="leaf">
    设置 `BRIGHTDATA_API_KEY` 环境变量以完全跳过登录：

    ```bash theme={null}
    export BRIGHTDATA_API_KEY=YOUR_API_KEY
    ```

    这对 Docker 容器、GitHub Actions 和其他自动化环境很有用。
  </Accordion>
</AccordionGroup>

## 交互式设置向导

为了获得引导式的首次体验，请使用 init 命令：

```bash theme={null}
brightdata init
```

这将逐步引导您完成身份验证、区域选择和默认配置。

| 标志                    | 描述              |
| --------------------- | --------------- |
| `--skip-auth`         | 跳过身份验证步骤（如果已登录） |
| `-k, --api-key <key>` | 直接提供 API 密钥     |

## 验证您的设置

登录后，确认一切正常工作：

```bash theme={null}
# 检查您的配置
brightdata config

# 验证 API 连接
brightdata budget

# 尝试快��抓取
brightdata scrape https://example.com
```

## 配置存储

CLI 在本地存储凭证和配置：

| 操作系统    | 路径                                              |
| ------- | ----------------------------------------------- |
| macOS   | `~/Library/Application Support/brightdata-cli/` |
| Linux   | `~/.config/brightdata-cli/`                     |
| Windows | `%APPDATA%\brightdata-cli\`                     |

创建两个文件：

| 文件                 | 用途           | 权限             |
| ------------------ | ------------ | -------------- |
| `credentials.json` | API 密钥       | `0o600`（仅限所有者） |
| `config.json`      | 区域、输出格式、偏好设置 | 标准             |

<Tip>
  **配置的优先级顺序：** CLI 标志 → 环境变量 → `config.json` → 默认值。您始终可以逐个命令覆盖任何设置。
</Tip>

## 后续步骤

<CardGroup>
  <Card title="命令" icon="code" horizontal href="/cli/commands">
    探索完整的命令参考。
  </Card>

  <Card title="使用示例" icon="book-open" horizontal href="/cli/examples">
    跳转到真实工作流和配方。
  </Card>
</CardGroup>
