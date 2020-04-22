# Marplotlib 막대그래프 그리기
'''
bar() 함수를 이용해서 막대 그래프(bar graph)를 그릴 수 있다.
연도별 값을 갖는 데이터를 막대 그래프로 플롯.
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)

# years는 x축에 표시될 연도이고, values는 y값.
years = ['2017', '2018', '2019']
values = [100, 400, 900]

# 먼저 bar() 함수에 x(=[0, 1, 2])와 값(=[100, 400, 900])을 입력.
plt.bar(x, values)
values = [100, 400, 900]

# 먼저 bar() 함수에 x(=[0,1,2])와 값(=[100,400,900])을 입력.
plt.bar(x, values)

'''
xticks()에 x와 years를 입력해주면,
x축에 '2017', '2018', '2019'가 순서대로 표시된다.

'''
plt.xticks(x,years)
plt.show()

'''
막대그래프에도
막대와 테두리의 색, 두께 등 다양한 스타일을 적용할 수 있다.

우선 bar() 함수에 x, y(=values)값을 입력.
'''

plt.bar(x, values,
        width=0.6,
        align='edge',
        color='springgreen',
        edgecolor='gray',
        linewidth=3,
        tick_label=years,
        log=True)

'''
barh()를 이용하면 수평 막대 그래프를 그릴 수 있다.
'''
y = np.arange(3)
plt.barh(y,values,
         height=-0.6,
         color='springgreen',
         edgecolor='gray',
         linewidth=3,
         tick_label=years,
         log=False)
plt.show()

# https://matplotlib.org/contents
# 여기서 필요한 모양의 그래프들과 소스를 확인 및 다운할 수 있다.


