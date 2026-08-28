> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取数据集元数据

<Tip>
  将您的 API Key 粘贴到授权字段。要获取 API Key，请[创建账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)并了解[如何生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
</Tip>

## 一般描述

* 此端点用于获取特定数据集的详细元数据。
* 元数据包括可用字段、数据类型以及字段说明。
* 使用此端点可在查询或下载数据集之前了解其结构。

## 请求

### **端点**

```

GET [http://api.brightdata.com/datasets/{dataset_id}/metadata](http://api.brightdata.com/datasets/{dataset_id}/metadata)

```

### **路径参数**

| 参数           | 类型       | 描述        |
| ------------ | -------- | --------- |
| `dataset_id` | `string` | 数据集的唯一标识符 |

### **请求头**

| Header          | 类型     | 描述            |
| --------------- | ------ | ------------- |
| `Authorization` | string | 用于认证的 API Key |

## 响应

### **响应示例**

```json theme={null}
{
    "id": "gd_l1vijqt9jfj7olije",
    "fields": {
        "name": {
            "type": "text",
            "active": true,
            "description": "公司名称"
        },
        "url": {
            "type": "url",
            "required": true,
            "description": "与公司关联的 URL 或网页地址"
        },
        "cb_rank": {
            "type": "number",
            "description": "公司在 Crunchbase 的排名"
        }
    }
}
```

### **响应字段**

| 字段       | 类型       | 描述             |
| -------- | -------- | -------------- |
| `id`     | `string` | 数据集的唯一标识符      |
| `fields` | `object` | 包含数据集中每个字段的元数据 |

### **字段元数据**

`fields` 对象中的每个字段包含以下属性：

| 属性            | 类型        | 描述                                |
| ------------- | --------- | --------------------------------- |
| `type`        | `string`  | 字段的数据类型（例如，`text`、`number`、`url`） |
| `active`      | `boolean` | 指示字段当前是否激活                        |
| `required`    | `boolean` | 指示字段是否为必填（如适用）                    |
| `description` | `string`  | 字段的简要描述                           |

## 示例用例

### **获取数据集元数据**

要获取 "Crunchbase companies information" 数据集的元数据：

#### **请求**

```
GET http://api.brightdata.com/datasets/gd_l1vijqt9jfj7olije/metadata
```

#### **响应**

```json theme={null}
{
    "id": "gd_l1vijqt9jfj7olije",
    "fields": {
        "name": {
            "type": "text",
            "active": true,
            "description": "公司名称"
        },
        "url": {
            "type": "url",
            "required": true,
            "description": "与公司关联的 URL 或网页地址"
        },
        "cb_rank": {
            "type": "number",
            "description": "公司在 Crunchbase 的排名"
        }
    }
}
```

## 故障排除与常见问题

### **问题: "Unauthorized" 响应**

**解决方案**：确保请求头中包含有效的 API Key。

### **问题: "Dataset not found"**

**解决方案**：确认 `dataset_id` 是否正确，并且存在于数据集列表中。

### **问题: "Field missing in metadata"**

**解决方案**：某些字段可能对特定数据集处于非激活状态或不可用。

## 相关文档

* [获取数据集列表](/cn/api-reference/marketplace-dataset-api/get-dataset-list)
* [数据集筛选 API](/cn/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files)
* [数据集下载 API](/cn/datasets/scrapers/custom-scrapers/custom-dataset-api)
