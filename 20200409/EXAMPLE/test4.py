ftemp = int(input("화씨온도: "))
ctemp = (ftemp-32.0)*5.0/9.0
print("섭씨온도 : ", ctemp)

weight = float(input("몸무게 입력 kg : "))
height = float(input("키 입력 m :"))

bmi = (weight / (height**2))
print("당신의 BMI = ", bmi)
