from urllib.request import urlopen

url = "https://www.naver.com/"
html = urlopen(url)
print(html.read())

# urlopen 함수로  네이버 html을 가져옵니다