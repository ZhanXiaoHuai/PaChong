import requests
from Tools.scripts.verify_ensurepip_wheels import print_notice
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()

random_user_agent=ua.getGoogle

print(random_user_agent)

#爬取所有书籍和价格
# param={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
# }
# response=requests.get("https://books.toscrape.com/",headers=param).text
# soup=BeautifulSoup(response,"html.parser")
# all_prices=soup.find_all("p",attrs={"class":"price_color"})
# for price in all_prices:
#     print(price)
#
# all_titles=soup.find_all("h3")
# for title in all_titles:
#     all_links=title.find_all("a")
#     for link in all_links:
#         print(link.string)


param={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

for start_num in range(0,1,25):
    response=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=param)
    html=response.text
    soup=BeautifulSoup(html,"html.parser")

    all_titles=soup.find_all("span",attrs={"class":"title"})
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:
            print(title_string)
