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

ul = bs_obj.find("ul") ## ul 요소만 가져옴
print(ul)
print("===")

li = ul.find("li") # 가져온 ul 요소중에서 li 요소만 가져옴
print(li)
print("===")

print(li.text)  # li의 텍스트만 출력함

## find 함수는 선택한 태그의 첫번째요소만 가져옵니다 같은이름의 태그가 2개이상일경우 두개다 가져오지못함
