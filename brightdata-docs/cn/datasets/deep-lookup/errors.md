> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 错误处理

### 错误响应格式

```json theme={null}
{
  "error": {
    "code": "INVALID_QUERY",
    "message": "查询必须以 'Find all' 开头",
    "details": "请重新表述您的查询，使其以 'Find all' 开头，后跟您要查找的内容"
  }
}
```

### 常见错误代码

| 代码                     | 描述          | 解决方法        |
| :--------------------- | :---------- | :---------- |
| `INVALID_API_KEY`      | API 密钥缺失或无效 | 检查您的 API 密钥 |
| `RATE_LIMIT_EXCEEDED`  | 请求过多        | 等待并使用退避机制重试 |
| `INVALID_QUERY`        | 查询格式不正确     | 遵循查询指南      |
| `INSUFFICIENT_CREDITS` | 账户积分不足      | 为账户添加积分     |
| `REQUEST_NOT_FOUND`    | 请求 ID 不存在   | 验证请求 ID     |
| `PROCESSING_ERROR`     | 内部处理错误      | 联系支持        |
