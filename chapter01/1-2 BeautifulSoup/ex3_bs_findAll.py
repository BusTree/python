import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

li = bs_obj.findAll("li")  # 하위 li 요소가 전부 나옴
print(li)
print("===")
print(li[1])    # findall 의 경우 리턴값이 배열로 나오기떄문에 배열로 li요소를 선택할수있다.
print("===")
print(li[1].text)
