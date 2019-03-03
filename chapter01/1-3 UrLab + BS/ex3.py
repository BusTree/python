import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")


menu = bs_obj.find("ul", {"id": "PM_ID_serviceNavi"})
print(menu)
print("===")

menuName = menu.findAll("span", {"class": "an_txt"})

for span in menuName:
    print(span.text)