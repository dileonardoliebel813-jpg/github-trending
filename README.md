# GitHub 热门项目推荐

自动追踪 GitHub 上 Python / JavaScript / TypeScript 热门开源项目，综合评分排序，每 6 小时自动更新，纯静态部署，零服务器成本。

**[🌐 在线预览](https://dileonardoliebel813-jpg.github.io/ClaudeProjects)** · **[📊 数据文件](data.json)**

![自动更新](https://github.com/dileonardoliebel813-jpg/ClaudeProjects/actions/workflows/update.yml/badge.svg)

---

## 预览截图

> 部署后将截图放置于此，命名为 `screenshot.png` 并提交到仓库根目录。

<!-- ![预览截图](screenshot.png) -->

---

## 功能特点

- **零服务器**：纯静态页面 + GitHub Actions + GitHub Pages，无需任何后端
- **综合评分**：`log(stars) + 0.5×log(forks) + 时间衰减`，综合热度与活跃度
- **多语言筛选**：支持 Python / JavaScript / TypeScript 一键切换
- **自动更新**：每 6 小时由 GitHub Actions 自动抓取并提交最新数据
- **精致 UI**：卡片式展示，悬停动效，前三名高亮，完整移动端适配
- **快速加载**：无框架依赖，原生 HTML/CSS/JS，首屏极速

---

## 技术栈

| 层级 | 技术 |
|---|---|
| 数据抓取 | Python 3.11 · GitHub REST API (`/search/repositories`) |
| 评分算法 | 对数缩放 stars/forks + 指数时间衰减（半衰期 30 天） |
| 前端展示 | 原生 HTML5 · CSS 自定义属性 · Vanilla JS |
| 自动化 | GitHub Actions（cron `0 */6 * * *` + 手动触发） |
| 托管 | GitHub Pages（静态，免费） |

---

## 项目结构

```
├── fetch.py                  # 数据抓取脚本 + 综合评分
├── data.json                 # 自动生成的推荐数据（不需手动编辑）
├── index.html                # 前端展示页面
├── styles.css                # 样式（CSS 自定义属性 + 响应式）
├── requirements.txt          # Python 依赖（requests）
└── .github/
    └── workflows/
        └── update.yml        # 定时自动更新工作流
```

---

## 自动更新说明

工作流文件：`.github/workflows/update.yml`

**触发方式**
- 定时：每 6 小时自动运行（UTC `0 */6 * * *`）
- 手动：在仓库 Actions 页面点击 `Run workflow`

**运行流程**
1. Checkout 代码
2. 安装 Python 依赖
3. 执行 `fetch.py`，调用 GitHub API 抓取各语言 Top 10
4. 对结果评分、排序，写入 `data.json`
5. 自动 `git commit` + `git push` 更新数据文件

**所需配置**

在仓库 `Settings → Secrets and variables → Actions` 中添加：

| Secret 名 | 说明 |
|---|---|
| `GH_PAT` | GitHub Personal Access Token，需要 `public_repo` 权限 |

---

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 设置 Token（可选，无 Token 匿名请求每小时限 10 次）
export GITHUB_TOKEN=your_token_here   # Windows: set GITHUB_TOKEN=your_token_here

# 抓取数据
python fetch.py

# 启动本地预览
python -m http.server 8000
# 浏览器访问 http://localhost:8000
```

---

## 部署到 GitHub Pages

1. 将代码推送到 GitHub 仓库
2. 仓库 `Settings → Pages → Source` 选择 `Deploy from a branch`
3. Branch 选 `main`，目录选 `/ (root)`，保存
4. 在 `Settings → Secrets` 中添加 `GH_PAT`
5. 访问 `https://<用户名>.github.io/<仓库名>`

---

## 后续计划

- [ ] 支持更多语言（Go、Rust、Java、C++ 等）
- [ ] 加入 topics / 标签维度筛选
- [ ] 评分引入 issue 活跃度、contributor 数量
- [ ] 历史趋势图（记录每日 star 增量曲线）
- [ ] 关键词搜索
- [ ] RSS / 邮件订阅推送
