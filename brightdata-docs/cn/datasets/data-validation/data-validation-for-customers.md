> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 面向客户的数据验证

## 概述

Bright Data 的自动化数据集创建平台在数据集交付之前包含验证和审批阶段。该平台提供错误处理、验证检查和自定义功能，确保数据的准确性和可靠性。这些验证检查对于节省时间、减少数据错误以及保持数据质量至关重要。

<Frame caption="数据集验证流程：Snapshot Triggered（快照触发）→ Did it Pass Validation Tests?（是否通过验证测试）→ 通过则进入 Dataset is delivered（交付数据集）；未通过则 Fix and send to user（修复后发送给用户审批），若用户拒绝则按 Handling by SLA（按 SLA 处理）后再返回修复。">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-customers/flow-chart.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=fbd27f4a8c509b3eeb604e9726834d83" alt="数据集验证流程图，展示从快照触发到交付的完整步骤（图中文字为英文）" width="1115" height="291" data-path="images/datasets/data-validation/data-validation-for-customers/flow-chart.png" />
</Frame>

## 工作原理

一旦数据集快照准备就绪：

<Tabs>
  <Tab title="✅ 如果所有验证测试均通过">
    用户将获得数据集，并在平台中看到所有测试均已通过的提示。
  </Tab>

  <Tab title="❌ 如果全部/部分验证测试失败">
    开发人员会检查问题，并决定是否：

    1. 根据失败的测试修复数据集。
    2. 仍然将数据集交付给用户，并解释为何验证测试失败但被覆盖。

    随后用户可以选择：

    1. 通过该快照。
    2. 仅通过此次时间范围的快照。
    3. 拒绝该快照，我们将相应修复爬虫。
  </Tab>
</Tabs>

当用户批准数据集快照后，他们将进入交付阶段。

## 验证规则

<AccordionGroup>
  <Accordion title="唯一性">
    数据集必须包含一定比例的唯一值。

    * 示例：在 LinkedIn 公司资料数据集中，每家公司的 LinkedIn URL 应为唯一。如果存在重复 URL，则表示同一公司被列出不止一次，违反了唯一性规则。
  </Accordion>

  <Accordion title="填充率">
    数据集必须包含至少最低比例的已填充值。

    * 示例：在 LinkedIn 公司资料数据集中，至少 90% 的资料必须填写“行业”字段。如果超过 10% 的资料缺少该信息（字段为空），数据集将不符合所需的填充率。
  </Accordion>

  <Accordion title="必填字段">
    某些字段必须填写；如果保持为空，将会触发错误。

    * 示例：在 LinkedIn 数据集中，“公司名称”和“总部位置”等字段可能是必填项。缺少这些信息的资料将被标记为错误。
  </Accordion>

  <Accordion title="数据稳定性">
    与之前采集的值相比，数值变化不得超过 X。

    * 示例：若数据集定期更新，公司员工人数不应在两次更新之间出现巨大变化（例如突然从 50 跳到 5000），除非有已知原因（如并购）。
  </Accordion>

  <Accordion title="类型验证">
    验证每条数据的值类型是否与字段类型（如字符串、数字、日期）一致，并标记不一致项以供修正。

    * 示例：数据集应在“成立日期”字段中仅接受日期格式。如果录入了如“unknown”这样的文本，应被标记为错误。
  </Accordion>

  <Accordion title="架构和字段自定义验证">
    创建自定义规则验证某字段是否存在且其值是否有效，例如要求 size 字段只能为“S”、“M”或“L”。

    * 示例：数据集中可能有“公司规模”字段，接受的值包括“小”、“中”、“大”。若记录中出现了其他值，应被标记为错误。
  </Accordion>

  <Accordion title="最小记录数量阈值">
    数据集必须包含 X 条记录（每个 URL 应在总输入 URL 中返回 X 条记录）。

    * 示例：若数据集旨在代表某一领域（如科技行业）的公司，则必须包含该领域的最小公司数量，才能视为完整且具有代表性。
  </Accordion>

  <Accordion title="数据规模波动阈值">
    确定数据集规模波动是否处于 ±X% 范围内。

    * 示例：对于每月更新的数据集，公司总数不应出现剧烈波动（例如超过 10% 的增减），除非行业内出现特定事件或趋势。
  </Accordion>

  <Accordion title="记录完整性验证">
    检查数据集中每条记录，确保其空字段或 null 字段不超过一定比例（如 70%）。若超过该阈值，则触发错误。

    * 示例：在 LinkedIn 公司资料数据集中，如果某公司超过 70% 的字段（如行业、规模、位置、描述）为空，则该记录将被标记为不完整。
  </Accordion>

  <Accordion title="唯一标识与重复记录验证">
    检测并解决因标识错误或录入失误导致的重复记录问题，确保每条记录唯一且准确代表独立的数据点。

    * 示例：在 LinkedIn 数据集中，该规则会识别由于唯一标识分配错误导致同一公司被列出多次的情况。例如公司名称拼写略有差异导致被当作不同公司，该规则将标记这些记录以供修正。
  </Accordion>
