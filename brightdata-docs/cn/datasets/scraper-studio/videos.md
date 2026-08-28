> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 视频教程

> Bright Data Scraper Studio 视频演练：构建搜索爬虫、处理分页、使用模板、调试、交付与抓取动态站点。

本页是 Bright Data Scraper Studio 视频教程的索引。每个视频都对应一篇文档指南。根据您正在构建的内容选择对应主题直接开始。

## 入门

### Bright Data Scraper Studio 简介

带您直观了解 Bright Data Scraper Studio IDE：模板、代理网络，以及如何在一个流程中构建多个爬虫。如果您此前从未在 Bright Data 上构建过爬虫，请从这里开始。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/Ve04_6gDKvU" title="Introduction to Bright Data Web Scraper IDE" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [了解 Scraper Studio](/cn/datasets/scraper-studio/introduction)

### 平台概览：项目设置、代理与自动化

演练 Bright Data Scraper Studio 的核心功能：项目设置、代理的创建与管理，以及调度自动化采集运行。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/qo_fUjb02ns" title="Industrial-scale web scraping with AI and proxy networks" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [Scraper Studio IDE 界面](/cn/datasets/scraper-studio/scraper-studio-ide-interface)

## 构建爬虫

### 从 Amazon 搜索结果中抓取数据

如何抓取 Amazon 搜索结果、构建一个能遍历分页结果的爬虫，并依靠 Bright Data 代理网络规避封锁。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/YRRW4o-BjEM" title="Scrape Amazon search results" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [开发爬虫](/cn/datasets/scraper-studio/develop-a-scraper)

### 使用 `for` 循环遍历搜索结果

如何使用 `for` 循环导航数百页结果、提取每条列表的链接，并通过 `parse()` 和 `collect()` 收集数据。涵盖代理管理器设置、基础模板、输入定位、运行与测试代码以及读取日志。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/0w9BAIVGuCA" title="Walk search results with for loops" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [网页爬取基础](/cn/datasets/scraper-studio/basics-of-web-scraping)

### 使用模板并部署多个爬虫

如何从 IDE 模板开始构建一个 Walmart 爬虫、将其部署到代理网络，并将数据收集到单一 API 响应中。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/jQzI2ywA988" title="Use IDE templates and proxy networks" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [Scraper Studio 函数参考](/cn/datasets/scraper-studio/functions)

### 端到端构建一个 Python 爬虫

构建一个使用 Bright Data Scraper Studio 模板的 Python 项目，修改代码、预览结果、配置交付，并通过 API 获取数据。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/7ahUnBhdI5o" title="Build a Python scraper end-to-end" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [启动数据收集与交付](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options)

## 处理复杂站点

### 使用工具函数抓取动态站点

如何借助 Bright Data 的浏览器辅助函数抓取重度动态的站点：等待网格渲染、循环遍历网格单元，以及使用 `next_stage()` 分发详情采集。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/Pm93D8CVlY8" title="Scrape dynamic sites with utility functions" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [最佳实践](/cn/datasets/scraper-studio/best-practices)

### 使用 Python 自动化 Airbnb

如何自定义 Bright Data Scraper Studio 模板抓取 Airbnb，以及通过 API 触发爬虫并获取结果的完整流程。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/ASWS7eU5ao4" title="Automate Airbnb with Python" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [Scraper Studio AI Agent](/cn/datasets/scraper-studio/ai-agent)

## 调试与交付

### 调试爬虫并配置交付

如何在 IDE 中调试爬虫、阅读运行日志和错误，并选择交付方式（API 端点或 Amazon S3）。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/BVizDqOfins" title="Debug a scraper and configure delivery" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [Scraper Studio IDE 界面](/cn/datasets/scraper-studio/scraper-studio-ide-interface)

### 使用 Tableau 完成端到端数据工程

一段较长的演练：代理管理器、API 集成、从模板构建爬虫、按产品或类别使用输入、运行代码以及通过日志调试。

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/vSgJ3bOyE0w" title="End-to-end data engineering project" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**搭配阅读：** [功能参考](/cn/datasets/scraper-studio/features)

## 相关内容

<CardGroup cols={2}>
  <Card title="了解 Scraper Studio" icon="book-open" href="/cn/datasets/scraper-studio/introduction">
    Bright Data Scraper Studio 如何工作以及何时使用
  </Card>

  <Card title="开发爬虫" icon="wrench" href="/cn/datasets/scraper-studio/develop-a-scraper">
    在 IDE 中构建爬虫的分步演练
  </Card>
</CardGroup>
