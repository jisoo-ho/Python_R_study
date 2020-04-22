# Numpy 난수 생성(Random 모듈)
# 난수 생성에 활용할 수 있는 Numpy의 random 모듈(numpy.random)

# 1- random.rand() : 주어진 형태의 난수를 생성.
import numpy as np

# 예제1
'''
만들어진 난수 array는 주어진 값에 의해 결정되며,
(0,1) 범위에서 귬일한 분포를 갖는다.
'''
a = np.random.rand(5)
print(a)
'''
결과 : [0.75004981 0.21139253 0.45048688 0.94381202 0.00407233]
'''

'''
random.rand() 주어진 형태의 난수 array를 생성

random.randint() [최저값, 최대값]의 범위에서 임의의 정수

random.randn() 표준정규분포(standard normal distribution)를 갖는 난수를 반환

random.standard_normal() : randn()과 standard_normal() 은 기능이 비슷하지만, 
                        standard_normal()은 튜플을 인자로 받는다는 점에서 차이가 있다.
                        
random.random_sample() : [0.0, 1.0) 범위의 임의의 실수를 반환
                          
random.choice() : 주어진 1차원 어레이에서 임의의 샘플을 생성

random.seed() : 난수 생성에 필요한 시드를 정한다. 코드를 실행할 때 마다 똑같은 난수가 생성
'''

# Matplotlib 산점도 그리기
# scatter() 를 이용해서 산점도(scatter plot)를 그릴 수 있다.

import matplotlib.pyplot as plt
import numpy as np
'''
np.random.seed() 를 통해서 난수 생성의 시드를 설정하면,
같은 난수를 재사용할 수 있다.

seed() 에 들어갈 파라미터는
0에서 4294967295 사이의 정수여야 한다.
'''
np.random.seed(19680801)


# 1 - random.rand() : 주어진 형태의 난수를 생성.
import numpy as np

'''
만들어진 난수 array는 주어진 값에 의해 결정되며,
[0, 1) 범위에서 균일한 분포를 갖는다. - 수학에서 [0,1) 로 쓰면 0은 포함되고 1은 포함되지 않는다는 의미
'''

a = np.random.rand(5)
print(a) # 결과 : [0.44859207 0.21580016 0.1010523  0.0087913  0.7022354 ]
    
b = np.random.rand(2, 3)
print(b)
'''
결과 : 
    [[0.70633485 0.24791576 0.15788335]
     [0.69769852 0.71995667 0.25774443]]
'''

'''
x, y의 위치, 마커의 색(colors)과 면적(area)을 무작위로 지정.

예를 들어, x는
[0.7000003, 0.721613,... , 0.234654, 0.3216541]으로
0에서 1사이의 무작위한 50개의 값을 갖는다.
'''

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

'''
scatter() 에 x, y 위치를 입력
s는 마커의 면적을,
c는 마커의 색을 지정.
alpla는 마커색의 투명도를 결정
'''
plt.scatter(x, y, s = area, c=colors, alpha=0.5) # x축 위치잡을 값, y 축 위치잡을 값을 반드시 만들어야 한다.
plt.show()

# Matplotlib 히스토그램 그리기
# hist()를 이용해서 히스토그램(histogram)을 그리기.

# 1- 값 입력하기

import matplotlib.pyplot as plt
'''weight 리스트는 몸무게 값을 나타낸다.'''
weight = [68,81,64,56,78,74,61,77,66,68,59,
          71,80,59,67,81,69,73,69,74,70,65]
''' hist()함수에 리스트의 형태로 값들을 직접 입력해주면 된다.'''
plt.hist(weight)

# 2 - 여러 개의 히스토그램 그리기
import matplotlib.pyplot as plt
import numpy as np

'''
Numpy의 np.random.randn() 와
np.random.standard_normal(), np.random.rand() 함수를 이용해서
임의의 값들을 생성.
'''

# array a는 표준편차 2.0, 평균 1.0을 갖는 정규분포
a = 2.0 * np.random.randn(10000) + 1.0

# array b 는 표준정규분포를 따른다.
b = np.random.standard_normal(10000)

# array c는 -10.0 에서 10.0 사이의 균일한 분포를 갖는 5000개의 임의의 값.
c = 20.0*np.random.rand(5000) - 10.0

'''
세 개의 분포를 동시에 그래프에 나타내기.
plt.hist()

bins는 몇 개의 영역으로 쪼갤지를 설정.

density=True 로 설정해주면,
밀도함수가 되어서 막대의 아래 면적이 1이 된다.

alpha는 투명도를 의미합니다. 0.0에서 1.0사이의 값을 갖는다.
histtype 을 'step'으로 설정하면 막대 내부가 비어있고,
'stepfilled'로 설정하면 막대 내부가 채워진다.
'''

plt.hist(a, bins=100, density=True, alpha=0.7, histtype='step')
plt.hist(b, bins=50, density=True, alpha=0.5, histtype='stepfilled')
plt.hist(c, bins=100, density=True, alpha=0.9, histtype='step')

plt.show()

import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(1000)
b = np.random.rand(10000)
c = np.random.rand(100000)

plt.hist(a, bins=100, density=True, alpha=0.5, histtype='step', label='n=1000')
plt.hist(b, bins=100, density=True, alpha=0.75, histtype='step', label='n=10000')
plt.hist(c, bins=100, density=True, alpha=1.0, histtype='step', label='n=100000')
plt.legend()

#----------정수반환
import matplotlib.pyplot as plt
import numpy as np

''' a는 [0,10) 범위의 임의의 정수 1000개'''
a = np.random.randint(0, 10, 1000)
''' b는 [0,10) 범위의 임의의 정수 1000개'''
b = np.random.randint(10, 20, 1000)
''' c는 [0,10) 범위의 임의의 정수 1000개'''
c = np.random.randint(0, 20, 1000)

plt.hist(a, bins=100, density=False, alpha=0.5, histtype='step', label='0<=randint<10')
plt.hist(b, bins=100, density=False, alpha=0.75, histtype='step', label='10<=randint<20')
plt.hist(c, bins=100, density=False, alpha=1.0, histtype='step', label='0<=randint<20')
plt.legend()
plt.show()
