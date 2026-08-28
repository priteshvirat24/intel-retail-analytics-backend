> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 理解AI爬虫工作室API

AI Scraper Studio API 是一组端点，允许你使用 AI 创建 Scraper Studio 爬虫并使用自我修复工具更新现有爬虫，无需使用 UI。本页说明了应该调用哪个端点以及调用顺序。

两个流程都是异步的：你启动一个 AI 任务，然后检查其进度直到完成。

### 工作流 1：使用 AI 创建新爬虫

当你想让 AI 从头为目标网站生成爬虫（schema + 代码）时，请使用这些端点。

1. 创建爬虫实体\
   → <Badge color="blue"><a href="/api-reference/scraper-studio-api/ai-flow/create-scraper-template" target="_blank">创建爬虫模板</a></Badge>

2. 启动 AI 生成任务（schema + 代码）\
   → <Badge color="blue"><a href="/api-reference/scraper-studio-api/ai-flow/trigger-ai-flow" target="_blank">触发 AI Flow 以创建代码</a></Badge>

3. 轮询直到 AI 任务完成并返回结果\
   → <Badge color="blue"><a href="/api-reference/scraper-studio-api/ai-flow/ai-job-progress" target="_blank">AI 任务进度</a></Badge>

### 工作流 2：使用自我修复更新现有爬虫

当你已经有一个爬虫并想使用提示修复或修改它时，请使用这些端点。

1. 启动自我修复重构任务\
   → <Badge color="blue"><a href="/api-reference/scraper-studio-api/ai-flow/trigger-self-healing" target="_blank">触发自我修复</a></Badge>

2. 轮询直到重构任务完成或暂停等待用户输入\
   → <Badge color="blue"><a href="/api-reference/scraper-studio-api/ai-flow/self-healing-job-progress" target="_blank">自我修复任务进度</a></Badge>

3. 如果进度返回 `status: "pending_answer"`，批准或拒绝建议的差异\
   → <Badge color="blue"><a href="/cn/api-reference/scraper-studio-api/ai-flow/resume-self-healing-job" target="_blank">恢复自我修复任务</a></Badge>

4. 爬虫准备好后，启动采集\
   → <Badge color="blue"><a href="/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method" target="_blank">启动采集</a></Badge>

创建或更新后，使用标准 Scraper Studio API 启动端点运行它（手动触发、计划、队列等）。

<Columns cols={2}>
  <Tip>
    **不确定使用哪个？**

    * 还没有爬虫 → [工作流 1](#workflow-1-create-a-new-scraper-with-ai)
    * 爬虫需要更改 → [工作流 2](#workflow-2-update-an-existing-scraper-with-self-healing)
  </Tip>

  <Tip>
    **初次使用 API？**

    参见：<a href="/cn/datasets/scraper-studio/quickstart" target="_blank">API 入门指南</a>
  </Tip>
</Columns>
