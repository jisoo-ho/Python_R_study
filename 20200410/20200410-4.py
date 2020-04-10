
import os

for x in os.listdir('c:/windows'):
    if x.endswith('exe'):
        print(x)

i = 0
for stock in['Naver', 'KAKAO', 'SK']:
    print(i, stock)
    i += 1


# 인덱스번호로 뭔가를 작업하고 싶은 경우에 사용
for i, stock in enumerate(["Naver","KAKAO","SK"]):
    print(i, stock)


a = 10000
b = 12345

print(id(a))
print(id(b))
