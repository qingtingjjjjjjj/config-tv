import os
import requests
from datetime import datetime

# 根目录输出文件夹，如果不存在则创建
folder = "."
os.makedirs(folder, exist_ok=True)

# 链接和文件名
urls = {
    "video.json": "https://raw.bgithub.xyz/wwb521/live/refs/heads/main/video.json",
    "tv.txt": "https://raw.bgithub.xyz/wwb521/live/refs/heads/main/tv.txt"
}

for filename, url in urls.items():
    file_path = os.path.join(folder, filename)
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ 成功更新: {file_path}")
    except Exception as e:
        print(f"❌ 下载失败 {url} -> {e}")

# 可选：生成更新时间日志
with open(os.path.join(folder, "last_update.txt"), "w") as f:
    f.write(f"Last update: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
