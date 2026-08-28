> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 数据范围如何影响交付时间

> 了解所选数据范围如何影响 Bright Data Web Archive 的交付时间：24 小时内立即处理，更早的数据需从 S3 Glacier 检索，最长 72 小时。

如果您的查询匹配的数据在**过去 24 小时内** - 您的快照将立即开始处理/交付。

如果您匹配的某些数据**早于 24 小时** - 需要从 **S3 Glacier Deep Archive** 存储层检索，然后才能交付，这可能需要**长达 72 小时**。

<Warning>
  避免跨越保留期边界的查询（从现在起大约 24 小时）。

  具有 `max_age` 或时间范围在当前时间的 \~24h ± 2h 内的请求可能包括已迁移到存档存储层的文件。尝试对此类查询进行转储可能会导致转储停滞或因文件存储类过渡而保持不完整。
</Warning>

<Tip>
  **建议：**

  * 我们建议初始测试时使用 `max_age` = `24h` 以确保快速交付。
  * 对于实时数据需求：使用 `max_age: "24h"` 或更窄的时间窗口以避免保留边界。
  * 对于历史数据（早于 24 小时）：使用显式的 `min_date`/`max_date` 过滤器而不是 `max_age`。
  * 如果转储显示停滞：我们通常会自动重试，如果没有发生，请提交工单。
</Tip>
