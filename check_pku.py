import requests
from bs4 import BeautifulSoup

url = "https://admission.pkusz.edu.cn/index.html"
headers = {"User-Agent": "Mozilla/5.0"}  # 像浏览器一样访问，避免被拒

try:
    r = requests.get(url, headers=headers, timeout=10)
    print("status:", r.status_code)
    print("apparent_encoding:", r.apparent_encoding)
    r.encoding = r.apparent_encoding or "utf-8"
    print("first200:", r.text[:200].replace("\n", " ") )
except Exception as e:
    print("error:", repr(e))
