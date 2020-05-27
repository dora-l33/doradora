#http://naver.com 사이트 이름을 가지고 비밀번호를 생성하기
#http://제외
#.이후 부분 제외
#비밀번호는 남은 글자 중 처음 세자리, 글자개수, 글자내 e개수, !로 구성

url = "http://naver.com"

a= url[7:10]
b=len(url[7:url.index(".")])
c=url.count("e")

print(f"{url}의 비밀번호는 {a}{b}{c}! 입니다.")
