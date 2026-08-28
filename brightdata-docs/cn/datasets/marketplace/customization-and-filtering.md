> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 自定义与筛选

> 通过 UI 或 API 自定义字段并筛选 Bright Data Marketplace 数据集（250+ 个域名），获取您所需的数据子集。

通过 UI 或 API，将 Bright Data Marketplace 数据集（250+ 个域名）缩小到您所需的确切记录和字段，方法是创建筛选子集并选择要包含的字段。

**您可以执行的操作：**

* **自定义字段：** 选择要包含在数据集视图或导出中的列（字段）。
* **筛选数据集：** 使用筛选规则创建已保存的子集。

**权限：** 您需要拥有该数据集的访问权限以及创建子集的权限。

<Frame>
  <img src="https://mintcdn.com/brightdata/eNyljOHwBKMSV2wr/images/datasets/marketplace/customization-and-filtering/customize-button.gif?s=2a76573b8dff5a970f2a1c74cb918c82" alt="自定义数据集的动画演示：在预览表中选择字段并应用筛选" width="1080" height="608" data-path="images/datasets/marketplace/customization-and-filtering/customize-button.gif" />
</Frame>

## 自定义字段

选择要在 Bright Data Marketplace 数据集视图和导出中显示的字段（列）。

1. 导航到您要处理的数据集。
2. 打开字段选择器（Fields selector）。
3. 选择要包含在视图中的字段。
4. 点击 Apply（应用），如果系统提示，请保存该视图。

**预期结果：** 该视图的数据集预览以及任何导出都将仅包含所选字段。

<Frame>
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/marketplace/customization-and-filtering/customize-fields.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=0bcc581f9abeba46c18517fc5962c38e" alt="字段选择器已打开，显示可用字段，已选字段被勾选" width="1920" height="941" data-path="images/datasets/marketplace/customization-and-filtering/customize-fields.png" />
</Frame>

## 筛选数据集

通过在 UI 或 API 中应用筛选规则，创建 Bright Data Marketplace 数据集的已保存子集。

<Frame>
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/datasets/marketplace/customization-and-filtering/filter.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=5b6b9cce86b69560265b1ff18c4dde42" alt="筛选面板已打开，显示包含筛选条件和创建子集" width="1920" height="941" data-path="images/datasets/marketplace/customization-and-filtering/filter.png" />
</Frame>

### 使用 UI 筛选数据集

1. 导航到您要筛选的数据集。
2. 点击筛选图标（右上角）。
3. 输入名称，以便日后找到此子集。
4. 在 Include filters（包含筛选条件）下，添加一个或多个筛选条件（例如：国家、职位、日期）。
5. 点击 Create subset（创建子集）。

**预期结果：** 将出现一个仅包含符合筛选条件记录的新子集。

### 筛选运算符参考

#### Select（选择）

从预定义列表中匹配一个或多个精确值（例如：国家或地区）。

#### Boolean（布尔值，true/false）

筛选只能为 true 或 false 的字段（例如：类似 `verified` 的字段）。

#### Date（日期）

筛选特定日期范围内的记录（起始日期和结束日期）。

#### Number（数值，运算符）

* **Is（等于）：** 匹配精确数值。
* **Not（不等于）：** 排除某个数值。
* **Exists（存在）：** 仅包含该字段非空的记录。
* **List (exact match)（列表，精确匹配）：** 匹配所提供列表中的任意值。
* **Lower than / Lower or equal to（小于 / 小于等于）：** 匹配低于（或不超过）阈值的值。
* **Greater than / Greater or equal to（大于 / 大于等于）：** 匹配高于（或达到）阈值的值。

#### String（字符串）

使用 UI 中提供的匹配类型筛选文本字段（例如：精确匹配或包含）。

#### Array（数组）

使用 Array includes（数组包含）匹配多值（数组）字段中包含特定值的记录（例如：类别、属性或标签）。

#### 上传 CSV 列表

如果需要匹配大量值，请在值输入框中使用 CSV 上传选项。上传一个每行一个值的 CSV 文件。上传后，筛选器会匹配数组中包含所上传列表中任意值的记录。

#### CSV 上传的限制

* **CSV 格式：** 上传一个每行一个值的 `.csv` 文件（单列）。
* **每个列表最多 10,000 个值：** 如需匹配更多值，请将这些值拆分到多个 CSV 列表中（最多共 100,000 个值），并在不同的子集中分别作为筛选器应用。
* **不允许空行或仅含空白的行：** 仅包含空格的行会被拒绝。
* **仅限单列：** CSV 必须只包含一列。如果包含表头，表头也必须是单列。
* **每行一个值：** 每行只放一个筛选值。不要在同一行用逗号分隔多个值。

### Includes 与 List（精确匹配）的区别

#### Includes（包含）

使用 Includes（包含）匹配字段中包含你所输入值的记录（部分匹配）。

示例：如果字段为 `name`，并使用 Includes = `john` 进行筛选，则可匹配到 `John Smith` 和 `Johnson` 等值。

#### List（精确匹配）

使用 List（精确匹配）匹配字段值恰好等于列表中某个值的记录（不进行部分匹配）。

示例：List（精确匹配）= `John Smith`、`Jane Doe` 仅匹配这些精确的值。

### 分组筛选器（基于规则的筛选）

1. 点击 + Add filter（添加筛选条件）。
2. 选择 Add group（添加分组）。
3. 定义您的分组规则（例如：类别为"电子产品"，且品牌为"Dell"或"Apple"）。

**预期结果：** 该子集仅包含符合您分组逻辑的记录。

### 局限

* 分组不能嵌套。
* 每个筛选器最多允许 2 个分组。
* 每个筛选分组最多允许 4 个输入。
* 要按更多值筛选，请使用 CSV 列表上传选项（如果可用），或联系您的账户经理。
* 如需更复杂的查询，请联系您的账户经理。

## 故障排除

* **我看不到筛选图标。** 请确保您正在查看数据集表格，并且您的账户拥有创建子集的权限。
* **我的子集没有返回任何结果。** 逐个移除筛选条件以找出限制性条件，然后重新应用正确的值和运算符。

## 后续步骤

* [导出或下载数据集子集](/cn/datasets/marketplace/data-delivery-and-export)
* [通过 API 筛选数据集](/cn/datasets/marketplace/filter-dataset-by-api)
* [Bright Data Marketplace 数据集概述](/cn/datasets/marketplace/overview)
