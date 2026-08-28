> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 代码示例

> 使用深度查找 API 的代码示例。

<CodeGroup>
  ```python Python - 完整研究流程 theme={null}
  import requests
  import time

  class DeepLookupAPI:
      def __init__(self, api_key):
          self.api_key = api_key
          self.base_url = "https://api.brightdata.com/datasets/deep_lookup/v1"
          self.headers = {"Authorization": f"Bearer {api_key}"}
      
      def research_with_spec(self, query, columns, limit=100):
          # 创建详细规范
          spec = {
              "name": "companies",
              "query": query,
              "title": query.replace("Find all ", ""),
              "columns": columns
          }
          
          # 触发研究
          trigger_response = requests.post(
              f"{self.base_url}/trigger",
              headers=self.headers,
              json={
                  "query": query,
                  "spec": spec,
                  "result_limit": limit
              }
          ).json()
          
          request_id = trigger_response["request_id"]
          
          # 轮询完成状态
          while True:
              status_response = requests.get(
                  f"{self.base_url}/request/{request_id}/status",
                  headers=self.headers
              ).json()
              
              print(f"进度: {status_response.get('progress', 0)}%")
              
              if status_response["status"] == "completed":
                  break
              elif status_response["status"] == "failed":
                  raise Exception("研究失败")
              
              time.sleep(5)
          
          # 获取结果
          results = requests.get(
              f"{self.base_url}/request/{request_id}",
              headers=self.headers
          ).json()
          
          return results
      
      def monitor_progress(self, request_id):
          """监控研究请求的详细进度"""
          while True:
              result = requests.get(
                  f"{self.base_url}/request/{request_id}",
                  headers=self.headers
              ).json()
              
              step = result.get('step', 'unknown')
              
              if step == 'identifying':
                  print("分析查询中...")
              elif step == 'generating_schema':
                  print("创建数据结构...")
              elif step == 'generating':
                  pages = result.get('pages_read', 0)
                  matched = result.get('matched_records', 0)
                  print(f"处理数据: 已读取 {pages} 页, 已匹配 {matched} 条记录")
              elif step == 'done':
                  print("研究完成！")
                  return result
              
              time.sleep(3)

  # 使用示例
  api = DeepLookupAPI("YOUR_API_KEY")

  columns = [
      {
          "name": "company_name",
          "description": "公司名称",
          "type": "enrichment"
      },
      {
          "name": "is_ai_company",
          "description": "必须为 AI/ML 公司",
          "type": "constraint"
      },
      {
          "name": "employee_count",
          "description": "员工数量",
          "type": "enrichment"
      },
      {
          "name": "min_50_employees",
          "description": "至少有 50 名员工",
          "type": "constraint"
      }
  ]

  results = api.research_with_spec(
      "Find all AI companies in Israel with more than 50 employees",
      columns,
      limit=100
  )

  print(f"找到 {results['matched_records']} 家公司")
  print(f"跳过 {results['skipped_records']} 家公司（不满足所有条件）")
  print(f"总成本: {results['total_cost']}")
  ```

  ```javascript Node.js - 预览并执行，监控进度 theme={null}
  const axios = require('axios');

  class DeepLookupAPI {
    constructor(apiKey) {
      this.apiKey = apiKey;
      this.baseURL = 'https://api.brightdata.com/datasets/deep_lookup/v1';
      this.headers = {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      };
    }

    async previewAndExecute(query, limit = 100) {
      // 创建预览
      const previewResponse = await axios.post(
        `${this.baseURL}/preview`,
        { query },
        { headers: this.headers }
      );
      
      const previewId = previewResponse.data.preview_id;
      
      // 等待预览完成
      let previewData;
      do {
        await new Promise(resolve => setTimeout(resolve, 2000));
        const response = await axios.get(
          `${this.baseURL}/preview/${previewId}`,
          { headers: this.headers }
        );
        previewData = response.data;
      } while (previewData.status !== 'completed');
      
      console.log('预览完成，样本数:', previewData.sample_data.length);
      
      // 触发完整研究
      const triggerResponse = await axios.post(
        `${this.baseURL}/trigger`,
        {
          preview_id: previewId,
          result_limit: limit
        },
        { headers: this.headers }
      );
      
      const requestId = triggerResponse.data.request_id;
      
      // 监控详细进度
      let lastStep = '';
      let result;
      
      do {
        await new Promise(resolve => setTimeout(resolve, 3000));
        const response = await axios.get(
          `${this.baseURL}/request/${requestId}`,
          { headers: this.headers }
        );
        
        result = response.data;
        
        if (result.step !== lastStep) {
          lastStep = result.step;
          switch(result.step) {
            case 'identifying':
              console.log('分析查询中...');
              break;
            case 'generating_schema':
              console.log('创建数据结构...');
              break;
            case 'generating':
              console.log('从数据源收集数据...');
              break;
            case 'done':
              console.log('研究完成！');
              break;
          }
        }
        
        if (result.step === 'generating' && result.matched_records) {
          console.log(`   已找到 ${result.matched_records} 条匹配...`);
        }
        
      } while (result.step !== 'done' && result.status !== 'failed');
      
      return result;
    }

    async enrichResults(requestId, columnName, columnQuery) {
      // 添加扩展列
      const enrichResponse = await axios.post(
        `${this.baseURL}/request/${requestId}/enrich`,
        {
          column_name: columnName,
          query: columnQuery
        },
        { headers: this.headers }
      );
      
      console.log(`添加 "${columnName}" 列...`);
      console.log(`最大额外成本: ${enrichResponse.data.max_additional_cost}`);
      
      // 等待扩展完成
      // （具体实现取决于实际 API 行为）
      
      return enrichResponse.data;
    }
  }

  // 使用示例
  const api = new DeepLookupAPI('YOUR_API_KEY');

  async function runResearch() {
    const results = await api.previewAndExecute(
      'Find all B2B marketplaces in Europe', 
      50
    );
    
    console.log(`找到 ${results.matched_records} 个市场`);
    console.log(`跳过 ${results.skipped_records} 个不符合条件的记录`);
    console.log(`成本: ${results.total_cost}`);
    
    // 添加扩展列
    await api.enrichResults(
      results.request_id,
      'ceo_name',
      'CEO 或创始人姓名'
    );
  }

  runResearch();
  ```
</CodeGroup>
