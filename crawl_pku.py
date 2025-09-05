import requests
from bs4 import BeautifulSoup

# 目标网址（北京大学研究生招生网）
url = "https://admission.pkusz.edu.cn/index.html"

# 发送请求
response = requests.get(url)
response.encoding = 'utf-8'  # 设置编码，防止中文乱码

# 解析网页
soup = BeautifulSoup(response.text, "html.parser")

# 找到所有文章标题和链接
for link in soup.find_all("a"):
    title = link.get_text(strip=True)
    href = link.get("href")
    if title and "招生简章" in title:  # 简单过滤：包含“招生简章”的文章
        print(title, href)

