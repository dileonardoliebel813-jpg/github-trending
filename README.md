# GitHub 热门项目推荐系统

> 自动抓取 GitHub 上 Python / JavaScript / TypeScript 热门开源项目，综合评分排序，每 6 小时自动更新。

**[🌐 在线预览](https://你的用户名.github.io/仓库名)** · **[📊 数据文件](data.json)**

![自动更新](https://github.com/你的用户名/仓库名/actions/workflows/update.yml/badge.svg)

## 项目亮点

- 零服务器：纯静态页面 + GitHub Actions + GitHub Pages
- 综合评分：`log(stars) + 0.5×log(forks) + 时间衰减`
- 按语言筛选，卡片式展示，适配移动端

## 目录结构

```
├── fetch.py                  # 数据抓取 + 评分
├── data.json                 # 生成的推荐数据
├── index.html                # 展示页面
├── styles.css                # 样式
├── requirements.txt          # Python 依赖
└── .github/workflows/
    └── update.yml            # 定时自动更新
```


## 功能

- 抓取近 30 天内新建的热门仓库（每类 10 个）
- 综合评分：star 数、fork 数、最近推送时间
- 按语言筛选，卡片式展示
- GitHub Actions 定时自动更新数据
- GitHub Pages 静态托管，无需服务器

## 技术栈

| 层 | 技术 |
|---|---|
| 数据抓取 | Python + GitHub REST API |
| 页面展示 | 原生 HTML / CSS / JS |
| 自动化 | GitHub Actions |
| 托管 | GitHub Pages |

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 设置 GitHub Token（可选，无 Token 有限速）
export GITHUB_TOKEN=your_token_here   # Windows: set GITHUB_TOKEN=...

# 抓取数据
python fetch.py

# 启动本地预览
python -m http.server 8000
# 访问 http://localhost:8000
```

## GitHub Actions 自动更新

工作流文件：`.github/workflows/update.yml`

- 每 6 小时自动运行一次
- 支持在 Actions 页面手动触发
- 运行后自动提交更新的 `data.json`

**需要在仓库 Settings → Secrets → Actions 中添加：**

| Secret 名 | 值 |
|---|---|
| `GH_PAT` | 你的 GitHub Personal Access Token（需要 `public_repo` 权限） |

## GitHub Pages 访问

1. 仓库 Settings → Pages
2. Source 选 `Deploy from a branch`，Branch 选 `main`，目录选 `/ (root)`
3. 保存后访问：`https://你的用户名.github.io/仓库名`

## 后续优化方向

- [ ] 增加更多语言支持（Go、Rust、Java 等）
- [ ] 加入项目 topics / 标签筛选
- [ ] 评分公式引入 issue 活跃度、contributor 数
- [ ] 历史趋势图（记录每日 star 增量）
- [ ] 支持搜索关键词
- [ ] 邮件 / RSS 订阅推送
