'''
Numpy란 Numerical Python 의 약자로
대규모 다차원 배열과 행렬 연산에 필요한 다양한 함수를 제공한다.
데이터 분석할 때 사용되는 다른 라이브러리 pandas와 matplotlib의 기반이 된다.
기본적으로 array라는 단위로 데이터를 관리하는데, 행렬 개념으로 생각하면 된다.

- numpy 특징 : 일반 list에 비해 빠르고 메모리에 효율적이다.
선형대수와 관련된 다양한 기능을 제공하고,
for문, while문 같은 반복문 없이 데이터 배열에 대한 처리를 지원한다.

 - numpy가 빠른 이유 : numpy는 메모리에 차례대로 생성/할당을 해준다.
 반면 기존의 List는 이 값(value)가 어디에 있는지 주소만 저장을 해놓고 그 주소를 알려준다.
 그래서 list를 for문을 돌리면 그 주소마다 하나하나씩 다 찾아가면서 연산을 해줘야 하는데,
 (파이썬은 변수형태로 들어가고 numpy는 메모리를 직접관리)
 numpy는 같은 곳에 몰려 있기 때문에 연산이 더 빠르게 이뤄진다.
 
  --> 넘파이는 데이터들을 한군데 차곡차곡 모아서 관리하는게 특징이다. 그러나 파이썬의 리스트는
  데이터가 있는 번지수가 있어서 그 변수. 즉, 주소들만 기억하고 실제로 찾아내려면 그 번지를 이용해서 찾아다녀야 한다.
  
 - numpy 호출 : "import numpy as np"로 numpy를 호출하는데 모두 np라는 별칭(alias)로 호출하지만 특별한 이유는 없다.
 - numpy로 array 생성하는 방법 : ex)test_array = np.array([1,3,5,7], float)
  type(test_array[3])을 하면 4바이트씩 numpy.float64 라는 값이 반환된다.
  float32 같은 데이터 타입은 하나씩 모여서 메모리 블럭을 구성한다.
  32bit(비트) = 4byte(바이트)이다. (8bit 가 1byte)
'''
import numpy as np

test_array = np.array([1,3,5,7], float)
print(test_array) # [1. 3. 5. 7.]
print(type(test_array)) # <class 'numpy.ndarray'>

'''
ndarray의 구성 -> (4,)
ndarray의 shape : (type : tuple)
이건 1차원 벡터형식이라고 부른다.

vector는 1차원 행렬을 말하고 하나의 행에 열만 있는 것이다.
(위의 그림 예시에서는 1차원에 4개의 element만 있음)
각 숫자는 value(요소)라고도 부른다.
shape를 보는 코드 예시는 그림 상에 없지만 결과적으로 (4,)의 결과를 보여줄 것이다.
'''

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
matrix2 = np.array(matrix, int).shape # (3, 4)
type(matrix2) # tuple
type(matrix) # list

tensor = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]]]

type(tensor) # list
np.array(tensor, int).shape # (3, 3, 4)
# 3차원 matrix, nparray의 shape(type : tuple)

np.array(tensor, int).ndim # number of dimension
# 3
np.array(tensor, int).size # data의 개수
# 36

'''
- Ndarray의 single element가 가지는 data type
- 각 element가 차지하는 memory의 크기가 결정됨
'''
np.array( [[1,2.6, 3.2], [4, 5.1, 6]], dtype=int)
#array([[1, 2, 3],
#       [4, 5, 6]])

np.array( [[1,2.6, 3.2], [4, "5", 6]], dtype=np.float32)
#array([[1. , 2.6, 3.2],
#       [4. , 5. , 6. ]], dtype=float32)

'''
각 요소마다 데이터 타입을 지정해주면 그 데이터 타입으로 변환이 되는 걸 볼 수 있다.

아래의 예시를 보면 여기는 실수형이고 여기는 string 타입인데 소수점 타입으로 바꾸면
???????????????????????????????????????????????????????????????????????????????
'''

# - nbyte : ndarray object의 메모리 크기 리턴

np.array([[1, 2.6, 3.2], [4, "5", 6]], dtype=np.float32).nbytes
# 24 -> 32bits = 4bytes -> 6 * 4 bytes
np.array([[1, 2.6, 3.2], [4, "5", 6]], dtype=np.float64).nbytes
# 48 -> 64bits = 8bytes -> 6 * 8 bytes
np.array([[1, 2.6, 3.2], [4, "5", 6]], dtype=np.int8).nbytes
# 6 -> 8bits = 1 bytes -> 6 * 1bytes


'''
하나의 value가 4바이트를 가지는데
요소가 6개 있으니까, 이게 메모리에서 차지하는 건 총 24바이트가 된다.
그 다음 타입은 하나가 8바이트이니까 48바이트를 차지한다.
'''

