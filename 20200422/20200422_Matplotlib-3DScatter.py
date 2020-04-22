# Matplotlib 3차원 산점도 그리기
'''
scatter() 를 이용해서 3차원 산점도(3D Scatter plot)를 그리기.

3차원 그래프를 그리기 위해서
from mpl_toolkits.mplot3d import Axes3D 를 추가.

이 부분은 matplotlib 3.1.0 버전부터는
디폴트로 포함되기 때문에 적어주지 않아도 된다.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

'''
x, y의 위치, 마커의 색(colors)과 면적(area) 을 무작위로 지정.
'''
n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
cmin, cmax = 0, 2

xs = (xmax-xmin)*np.random.rand(n) + xmin
ys = (xmax-xmin)*np.random.rand(n) + ymin
zs = (xmax-xmin)*np.random.rand(n) + zmin
color = (xmax - xmin) * np.random.rand(n) + cmin

# rcParams 를 이용해서 figure의 사이즈를 설정
plt.rcParams["figure.figsize"] = (6,6) # 3차원 박스를 6분할로 나눈다.(가로, 세로)
fig = plt.figure()

'''
3D axes를 만들기 위해
add_subplot() 에 projection= '3d'키워드를 입력
'''
ax = fig.add_subplot(111, projection='3d')

'''
scatter() 함수에 x, y, z위치를 array의 형태로 입력
마커(marker)의 형태를 원형(circle)으로 설정
cmap = 'Greens'를 통해 colormap을 녹색 계열로 설정
'''

ax.scatter(xs, ys, zs, c=color, marker='o', s=15, cmap='Greens')
