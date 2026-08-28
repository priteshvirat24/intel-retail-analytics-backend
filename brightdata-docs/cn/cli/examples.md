> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用示例

> Bright Data CLI 的真实工作流程和配方 - 从简单爬取到高级自动化管道。

## 爬取工作流程

### 从任何网站获取干净的内容

```bash theme={null}
# 清洁的 markdown - 适合阅读或输入到 LLM
brightdata scrape https://news.ycombinator.com

# 保存到文件
brightdata scrape https://docs.python.org/3/tutorial/ -o python-tutorial.md

# 获取原始 HTML 用于解析
brightdata scrape https://example.com -f html -o page.html
```

### 地理位置目标爬取

```bash theme={null}
# 查看美国客户的亚马逊价格
brightdata scrape https://amazon.com/dp/B09V3KXJPB --country us

# 从德国爬取德国新闻网站
brightdata scrape https://spiegel.de --country de

# 移动用户代理用于移动优化页面
brightdata scrape https://example.com --mobile
```

### 截图

```bash theme={null}
# 整页截图
brightdata scrape https://example.com -f screenshot -o homepage.png

# 从特定国家截图
brightdata scrape https://amazon.co.uk -f screenshot --country gb -o uk-amazon.png
```

***

## 搜索工作流程

### 基础网络搜索

```bash theme={null}
# 谷歌搜索，带格式化表格输出
brightdata search "best web scraping tools 2025"

# 获取原始 JSON 用于处理
brightdata search "typescript best practices" --json

# 格式化打印用于检查
brightdata search "AI startups" --pretty
```

### 本地化和专业搜索

```bash theme={null}
# 从德国进行本地餐厅搜索，使用德语
brightdata search "restaurants berlin" --country de --language de

# 仅新闻结果
brightdata search "AI regulation 2025" --type news

# 购物结果
brightdata search "wireless headphones" --type shopping

# 图片搜索
brightdata search "mountain landscape wallpaper" --type images
```

### 分页

```bash theme={null}
# 第一页（默认）
brightdata search "web scraping tutorials"

# 第二页
brightdata search "web scraping tutorials" --page 1

# 第三页
brightdata search "web scraping tutorials" --page 2
```

***

## 结构化数据提取

### 电子商务

```bash theme={null}
# 亚马逊产品详情
brightdata pipelines amazon_product "https://amazon.com/dp/B09V3KXJPB"

# 亚马逊产品评论
brightdata pipelines amazon_product_reviews "https://amazon.com/dp/B09V3KXJPB"

# 亚马逊搜索 - 需要关键词 + 域名
brightdata pipelines amazon_product_search "wireless headphones" "https://amazon.com"

# 沃尔玛产品
brightdata pipelines walmart_product "https://walmart.com/ip/123456"

# 导出为 CSV
brightdata pipelines amazon_product "https://amazon.com/dp/B09V3KXJPB" --format csv -o product.csv
```

### 社交媒体资料

```bash theme={null}
# LinkedIn 个人资料
brightdata pipelines linkedin_person_profile "https://linkedin.com/in/username"

# LinkedIn 公司资料
brightdata pipelines linkedin_company_profile "https://linkedin.com/company/bright-data"

# Instagram 资料
brightdata pipelines instagram_profiles "https://instagram.com/username"

# TikTok 资料
brightdata pipelines tiktok_profiles "https://tiktok.com/@username"
```

### 评论和评价

```bash theme={null}
# Google Maps 评论 - 最近 7 天
brightdata pipelines google_maps_reviews "https://maps.google.com/maps/place/..." 7

# YouTube 评论 - 前 50 条
brightdata pipelines youtube_comments "https://youtube.com/watch?v=dQw4w9WgXcQ" 50

# Facebook 公司评论 - 25 条评论
brightdata pipelines facebook_company_reviews "https://facebook.com/company" 25

# Instagram 评论
brightdata pipelines instagram_comments "https://instagram.com/p/ABC123"
```

***

## 管道和自动化

CLI 设计为支持管道。当标准输出不是 TTY 时，颜色和加载指示器会自动禁用。

### 链接搜索 → 爬取

```bash theme={null}
# 搜索谷歌，提取第一个 URL，然后爬取它
brightdata search "best python frameworks 2025" --json \
  | jq -r '.organic[0].link' \
  | xargs brightdata scrape
```

### 爬取并在终端中阅读

```bash theme={null}
# 将 markdown 输出管道到终端阅读器
brightdata scrape https://docs.github.com | glow -

# 或使用 less
brightdata scrape https://docs.github.com | less
```

### 导出为 CSV 用于分析

```bash theme={null}
# 亚马逊产品数据到 CSV
brightdata pipelines amazon_product "https://amazon.com/dp/B09V3KXJPB" --format csv > product.csv

# LinkedIn 职位到 CSV
brightdata pipelines linkedin_job_listings "https://linkedin.com/jobs/view/123" --format csv -o jobs.csv
```

### 使用 jq 提取特定字段

```bash theme={null}
# 从亚马逊搜索中仅获取标题和价格
brightdata pipelines amazon_product_search "laptop" "https://amazon.com" \
  | jq '[.[] | {title, price: .final_price}]'

# 从搜索中仅获取有机结果 URL
brightdata search "web scraping" --json | jq -r '.organic[].link'
```

### 异步作业用于重型工作负载

```bash theme={null}
# 提交异步爬取
JOB_ID=$(brightdata scrape https://heavy-page.com --async --json | jq -r '.snapshot_id')

# 进行其他工作...

# 稍后检查
brightdata status $JOB_ID --wait --pretty
```

***

## 账户管理

### 监控成本

```bash theme={null}
# 快速余额检查
brightdata budget

# 详细余额包括待处理费用
brightdata budget balance

# 按区域的成本分析
brightdata budget zones

# 特定日期范围内的特定区域
brightdata budget zone cli_unlocker --from 2024-01-01T00:00:00 --to 2024-02-01T00:00:00
```

### 管理配置

```bash theme={null}
# 查看当前配置
brightdata config

# 设置默认输出为 JSON
brightdata config set default_format json

# 使用自定义区域进行爬取
brightdata config set default_zone_unlocker my_custom_zone

# 覆盖 SERP 区域
brightdata config set default_zone_serp my_serp_zone
```

***

## AI 代理集成

### 为编码代理安装技能

```bash theme={null}
# 交互式选择器 - 选择技能和目标代理
brightdata skill add

# 将爬取技能安装到你的代理中
brightdata skill add scrape

# 安装搜索功能
brightdata skill add search

# 查看所有可用技能
brightdata skill list
```

<Tip>
  技能是预先打包的提示和配置束，教导 AI 编码代理如何有效使用 Bright Data。详见 [技能](/cn/ai/for-agents/skills)。
</Tip>

***

## 环境变量

使用环境变量覆盖任何存储的配置：

| 变量                           | 用途                 |
| ---------------------------- | ------------------ |
| `BRIGHTDATA_API_KEY`         | API 密钥（完全跳过登录）     |
| `BRIGHTDATA_UNLOCKER_ZONE`   | 默认 Web Unlocker 区域 |
| `BRIGHTDATA_SERP_ZONE`       | 默认 SERP 区域         |
| `BRIGHTDATA_POLLING_TIMEOUT` | 轮询超时时间（秒）          |

```bash theme={null}
# 在 CI/CD 中使用，无需登录
BRIGHTDATA_API_KEY=your_key brightdata scrape https://example.com

# 为大型管道作业覆盖超时
BRIGHTDATA_POLLING_TIMEOUT=1200 brightdata pipelines amazon_product "https://amazon.com/dp/..."
```
