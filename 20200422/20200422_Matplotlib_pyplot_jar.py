# Matplotlib 기본사용
"""
Matplotlib 라이브러리를 이용해서 그래프그리기
"""

#Pyplot소개
'''
matplotlib.pyplot은
Matplotlib을 MATLAB과 비슷하게 동작하도록 하는 명령어 스타일의 함수모음
각각의 pyplot하a수를 사용해 그림(figure)에 변화를 줄수있다
예) 그림을 만들어 플롯영역만들고, 몇개의 라인을 플롯하고 라벨들로 꾸미는 등 일을 할 수있다.
'''

#기본그래프
'''
pyplot으로 어떤 값들을 시각화는것은 매우간단함
pyplot.plot()에 하나의 리스트를 입력하면 그래프가 그려짐

'''

import matplotlib.pyplot as plt

#matplotlib은 리스트의 값들이 y값들이라고 가정하고 x값들([0,1,2,3])을 자동으로 만듬
plt.plot([0,1,2,3])
plt.ylabel('y-label')
plt.show()

'''
plot()은 다재다능한 명령어라 임의의개수의 인자를 받을 수 있음
예를들어 아래와 같이 입력하면 x와y값을 그래프로 나타낼 수 있음
'''

plt.plot([0,1,2,3],[1,5,10,25])

###########속성#############
#1) 스타일지정하기
'''
색상과 선의 형태를 지정하는 포맷문자열을 세번째 인자에 입력
디폴트 포맷문자열음 'b-' 파란색(b) 선(-)을 의미
ro는 빨간색(red) 원형(o)를 의미
'''
#카페 게시글(marker종류)내용 참조

plt.plot([0,1,2,3],[1,5,10,25],'ro') 

#2) axis()이용해 축의 [xmin, xmax,ymin, ymax]범위 지정
plt.axis([0,6,0,20]) #리스트 형식으로 묶어야함
plt.show()


#여러개의그래프 그리기
'''
matplotlib에서 리스트만 가지고 작업하는 것은 제한적이라
Numpy의 어레이 함수를 사용한다

사실, 모든시퀀스는 내부적으로 Numpy어레이로 변환됨
'''

#3) 다양한 포맷스타일의 여러개의 라인을 하나의 그래프로 그리기

import numpy as np

#200ms간격으로 균일한 샘플된 기간
t=np.arange(0.,5.,0.2)

#빨간대쉬, 파란사각형, 녹색삼각형
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()

#4) Matplotlib라벨설정하기
'''
xlabel(),ylabel()함수
그래프의 x,y축에 대한 라벨을 설정할 수 있음
'''
plt.plot([0,1,2,3],[1,5,10,25])
plt.xlabel('xLabel')
plt.ylabel('yLabel')
plt.show()

'''
axis()에 [xmin,xmax,ymin,ymax]의 형태로 x,y축의 범위를 지정
입력 리스트는 꼭 네개의 값 [xmin,xmax,ymin,ymax]이 있어야 한다.

입력값이 없으면 데이터에 맞게 자동(Auto)으로 범위를 지정.
'''

# Matplotlib 색깔 지정하기
# 자주 사용하는 색깔 외에도 다양한 색상을 지정할 수 있다.

import matplotlib.pyplot as plt

'''
plot()에 color = 'springgreen' 과 같이 입력해주면, springgreen에 해당하는 색깔이 지정된다.
'''

plt.plot([1,2,3,4], [1,4,9,16], color = 'springgreen')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.axis([0,5,0,20])
plt.show()

# Matplotlib 색깔 지정하기2
'''
16진수 코드(hex code)로도 색깔을 지정할 수 있다.
색깔, 마커와 선의 종류까지 모두 지정.
'''
import matplotlib.pyplot as plt
'''
색깔은 '#e35f62'와 같이 16진수로, 마커는 circle, 선 종류는 대쉬(dashed)로 지정
'''
plt.plot([1,2,3,4],[1,4,9,16], color='#e35f62', marker='o', linestyle='--')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.axis([0,5,0,20])
plt.show()

# Matplotlib 여러 곡선 그리기
# 세 개의 곡선을 하나의 그래프에 그리기.

import matplotlib.pyplot as plt
import numpy as np

