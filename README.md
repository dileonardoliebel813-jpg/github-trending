# GitHub Trending Radar

> 自动追踪 GitHub 热门开源项目，用可解释评分算法生成 Python / JavaScript / TypeScript 趋势看板。  
> A static trend radar for discovering high-momentum open-source repositories with automated GitHub Actions updates.

[![Automation](https://github.com/dileonardoliebel813-jpg/github-trending/actions/workflows/update.yml/badge.svg)](https://github.com/dileonardoliebel813-jpg/github-trending/actions)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-2ea44f?style=flat-square)](https://pages.github.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

---

## 项目定位 / Overview

GitHub Trending Radar 是一个零后端、可自动更新的开源项目趋势看板。它通过 GitHub REST API 抓取热门仓库数据，并使用 stars、forks 和更新时间衰减计算综合热度分数，帮助快速发现近期更值得关注的开源项目。

This project demonstrates API integration, data ranking, scheduled automation, and static-site deployment. It is designed as a portfolio-ready data automation project rather than a simple static page.

---

## 在线预览 / Live Demo

> 如果 GitHub Pages 已启用，访问地址通常为：

```text
https://dileonardoliebel813-jpg.github.io/github-trending/
```

数据文件：[`data.json`](./data.json)

---

## 核心功能 / Features

- **自动数据抓取**：通过 GitHub REST API 获取 Python / JavaScript / TypeScript 热门仓库。
- **可解释评分**：综合 stars、forks 与更新时间衰减，避免只看单一指标。
- **定时刷新**：GitHub Actions 每 6 小时自动运行并更新 `data.json`。
- **静态部署**：无后端服务，适合 GitHub Pages 低成本长期托管。
- **前端筛选**：支持按语言切换趋势项目。
- **响应式 UI**：卡片式展示、排名突出、移动端可读。

---

## 评分逻辑 / Ranking Logic

项目不是简单按 star 数排序，而是使用综合评分衡量“热度 + 传播度 + 新鲜度”：

```text
score = log(stars) + 0.5 × log(forks) + time_decay
```

| 维度 | 作用 |
|---|---|
| `log(stars)` | 衡量项目关注度，同时用对数压缩超大仓库优势 |
| `0.5 × log(forks)` | 衡量社区使用和二次开发意愿 |
| `time_decay` | 给近期更新项目更高权重，降低长期静态项目占榜概率 |

这种方式让榜单更适合发现“近期仍然活跃、值得继续观察”的项目。

---

## 技术栈 / Tech Stack

| 模块 | 技术 |
|---|---|
| 数据抓取 | Python 3.11, GitHub REST API `/search/repositories` |
| 数据处理 | requests, JSON, custom scoring formula |
| 前端展示 | HTML5, CSS3, Vanilla JavaScript |
| 自动化 | GitHub Actions cron workflow |
| 部署 | GitHub Pages static hosting |

---

## 架构流程 / Architecture

```text
GitHub Actions Scheduler
          │
          ▼
      fetch.py
          │
          ▼
GitHub REST API Search
          │
          ▼
 scoring + normalization
          │
          ▼
      data.json
          │
          ▼
  Static HTML/CSS/JS UI
          │
          ▼
     GitHub Pages
```

---

## 项目结构 / Project Structure

```text
├── fetch.py                  # 数据抓取脚本与综合评分逻辑
├── data.json                 # 自动生成的趋势数据
├── index.html                # 静态页面结构
├── styles.css                # 响应式样式与视觉设计
├── requirements.txt          # Python 依赖
└── .github/
    └── workflows/
        └── update.yml        # 定时更新工作流
```

---

## 本地运行 / Local Development

```bash
pip install -r requirements.txt
```

可选：设置 GitHub Token，提高 API 限额。

```bash
export GITHUB_TOKEN=your_token_here
```

Windows CMD：

```bat
set GITHUB_TOKEN=your_token_here
```

抓取数据并启动本地预览：

```bash
python fetch.py
python -m http.server 8000
```

浏览器访问：

```text
http://localhost:8000
```

---

## 自动化配置 / Automation

工作流文件：`.github/workflows/update.yml`

| 触发方式 | 说明 |
|---|---|
| `cron: 0 */6 * * *` | 每 6 小时自动刷新 |
| `workflow_dispatch` | 支持手动触发 |

推荐在仓库 `Settings → Secrets and variables → Actions` 添加：

| Secret | 说明 |
|---|---|
| `GH_PAT` | GitHub Personal Access Token，建议具备 `public_repo` 权限 |

如果没有 Token，匿名 GitHub API 请求会受到更严格的速率限制。

---

## 部署到 GitHub Pages / Deployment

1. 推送代码到 GitHub 仓库。
2. 打开 `Settings → Pages`。
3. Source 选择 `Deploy from a branch`。
4. Branch 选择 `main`，目录选择 `/ (root)`。
5. 保存后访问：

```text
https://<username>.github.io/<repository-name>/
```

---

## 作品集亮点 / Portfolio Highlights

- 将公开 API 数据转化为可浏览、可比较、可自动更新的产品化页面。
- 用轻量评分算法解决“只按 star 排名不够准确”的问题。
- 展示了从数据抓取、算法处理、自动化更新到静态部署的完整闭环。
- 无需服务器即可长期运行，适合作为低成本数据产品 Demo。
- 代码结构清晰，适合继续扩展语言维度、趋势图和订阅推送。

---

## 后续计划 / Roadmap

- [ ] 支持 Go、Rust、Java、C++ 等更多语言
- [ ] 增加 topics / 标签筛选
- [ ] 引入 issue 活跃度、贡献者数量等指标
- [ ] 增加历史趋势图和 star 增长曲线
- [ ] 增加关键词搜索
- [ ] 支持 RSS 或邮件订阅

---

## Author

GitHub: [@dileonardoliebel813-jpg](https://github.com/dileonardoliebel813-jpg)
