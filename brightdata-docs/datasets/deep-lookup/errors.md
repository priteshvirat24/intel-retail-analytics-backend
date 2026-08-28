> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Error handling

> Reference for Deep Lookup API error codes and response formats, including INVALID_QUERY and other common errors with resolution guidance.

## Error Response Format

```json theme={null}
{
  "error": {
    "code": "INVALID_QUERY",
    "message": "Query must start with 'Find all'",
    "details": "Please rephrase your query to begin with 'Find all' followed by what you're looking for"
  }
}
```

## Common Error Codes

| Code                   | Description                      | Resolution                  |
| :--------------------- | :------------------------------- | :-------------------------- |
| `INVALID_API_KEY`      | API key is missing or invalid    | Check your API key          |
| `RATE_LIMIT_EXCEEDED`  | Too many requests                | Wait and retry with backoff |
| `INVALID_QUERY`        | Query format is incorrect        | Follow query guidelines     |
| `INSUFFICIENT_CREDITS` | Account has insufficient credits | Add credits to account      |
| `REQUEST_NOT_FOUND`    | Request ID doesn't exist         | Verify request ID           |
| `PROCESSING_ERROR`     | Internal processing error        | Contact support             |
