### 1차원 리스트 #####
apart = [101, 102, 103, 104]
for i in apart:
    print("Newspaper delivery :", i)


#### 2차원 리스트 #####
apart2 = [[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]

print(type(apart2[0]))


for i in range(len(apart2)):
    for j in range(len(apart2)):
        if apart2[i][j] == 203:
            continue
        else:
            print("Newspaper delivery :", apart2[i][j])
