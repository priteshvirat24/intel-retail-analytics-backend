> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 自动自我修复

> 在 Bright Data Scraper Studio 中配置自动自我修复：当爬虫成功率下降或出现 6 种受支持错误之一时，自动尝试修复爬虫。

使用 **Auto Self Healing**（自动自我修复）标签页，让 Bright Data Scraper Studio 在采集质量下降或出现受支持的爬虫错误时自动尝试修复爬虫。自动自我修复作业不消耗积分。

自动自我修复按爬虫单独配置。启用后，Bright Data Scraper Studio 会监控该爬虫的运行情况，并在满足您设置的触发规则时启动修复作业。

<Note>
  自动自我修复无需您手动发起。如果您想通过自然语言提示词按需修复爬虫，请改用 Scraper Studio IDE 中的[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)。
</Note>

## 如何打开自动自我修复设置？

1. 在 Bright Data Scraper Studio 中打开 **My Scrapers**（我的爬虫）。
2. 选择要配置的爬虫。
3. 打开 **Auto Self Healing**（自动自我修复）标签页。
4. 配置常规设置、触发规则和通知。
5. 点击 **Save**（保存）。

保存后的设置对该爬虫之后的运行生效，已完成的运行不会被重新处理。

## 哪些常规设置控制自动自我修复？

| 设置                                     | 选项     | 作用                                                                                                                                                                                  |
| -------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable Auto Self Healing**（启用自动自我修复） | On、Off | 为该爬虫开启或关闭自动自我修复。设为 On 时，Bright Data Scraper Studio 会在满足触发规则后启动修复作业。                                                                                                                 |
| **Auto save code**（自动保存代码）             | On、Off | 控制 Bright Data Scraper Studio 是否保存修复过程生成的代码。设为 On 时，任何成功的修复作业都会将新提取的代码保存到生产环境，并更新采集器的模板版本。设为 Off 时，修复作业仍会运行，但不会保存生成的代码，系统会向您在 **Notifications**（通知）中选择的用户发送邮件，由他们审核建议的修复方案后再决定是否保存。 |

<Warning>
  **Auto save code**（自动保存代码）会直接写入生产环境。成功的修复作业会保存新代码并提升采集器的模板版本，全程没有人工审核，因此下一次运行将使用 AI 生成的代码进行采集。只有在您接受这一点时才开启该选项。保持 Off 可以在任何修复进入生产环境之前保留一道审核环节。
</Warning>

## 哪些触发规则会启动修复作业？

触发规则决定自动自我修复何时为您正在配置的爬虫启动。**Success Rate Threshold** 和 **Minimum Inputs Threshold** 为必填字段。

| 触发规则                                           | 默认值     | 作用                                                                         |
| ---------------------------------------------- | ------- | -------------------------------------------------------------------------- |
| **Success Rate Threshold (%)**（成功率阈值）          | `40`    | 低于该成功率时触发自动自我修复。设为 `40` 时，一旦爬虫成功率低于 40%，即可启动修复作业。                          |
| **Trigger Frequency**（触发频率）                    | Per Day | Bright Data Scraper Studio 是每天检查一次（**Per Day**），还是在每次作业运行时检查（**Per Job**）。 |
| **Minimum Inputs Threshold**（最小输入数阈值）          | `10`    | 触发自动自我修复所需的最小作业输入数量。输入数少于该值的运行不会启动修复作业，因此小规模运行中的少量失败不会被视为质量下降。             |
| **Cooldown Period (hours)**（冷却时间，小时）           | `3`     | 该爬虫连续两次触发自动自我修复之间必须等待的最少小时数。                                               |
| **Max Auto-Healing Jobs Per Day**（每日最大自动修复作业数） | `8`     | 该爬虫一天内允许运行的自动自我修复作业上限。                                                     |

失败的修复作业同样计入 **Max Auto-Healing Jobs Per Day**，也同样会启动 **Cooldown Period**。

## 哪些错误代码会触发自动自我修复？

自动自我修复仅对以下 6 种爬虫错误代码启动：

* `crawl_error`
* `parse_error`
* `bad_cmd_arg`
* `dead_page`
* `bad_input`
* `bad_navigate`

爬虫如果因其他错误代码失败，即使满足全部触发规则也不会启动自动自我修复。每个代码的含义及手动排查方法，请参见 [Scraper Studio 错误代码](/cn/datasets/scraper-studio/error-codes)。

## 在哪里查看状态和通知？

**Auto Self Healing**（自动自我修复）标签页中的 **Status**（状态）区域会显示该爬虫的修复作业活动。在任何修复作业运行之前，显示为 `No auto healing jobs were triggered`。

**Notifications**（通知）区域提供 **Select users to notify**（选择要通知的用户）下拉框，列出您账户下的用户。被选中的用户会在自动自我修复触发时、完成时以及需要处理时收到邮件。当 **Auto save code** 设为 Off 时，请至少选择一位用户，因为审核邮件是建议修复方案送达相关人员的唯一途径。

## 常见问题

### 自动自我修复与自我修复工具有什么区别？

自动自我修复依据您为每个爬虫配置的触发规则自动运行。[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)是手动的：您在 Scraper Studio IDE 中打开爬虫，用自然语言描述修复需求，并在接受前审核代码差异。自动自我修复不需要提示词。

### 自动自我修复会在未经询问的情况下修改我的爬虫吗？

只有在 **Auto save code** 设为 On 时才会。当 **Auto save code** 设为 Off 时，Bright Data Scraper Studio 仍会运行修复作业，但不会保存生成的代码，而是向 **Notifications** 中选择的用户发送邮件，请他们先审核建议的修复方案。

### 爬虫失败后，自动自我修复为什么没有启动？

请先检查失败的错误代码。自动自我修复仅对本页列出的 6 种错误代码启动，因此以其他代码失败的爬虫永远不会触发它。如果错误代码在支持范围内，请检查该爬虫的其他触发规则：本次运行的输入数可能低于 **Minimum Inputs Threshold**，或者该爬虫仍处于 **Cooldown Period** 内，又或者已达到 **Max Auto-Healing Jobs Per Day** 上限。失败的修复作业同样计入这两项限制。

### 可以通过 API 配置自动自我修复吗？

暂时不可以。自动自我修复的规则只能在控制面板中设置。[AI Flow API](/cn/api-reference/scraper-studio-api/ai-flow/overview) 可以通过 [触发自我修复](/cn/api-reference/scraper-studio-api/ai-flow/trigger-self-healing) 按需启动修复作业，但不提供本页所列触发规则的配置接口。

### 这些设置会影响已经完成的运行吗？

不会。自动自我修复的设置仅对该爬虫之后的运行生效，已完成的运行不会被修改或重新处理。

## 相关内容

<CardGroup cols={2}>
  <Card title="自我修复工具" icon="wand-magic-sparkles" href="/cn/datasets/scraper-studio/self-healing-tool">
    通过自然语言提示词按需修复爬虫
  </Card>

  <Card title="Scraper Studio 错误代码" icon="triangle-exclamation" href="/cn/datasets/scraper-studio/error-codes">
    每个爬虫错误代码的含义及排查方法
  </Card>

  <Card title="触发自我修复 API" icon="code" href="/cn/api-reference/scraper-studio-api/ai-flow/trigger-self-healing">
    通过 AI Flow API 启动自我修复作业
  </Card>

  <Card title="启动数据收集与交付" icon="paper-plane" href="/cn/datasets/scraper-studio/initiate-collection-and-delivery-options">
    运行生产环境爬虫并配置交付方式
  </Card>
</CardGroup>
