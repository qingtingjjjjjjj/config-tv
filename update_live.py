import os
import requests
from datetime import datetime

# 根目录输出文件
folder = "."
os.makedirs(folder, exist_ok=True)

# 链接和文件名（新增第三条接口 zubo_all.txt）
urls = {
    "video.json": "https://raw.githubusercontent.com/wwb521/live/refs/heads/main/video.json",
    "tv.txt": "https://raw.githubusercontent.com/wwb521/live/refs/heads/main/tv.txt",
    "zubo_all.txt": "https://raw.githubusercontent.com/q1017673817/iptvz/refs/heads/main/zubo_all.txt"
}

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

for filename, url in urls.items():
    file_path = os.path.join(folder, filename)
    print(f"➡️ 正在下载: {url} -> {file_path}")
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        # 检查内容是否为空
        if not response.content.strip():
            print(f"⚠️ 文件内容为空，未写入: {file_path}")
            continue

        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ 成功更新: {file_path}")
    except Exception as e:
        print(f"❌ 下载失败 {url} -> {e}")

# 更新时间日志
with open(os.path.join(folder, "last_update.txt"), "w") as f:
    f.write(f"Last update: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
print("📅 更新时间已记录 -> last_update.txt")