</AccordionGroup>

## 主要组件与功能

<Frame caption="数据集测试的整体视图：在 All results（全部结果）/ Passed（通过）/ Failed（失败）标签页之间切换。每条 Test（测试）显示 Test result（测试结果）、Expected value（期望值）和 Review status（审批状态，例如 Ready for deliver 表示可交付）。">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-customers/overall-view.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=8fa2715b8a99096f8aec25bd2dc71ae0" alt="数据集测试的整体视图：Snapshot 区列出 Min number of records、Crawler errors、PII blacklisted 等结果；Failed records 区按字段列出每条规则的结果（图中文字为英文）" width="1210" height="790" data-path="images/datasets/data-validation/data-validation-for-customers/overall-view.png" />
</Frame>

### 评估验证测试结果

<Frame caption="Validation results（验证结果）页面：包含 Request details / Validation rules / Validation results 三个标签页。每条失败的测试可点击右侧的 Evaluate（评估）链接进行处理。">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-customers/evaluate.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=7ed83bdf7e5ff3f61ddf1d005c83efbb" alt="数据集 Amazon best products 的验证结果页面，红色箭头指向每行右侧的 Evaluate 操作链接（图中文字为英文）" width="1350" height="1004" data-path="images/datasets/data-validation/data-validation-for-customers/evaluate.png" />
</Frame>

一旦数据集快照的验证错误被处理，用户将收到通知并可选择：

1. 通过
2. 临时通过
3. 拒绝快照

### 评估操作

对于每个失败的验证测试，用户有三种选择：

1. **设置新阈值**
   1. 设置自定义值 – 如果开发者未达到默认阈值，用户可以设定新阈值。设置后快照将返回给开发者处理。
   2. 按 X% 设置 – 接受开发者达到的成功率，并将阈值设为开发者提取的值。

2. **忽略测试（仅一次）** – 接受开发者此次提取的值（默认值在下次快照中不会改变）。

3. **拒绝** – 用户不接受对失败测试的调整；问题将返回给开发者修复。状态将标记为“已拒绝”，之后会再次发送给客户审批。

<Frame caption="Evaluate options（评估选项）对话框：显示 Failed value（失败值）与 Current threshold（当前阈值），并提供三种处理方式 — Set new threshold（设置新阈值，可输入自定义值或按当前实际比例）、Ignore test this time（仅本次忽略测试）、Reject ignoring（拒绝忽略并发回开发者）。">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-customers/evaluate-options.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=a53a16bd9790d81bf42bc4587a07c960" alt="Evaluate options 对话框，列出三种处理失败测试的选项（图中文字为英文）" width="500" data-path="images/datasets/data-validation/data-validation-for-customers/evaluate-options.png" />
</Frame>

如果所有问题都被忽略/批准，点击“交付数据集”以交付快照。

<Note>如果客户审批处于待处理状态超过 14 天，将自动交付快照。</Note>

<Frame caption="所有问题处理完毕后，Validation results 页面右上角会出现蓝色的 Deliver dataset（交付数据集）按钮，点击即可将快照交付给客户。">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-customers/validations-results.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=d75a4b1ae9a388a2166bbd3e10d5516f" alt="Validation results 页面，所有失败项的 Review status 均为 Ignored & delivered，右上角显示 Deliver dataset 按钮（图中文字为英文）" width="1600" height="565" data-path="images/datasets/data-validation/data-validation-for-customers/validations-results.png" />
</Frame>

如果所有/部分问题被拒绝，点击“发送给开发者”以返回进行进一步修复。

<Frame caption="若存在被拒绝或未处理的失败项，Validation results 页面右上角会显示蓝色的 Send back to developer（发送给开发者）按钮，点击会将快照退回给开发者修复。">
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/data-validation/data-validation-for-customers/failed-results.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=932edc2ee86a00a82ec7cb7e2ab89ca0" alt="Validation results 页面，Snapshot 区与 Fields 区列出多条 Failed 测试，右上角显示 Send back to developer 按钮（图中文字为英文）" width="1360" height="978" data-path="images/datasets/data-validation/data-validation-for-customers/failed-results.png" />
</Frame>

## 通知与沟通

用户会在控制面板账户和电子邮件中收到状态更新通知。
