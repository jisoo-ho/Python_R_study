import time 
print(time.time()) # 정수형태로 시간을 받아주는 함수 1586479561.056389


print(time.ctime()) # 보기 편한 형태로 출력 Fri Apr 10 09:46:01 2020

print(type(time.ctime())) # <class 'str'>


cur_time = time.ctime()
print(type(cur_time)) # <class 'str'>
print(cur_time) # Fri Apr 10 09:49:29 2020
print(cur_time.split(' ')[-1]) # 제일 뒤에꺼 하나만 잘라서 출력 #연도만 출력 (2020)
print(cur_time.split(' ')) # ['Fri', 'Apr', '10', '09:48:53', '2020']

print(type(cur_time))
