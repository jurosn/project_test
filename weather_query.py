import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    headers = {  # 表现得像真人
        "User-Agent": "Mozilla/5.0" # 伪装成正常浏览器，最常见，通用标志
    }

    try:
        # 向目标网站发送请求，发送伪装的浏览器信息，要求回复时间不超过5s
        response = requests.get(url, headers=headers, timeout=5)
        # 返回状态，200则成功，404和500有异常
        response.raise_for_status()
    except Exception as e: # 返回错误原因
        print("Error fetching weather:", e)
        return
    
    # response.text 是网站返回的html语言
    # 用BeautifulSoup库解析html
    soup = BeautifulSoup(response.text, "html.parser")
    # 找到返回数据中含有<span>(span为html语言的标签)的标签
    # class_表示找到class属性为phrase的<span>标签
    weather = soup.find("span", class_="phrase")

    if weather:
        print(f"Weather in {city}: {weather.text}") # .text 提取文字
    else:
        print("Sorry, weather info not found.")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)