'''
Numpy를 사용해서 array를 생성
numpy.arange()
주어진 간격에 따라 균일한 array를 생성한다.
'''

a = np.arange(5)
b = np.arange(1, 5)
c = np.arange(2, 10, 2)

print(a) # [0 1 2 3 4]
print(b) # [1 2 3 4]
print(c) # [2 4 6 8]

'''
array a는 [0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8]
'''
a = np.arange(0, 2, 0.2)

'''
plot() 에 x 값, y 값, 스타일을 순서대로 세 번씩 입력하면, 
세 개의 곡선(y=x, y=x^2, y=x^3)이 동시에 그려진다.
'''
plt.plot(a, a, 'r--',
         a, a**2, 'bo',
         a, a**3, 'g-.')
'''
'r-은' 빨간색(Red)의 대쉬(Dashed) 스타일 선,
'bo'는 파란색(Blue) 의 Circle 마커,
'g-.'은 녹색(Green)의 대쉬-닷(Dash-dot) 스타일 선을 의미.
'''
plt.show()

# 세 개의 곡선의 세세한 스타일을 설정할 수 있다.
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0, 2, 0.2)

# 첫 번째 곡선의 스타일은 'bo'로,
plt.plot(a, a, 'bo')

# 두 번째 곡선은 color='#e35f62', marker='*', linewidth=2로,
plt.plot(a, a**2, color='#e35f62', marker='*', linewidth = 2)

# 세 번째 곡선은 color='springgreen, marker='^', markersize=9로
plt.plot(a, a**3, color='springgreen', marker='^', markersize=9)


# Matplotlib 그리드와 틱 설정하기
'''
grid() 와 tick_params() 를 이용해서
그래프의 그리드와 틱의 스타일을 설정할 수 있다.
'''
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0, 2, 0.2)

plt.plot(a, a, 'bo')
plt.plot(a, a**2, color='#e35f62', marker='*', linewidth = 2)
plt.plot(a, a**3, color='springgreen', marker='^', markersize=9)

'''
그리드가 표시되도록 하려면,
grid() 의 첫 번째 파라미터를 True로 설정.

axis = 'y'로 설정하면 y 축의 그리드만 표시.

alpha는 투명도로 설정합니다.
0으로 설정하면 투명하게,
1은 불투명하게 표시

linestyle을 대쉬(Dashed)로 설정.
'''
plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')

'''
tick_params() 를 이용해서 그래프의 틱(Tick)에 관련된 설정을 할 수 있다.

axis='both' 로 설정하면 x,y축의 틱에 모두적용.

direction='in' 으로 틱의 방향을 그래프 안 쪽을 ㅗ설정.

틱의 길이(length)를 3만큼으로 하고,
틱과 라벨의 거리(pad)를 6만큼.
틱 라벨의 크기(labelsize)를 14로 설정.
'''
plt.tick_params(axis='both', direction='in', length=3, pad=6, labelsize=14)
plt.show()


# Matplotlib 타이틀 설정하기
# title() 을 이용해서 그래프의 제목(타이틀)을 설정.
'''
plt.title()을 이용해서 그래프의 타이틀을 'Sample graph'로 설정.
'''
plt.title('Sample graph')
plt.show()

# 2 - 위치와 오프셋
plt.title('Sample graph', loc = 'right', pad=20)
'''
loc ='right'로 설정하면,
타이틀이 그래프의 오른쪽 위에 나타나게 된다.

'left', 'center', 'right'로 설정할 수 있으며
디폴트는 'center'

pad = 20 은
타이틀과 그래프와의 간격(오프셋)을 포인트 단위로 설정.
'''

# 3- 폰트 설정
'''
fontdict 에 딕셔너리 형태로 폰트에 대한 설정을 입력할 수 있다.
'fontsize'를 16으로, 'fontweight'를 'bold'로 설정.

'fontsize'는 포인트 단위의 숫자를 입력하거나,
'smaller', 'x-large' 등의 상대적인 설정을 할 수 있다.

'fontweight'에는 'normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight'의
설정을 할 수 있다.
'''
title_font = {
    'fontsize':16,
    'fontweight':'bold'
    }
plt.title('Sample graph',fontdict=title_font, loc = 'left', pad=20)
