import numpy as np

# concatenate
# - numpy array를 합치는 함수
a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
np.concatenate((a,b), axis = 0)
#array([[1, 2, 3],
#       [4, 5, 6]])

a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])
np.concatenate((a,b.T), axis=1 ) # a.T는 a의 역행렬 
#array([[1, 2, 5],
#       [3, 4, 6]])

# vstack 이랑 hstack은 같은 함수인데 axis로 결정된다.

'''Operations betwwn arrays'''
a = np.array( [[1,2,3], [4,5,6]], float)
a+a # matrix + matrix 연산
#array([[ 2.,  4.,  6.],
#       [ 8., 10., 12.]])

a-a # - 연산
#array([[0., 0., 0.],
#       [0., 0., 0.]])

a*a # matrix 내 요소들간 같은 위치에 있는 값들끼리 연산
#array([[ 1.,  4.,  9.],
#       [16., 25., 36.]])

'''이렇게 같은 index에 있는 것 끼리 더하고 빼고 곱해줘서 그 자리에 결과값을 넣어주는 연산 
= Element-wise Operation 이라고 한다.'''

# Dot product
# - matrix 의 기본 연산
# - dot 함수 사용

dot_a = np.arange(1, 7).reshape(2,3)
#array([[1, 2, 3],
#       [4, 5, 6]])

dot_b = np.arange(1, 7).reshape(3,2)
#array([[1, 2],
#       [3, 4],
#       [5, 6]])

dot_a.dot(dot_b)
# 행렬 연산식 적용 ( 2x3 행렬과 3x2 행렬의 곱)
#array([[22, 28],
#       [49, 64]])

t_matrix = np.array( [[1,2], [3,4]], float)
#array([[1., 2.],
#       [3., 4.]])

scalar = 2

t_matrix + scalar # matrix, scalar 덧셈 ( 모든 값에 2를 더한다 )
#array([[3., 4.],
#       [5., 6.]])

# - scalar - matrix 외에도, vector - matrix간의 연산도 지원
t_matrix = np.arange(1,13).reshape(4,3)
t_vector = np.arange(100, 400, 100)
t_matrix + t_vector
#array([[101, 202, 303],
#       [104, 205, 306],
#       [107, 208, 309],
#       [110, 211, 312]])

# All, Any
# - All : array의 데이터가 전부 조건에 만족하면 True
# - Any : array의 데이터 중 하나라도 조건에 만족하면 True
a = np.arange(5)
a
#array([0, 1, 2, 3, 4])

np.all(a>3)
# False
np.all(a<5)
# True
np.any(a>3)
# True
np.any(a>5)
# False

'''all은 말 그대로 모든 조건 만족하면 true가 나오고, any는 하나라도 만족하면 true를 추출해내는 함수이다.'''

a = np.array( [1,5,3], float)
b = np.array( [4,7,2], float)
a>b
#array([False, False,  True])
a==b
#array([False, False, False])
(a>b).any()
#True
(a>b).all()
#False

'''조건을 2개 이상 달고싶은 경우에 사용'''
a = np.array( [2,3,1], float)
np.logical_and(a > 0, a < 3 ) # and 조건의 비교
#array([ True, False,  True])

b = np.array( [False, True, True], bool)
np.logical_not(b) # not 조건의 비교
#array([ True, False, False])

c = np.array([False, False, False], bool)
np.logical_or(b,c) # or 조건의 비교(하나라도 맞으면 True, 모두 틀리면 False)
#array([False,  True,  True])

# logical_and는 한번에 두 가지 조건을 넣을 수 있다.


'''np.where'''
# - where(조건, True, False)

a = np.array( [2,3,1], float)
np.where(a > 1, 0, 3)
#array([0, 0, 3])

a = np.arange(3,10)
np.where(a>6) # True값의 index 반환
#(array([4, 5, 6], dtype=int64),)

a = np.array( [2, np.NaN, np.Inf], float) 
# 데이터가 NaN 들어간 값이랑 Inf 들어간 값. NaN은 널값 입력해주는 상수, Inf는 무한대값을 넣어주는 상수

np.isnan(a)
#array([False,  True, False])

np.isfinite(a) # 한정된 수인 경우 True
#array([ True, False, False])

# np.where은 우리가 생각하는 if문의 역할을 한다.

'''
isnan은 null값인 경우에만 true가 나온다.
np.NaN은 numpy 의 null값을 입력하는 함수이고, null값이니까 True

np.Inf는 무한대이다.

np.isinfite()는 한정된 수의 경우 True가 나오고
한정되지 않은 NaN이나 Inf의 경우에는 False가 나온다.
'''

'''argmax, argmin'''
# - array 내 최대값 또는 최소값의 index 반환
a = np.array( [2,3,1,5,6,22,11])
np.argmax(a), np.argmin(a)
#(5, 2)

# -axis 기반의 반환
a = np.array( [[1,4,2,22], [45,32,4,7], [34,54,9,8]])
np.argmax(a,axis=0), np.argmin(a, axis=1) # 0번(열 기준), 1번(행 기준)
#(array([1, 2, 2, 0], dtype=int64), array([0, 2, 3], dtype=int64))
# 첫 번째 열에서 가장 큰 값 45(1번 인덱스)-컬럼
# 첫 번째 행에서 가장 작은 값 1(0번 인덱스)-로우, 두번째 행에서 가장 작은값 4(2번 인덱스) - 로우

'''boolean index '''
# -numpy의 배열은 특정 조건에 따른 값을 배열 형태로 추출 가능
# -comparison operation 함수들도 모두 사용 가능
t_a = np.array( [3,5,8,0,7,4], float)
t_a > 4
#array([False,  True,  True, False,  True, False])

t_a[t_a>4] # 조건이 True인 index 의 요소값만 추출
#array([5., 8., 7.])

t_c = t_a <4
t_c
# array([ True, False, False,  True, False, False])

t_a[t_c] 
#array([3., 0.])