# - Array의 크기를 변경함(element의 개수는 동일)
t_matrix = [[1,2,3,4], [5,6,7,8]]
np.array(t_matrix).shape
#(2, 4)
np.array(t_matrix).reshape(8,)
#array([1, 2, 3, 4, 5, 6, 7, 8]) --> 2행으로 되어있는 것을 1행으로 변경하였다.
np.array(t_matrix).reshape(8,).shape
#(8,)


# - Array의 size만 같다면 다차원으로 자유로이 변형 가능
np.array(t_matrix).reshape(2, 4).shape
#(2, 4)
np.array(t_matrix).reshape(-1, 2).shape # -1 을 입력하면 알아서 행 갯수를 맞춰준다.
#(4, 2)
np.array(t_matrix).reshape(2,2,2)
#array([[[1, 2],
#        [3, 4]],
#       [[5, 6],
#        [7, 8]]])
np.array(t_matrix).reshape(2,2,2).shape
#(2, 2, 2)

# flatten : 다차원 array를 1차원 array로 변환
t_matrix = [ [[1,2], [3,4]], [[1,2], [3,4]], [[1,2],[3,4]]]
np.array(t_matrix).flatten()
# array([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])

# flatten : 다차원을 1차원으로만 만들어 주는 함수. 즉, reshape은 최소화할 열이나 행 둘중에 하나를 뿌려줘야 하는데 flatten은 1차원으로만됨

# indexing
a = np.array([[1,2.2,3], [4,5,6.3]],int)
print(a)

#[[1 2 3]
# [4 5 6]]

print(a[0,0]) # 1
print(a[0][0]) # 1
a[0,0]=7
print(a)
#[[7 2 3]
# [4 5 6]]

# slicing
# - list와 달리 행과 열 부분을 나눠서 slicing 이 가능함
# - matrix 부분 집합 추출할 때 유용
a = np.array([[1,2,3,4,5],[6,7,8,9,10]],int)
a[:,1:] # 전체 row의 1열 이상
#array([[ 2,  3,  4,  5],
#       [ 7,  8,  9, 10]])

a[1, 2:4] # 1row의 2~3열
#array([8, 9])

a[1:3] #1row ~ row 전체
#array([[ 6,  7,  8,  9, 10]])

a = np.array([[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14]], int)
print(a)
#[[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]]

a[:,::2] # 행과 열은 내부 인덱스를 뽑는거고, 두 번째는 위치를 뽑는것
#array([[ 0,  2,  4],
#       [ 5,  7,  9],
#       [10, 12, 14]])

a[::2,::2] # ::은 스텝(간격)을 의미한다.
#array([[ 0,  2,  4],
#       [10, 12, 14]])

#배열을 만드는데 범위를 지정해서 만드는 방법
# - array의 범위를 지정하여, 값의 list를 생성하는 명령어

np.arange(20)#list의 range와 같은 역할, intege로 0부터 19까지 배열 추출
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

np.arange(0, 1, 0.2) #float 가능
#array([0. , 0.2, 0.4, 0.6, 0.8])

np.arange(20).reshape(4,5) # 만든 값을 reshape한다.
#array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14],
#       [15, 16, 17, 18, 19]])

np.zeros(shape = (5,2), dtype = np.int8) # 5 by 2 zero matrix 생성, int8
#array([[0, 0],
#       [0, 0],
#       [0, 0],
#       [0, 0],
#       [0, 0]], dtype=int8)

np.ones(shape = (5,2), dtype = np.int8) # 5 by 2 one matrix 생성, int8
#array([[1, 1],
#       [1, 1],
#       [1, 1],
#       [1, 1],
#       [1, 1]], dtype=int8)

np.empty(shape=(3,2), dtype=np.int8)
#array([[1, 2],
#       [3, 4],
#       [5, 6]], dtype=int8)
# 실행할 때 마다 다른 값이 출력된다.

'''
empty는 주어진 shape대로 비어있는 것을 생성한다.
이런 식으로 array를 만드는데 메모리를 어느 정도 할당 시켜준다.
그런데 메모리에 기존에 있었던 값을 보여준다.

zeros나 ones는 0과 1로 메모리 할당 값을 초기화 시켜주는데
empty는 초기화시키지 않고 기존에 메모리에 있는 찌꺼기 그대로 보여준다.
'''

#기존 ndarray의 shape 크기만큼 1 or 0 or empty array 반환
t_matrix = np.arange(15).reshape(3,5)
np.ones_like(t_matrix) # 채워져있는 구조를 이용해서 1로 바꾼 것, 원본 반영되는게 아님
#array([[1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1]])

t_matrix1 = np.arange(15).reshape(3,5)
np.zeros_like(t_matrix1) # 채워져있는 구조를 이용해서 0으로 바꾼 것, 원본 반영되는게 아님
#array([[0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0]])

t_matrix2 = np.arange(15).reshape(3,5)
np.empty_like(t_matrix2)
#array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])


