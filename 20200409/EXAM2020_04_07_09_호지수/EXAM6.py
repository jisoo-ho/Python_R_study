# 1. *****패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

print("1번답")
for i in range(5):
    print("*", end="")


# 2. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.
print("\n2번답")
for i in range(4):
    print("\n")
    for j in range(5):
        print("*", end="")

# 3. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.
#*
#**
#***
#****
#***** 

print("\n3번답")

for i in range(6):
    print("*"*i)


# 4. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

#*****
#****
#***
#**
#*
print("\n4번답")
for i in range(5):
    for j in range(5-i):
        print("*", end="")
    print()



# 5. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

#    *
#   **
#  ***
# ****
#*****
print("\n5번답")
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()



# 6. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

#*****
# ****
#  ***
#   **
#    *

print("\n6번답")
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(5-i):
        print("*", end="")
    print()



# 7. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
# 위로 솟은 트리(5단)

print("\n7번답")
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for j in range(2*(i+1)-1):
        print("*", end="")
    print()

# 8. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
# 아래로 솟은 트리(5단)

print("\n8번답")
for j in range(5):
    for i in range(j):
        print(' ', end='')
    for i in range(2*(5-j)-1):
        print('*', end='')
    print("") 
 


# 9. 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for i in apart:
    for j in i:
        if j in arrears:
            continue
        else:
            print("Newspaper delivery :", j)

