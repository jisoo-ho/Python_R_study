x1 = int(input("시작 값을 입력하세요(숫자) : "))
x2 = int(input("끝 값을 입력하세요(숫자) : "))

x3 = list(range(x1, x2+1))

for i in range(len(x3)):
    if x3[i] % 2 != 0:
        print(x3[i])


num = 0
while 1:
    print(num, "test1")
    if num == 10:
        break
    num += 1

num2 = 0
while num2 < 10:
    num2 += 1
    if num2 == 5:
        continue
    print(num2, "test2")
