
# 1번.
def myaverage(a, b):
    c = (a + b) / 2
    return c


# 2번.
def get_max_min(data_list):
    d1 = max(data_list)
    d2 = min(data_list)
    return (d1, d2)

# 3번.

import os

def get_txt_list(path):
    for x in os.listdir(path):
        if x.endswith('TXT'): # 제 컴퓨터에서 .txt가 아니라 TXT라서 이렇게 했습니다.
            print(x)
    
path = './dataset/titanic.csv'

# 4번

def bmi_cal(kg, cm):
    bmi = kg / ((cm/100)**2)
    if bmi < 18.5:
        print("마른체형")
    elif 18.5 <= bmi < 25.0:
         print("표준")
    elif 25.0 <= bmi < 30.0:
        print("비만")
    elif bmi >= 30.0:
        print("고도비만")

# 5번
def bmi_program():
    while 1:
        kg = int(input("몸무게를 입력하세요.(kg)"))
        m = int(input("키를 입력하세요.(cm)"))
        bmi = kg / ((m/100)**2)
        if bmi < 18.5:
            print("마른체형")
        elif 18.5 <= bmi < 25.0:
             print("표준")
        elif 25.0 <= bmi < 30.0:
            print("비만")
        elif bmi >= 30.0:
            print("고도비만")


# 6.
def get_triangle_area(width, height):
    face = width * height / 2
    return face

# 7.
def add_start_to_end(start, end):
    a = range(start, end+1)
    suma = sum(a)
    return suma

# 8.
list = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']
def first_three(list):
    lis = []
    for i in range(len(list)):
        lis.append(list[i][0:3])
    return lis


