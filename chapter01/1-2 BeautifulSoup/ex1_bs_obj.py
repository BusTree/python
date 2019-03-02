import bs4

html_Str = "<html><div>hello</div></html>"
bs_obj = bs4.BeautifulSoup(html_Str, "html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))

# 뷰티풀솝에 find 함수로 div 태크에 있는 항목만 불러옵니다.
