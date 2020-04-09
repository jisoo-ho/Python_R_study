# 1. 09/07 의 종가를 리스트의 첫 번째 항목으로 입력해서
# naver_closing_price라는 이름의 리스트를 만들어보세요.

naver_closing_price = [474500, 461500, 501000, 500500, 488500]
print(type(naver_closing_price))


# 1-2. 만든 naver_closing_price 를 이용해
# 해당 주에 종가를 기준으로 가장 높았던 가격을 출력하세요.

print(max(naver_closing_price))

# 1-3. 만든 naver_closing_price 를 이용해
# 해당 주에 종가를 기준으로 가장 낮았던 가격을 출력하세요.
print(min(naver_closing_price))

# 1-4. 만든 naver_closing_price 를 이용해
# 해당 주에서 가장 종가가 높았던 요일과
# 가장 종가가 낮았던 요일의 가격 차를 화면에 출력하세요.

print(max(naver_closing_price) - min(naver_closing_price))

# 1-5.  만든 naver_closing_price 를 이용해  수요일의 종가를 화면에 출력하세요.
print("수요일종가:", naver_closing_price[2])

# 1-6.  날짜를 딕셔너리의 키 값으로,  종가를 딕셔너리의 값으로 사용해
# naver_closing_price2 라는 딕셔너리를 만드세요.
naver_closing_price2 = {"09/07" : 474500, "09/08":461500,"09/09":501000,"09/10":500500,"09/11":488500 }
print(type(naver_closing_price2))

# 1-7.  naver_closing_price2 딕셔너리를 이용해
# 09/09 일의 종가를 출력하세요
print(naver_closing_price2["09/09"])


