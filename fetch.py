import os
import sys
import json
import math
import requests
from datetime import datetime, timedelta, timezone

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}" if GITHUB_TOKEN else "",
}

LANGUAGES = ["Python", "JavaScript", "TypeScript"]
PER_LANG = 10
SINCE_DAYS = 30


def fetch_trending(language: str, limit: int) -> list[dict]:
    since = (datetime.utcnow() - timedelta(days=SINCE_DAYS)).strftime("%Y-%m-%d")
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"language:{language} created:>{since}",
        "sort": "stars",
        "order": "desc",
        "per_page": limit,
    }
    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
        if resp.status_code == 403:
            reset = resp.headers.get("X-RateLimit-Reset", "")
            reset_time = datetime.fromtimestamp(int(reset)).strftime("%H:%M:%S") if reset else "未知"
            print(f"  [限流] {language} 跳过，API 重置时间：{reset_time}")
            return []
        resp.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"  [超时] {language} 请求超时，跳过")
        return []
    except requests.exceptions.RequestException as e:
        print(f"  [错误] {language} 请求失败：{e}")
        return []
    items = resp.json().get("items", [])
    return [
        {
            "full_name": r["full_name"],
            "html_url": r["html_url"],
            "description": r.get("description", ""),
            "language": r.get("language", ""),
            "stargazers_count": r["stargazers_count"],
            "forks_count": r["forks_count"],
            "pushed_at": r["pushed_at"],
        }
        for r in items
    ]


def score_repo(repo: dict) -> float:
    stars = repo["stargazers_count"]
    forks = repo["forks_count"]
    pushed_at = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
    days_since_push = (datetime.now(timezone.utc) - pushed_at).days
    # log scale for stars/forks, decay for recency (half-life ~30 days)
    recency = math.exp(-days_since_push / 30)
    return round(math.log1p(stars) * 1.0 + math.log1p(forks) * 0.5 + recency * 10, 4)


def main():
    if not GITHUB_TOKEN:
        print("[警告] 未设置 GITHUB_TOKEN，匿名请求每小时限 10 次")
    all_repos = []
    for lang in LANGUAGES:
        print(f"Fetching {lang}...")
        repos = fetch_trending(lang, PER_LANG)
        for repo in repos:
            repo["score"] = score_repo(repo)
        all_repos.extend(repos)
        print(f"  Got {len(repos)} repos")

    if not all_repos:
        print("[错误] 未获取到任何数据，终止写入")
        sys.exit(1)

    all_repos.sort(key=lambda r: r["score"], reverse=True)

    output = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_count": len(all_repos),
        "projects": all_repos,
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved to data.json ({len(all_repos)} projects)")


if __name__ == "__main__":
    main()