# 단위행렬 (i행렬)을 생성 n -> number of rows
np.identity(n=3, dtype=np.int8)
#array([[1, 0, 0],
#       [0, 1, 0],
#       [0, 0, 1]], dtype=int8)

np.identity(n=5) #정사각형 행렬
#array([[1., 0., 0., 0., 0.],
#       [0., 1., 0., 0., 0.],
#       [0., 0., 1., 0., 0.],
#       [0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 1.]])

np.eye(N=3, M=4, dtype=np.int) # N값과 M 값을 변경시켜서 직사각형 형태로 만들 수 있다.
#array([[1, 0, 0, 0],
#       [0, 1, 0, 0],
#       [0, 0, 1, 0]])

np.eye(4) # identity행렬과 같게 출력
#array([[1., 0., 0., 0.],
#       [0., 1., 0., 0.],
#       [0., 0., 1., 0.],
#       [0., 0., 0., 1.]])

np.eye(3, 6, k=3) # k --> start index
# 기준 열에서 1을 시작점으로 찍는 옵션(3칸 건너 뛰고 시작한다.)
#array([[0., 0., 0., 1., 0., 0.],
#       [0., 0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 0., 1.]])


'''행렬 중 대각선 값만 뽑아내는 함수'''
t_matrix = np.arange(16).reshape(4,4)
np.diag(t_matrix)
# array([ 0,  5, 10, 15])

np.diag(t_matrix, k=1) # k옵션은 출력하는 열의 시작 위치를 나타낸다.
# array([ 1,  6, 11])

'''Random Sampling'''
# 정규분포 만들어주는 함수
np.random.uniform(0,1,12).reshape(4,3) # 균등분포
# np.random.uniform(최소값, 최대값, 데이터 개수)
#array([[0.39422635, 0.83574142, 0.10830835],
#       [0.33941921, 0.97021726, 0.91356626],
#       [0.9100399 , 0.8243246 , 0.85169551],
#       [0.48654262, 0.15473669, 0.8773488 ]])


np.random.normal(0,1,12).reshape(4,3) # 정규분포
# np.random.normal(평균 0, 표준편차 1에 해당하는 12개)를 뽑으라는 의미
#array([[ 0.29332096, -0.05565469, -0.04275069],
#       [ 0.15716903, -0.50732937, -0.12142198],
#       [ 1.42172159,  0.29410614, -2.32252451],
#       [ 1.44995498, -0.75131102,  0.35022273]])

'''axis'''
# - 모든 operation function 을 실행할 때, 기준이 되는 dimension 축
# 집계연산을 할 때 어떤 축을 기준으로 집계연산을 해달라는 의미
t_array = np.arange(1,13).reshape(3,4)
t_array
#array([[ 1,  2,  3,  4],
#       [ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])

t_array.sum(axis = 0), t_array.sum(axis=1) # 0방향이 컬럼(세로) 방향, 1방향이 로우(가로)
#(array([15, 18, 21, 24]), array([10, 26, 42]))

# - 모든 operation function 을 실행할 때, 기준이 되는 dimension 축
tensor = np.array([t_array, t_array, t_array])
tensor

# array([[[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],
# 
#        [[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],
# 
#        [[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]]])

t_array = np.arange(1, 13).reshape(3,4)
t_array
#array([[ 1,  2,  3,  4],
#       [ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])

t_array.mean(), t_array.mean(axis=0)
#(6.5, array([5., 6., 7., 8.]))

t_array.std(), t_array.std(axis=0) # 표준편차를 만드는 함수 .std 
#(3.452052529534663, array([3.26598632, 3.26598632, 3.26598632, 3.26598632]))


'''Mathmatical functions'''
# 각각의 값을 찾아가면서 하나씩 찾는 것을 '브로드캐스팅'이라고 한다.

np.exp(t_array) # 지수함수
#array([[2.71828183e+00, 7.38905610e+00, 2.00855369e+01, 5.45981500e+01],
#       [1.48413159e+02, 4.03428793e+02, 1.09663316e+03, 2.98095799e+03],
#       [8.10308393e+03, 2.20264658e+04, 5.98741417e+04, 1.62754791e+05]])

np.sqrt(t_array) # 루트
#array([[1.        , 1.41421356, 1.73205081, 2.        ],
#       [2.23606798, 2.44948974, 2.64575131, 2.82842712],
#       [3.        , 3.16227766, 3.31662479, 3.46410162]])

np.sin(t_array) # sin 함수
#array([[ 0.84147098,  0.90929743,  0.14112001, -0.7568025 ],
#       [-0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825],
#       [ 0.41211849, -0.54402111, -0.99999021, -0.53657292]])

a = np.array([1,2,3])
b = np.array([4,5,6])
np.vstack((a,b))
#array([[1, 2, 3],
#       [4, 5, 6]])

a = np.array([ [1], [2], [3]])
b = np.array([ [4], [5], [6]])
np.hstack((a,b)) # ※ 주의 : 2차원 배열로 되어있어야 옆으로 붙는다.
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
