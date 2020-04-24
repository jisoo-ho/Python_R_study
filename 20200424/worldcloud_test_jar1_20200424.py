'''
### gensim ###
text 데이터들의 topic modelling 하는 라이브러리. 
즉 topic modelling 에 대한 여러가지 기능이 구현되어 있다.

topic model (topic은 주제라는 뜻.)
예를 들면 
"트와이스는 너무 좋고 나는 모모를 좋아 한다. "  라는 문장이 있으면 
이 문장의 주제는 트와이스 혹은 모모 일것이다. 
그것은 관점에 따라 좀 다른데 
일반적으로 사람은 이 문장의 주제가 무엇일까? 라고 질문하면 
트와이스 라고 이야기 할 관점이 크고 
그다음에 "트와이스 멤버의 모모" 라고 이야기 하는사람도 있을 것이다.
이런식으로 텍스트 데이터 집단에서 해당 텍스트 집단들의 주제를 추출할수 있거나 
만들수 있는 모델을 topic modelling 이라고 할수 있다.

##### 한글 자연어 처리 기초
# Kkma
from lib2to3.btm_utils import tokens
from konlpy.tag import Kkma
kkma = Kkma()

print(kkma.sentences('한국어 분석을 시작합니다~ 너를 만나~~ 참 행복했어~~'))
print(kkma.nouns('한국어 분석을 시작합니다~ 모든 날 ~ 모든 순간 ~~~ 함께 해~~'))
print(kkma.pos('한국어 분석을 시작합니다 노래 시작했다 노래 끝났다!'))
'''
'''
# Hannanum
from konlpy.tag import Hannanum
hannanum = Hannanum()

print(hannanum.nouns('한국어 분석을 시작합니다 재밌어용~'))
print(hannanum.morphs('한국어 분석을 시작합니다 안녕하세요'))
print(hannanum.pos('한국어 분석을 시작합니다 건강하세요 ~'))

'''
'''
# Twitter
from konlpy.tag import Okt
t = Okt()

print(t.nouns('한국어 분석을 시작합니다 재밌어용~'))
print(t.morphs('한국어 분석을 시작합니다 안녕하세요'))
print(t.pos('한국어 분석을 시작합니다 건강하세요 ~'))


'''
'''

# Komoran
from konlpy.tag import Komoran
k = Komoran()

print(k.nouns('한국어 분석을 시작합니다 재밌어요오~~'))
print(k.morphs('한국어 분석을 시작합니다 안녕하세요~~'))
print(k.pos('한국어 분석을 시작합니다 메롱~~'))

'''


'''
import time #성능 비교하려면 누가 빨리 끝나는지 알아야 하니까 타임 라이브러리
from konlpy.tag import Hannanum, Kkma, Komoran, Okt


# 성능 비교
sentence = u'감정노동자 보호법은 사업주로 하여금 감정노동으로부터 근로자를 보호하는 예방 조치를 이행하도록 강제한다.\
다만 현장 근로자들을 중심으론 이 같은 법안이 현장에 제대로 적용되기 위해서는 회사의 수직적 위계 구조와 인력 부족 문제 등\
구조적 문제가 우선 해결돼야 한다는 지적도 나온다.'

sentences = [sentence] * 100 # 성능평가 하려면 만개 정도는 넣어야 하는데 일단 테스트로 100개!


morphs_processors = [('Hannanum', Hannanum()),
                      ('Kkma', Kkma()),
                      ('Komoran', Komoran()),
                      ('Okt', Okt())]

for name, morphs_processor in morphs_processors:
    start_time = time.time()
    morphs = [morphs_processor.morphs(sentence) for sentence in sentences]
    elapsed_time = time.time() - start_time
    print('morphs_processor name = %20s, %.5f secs' % (name, elapsed_time))
'''
    
'''
빠른 속도와 보통의 정확도를 원한다면 Komoran / Hannanum
속도는 느리더라도 정확하고 상세한 품사 정보 원하면 Kkma
어느 정도 띄어쓰기 되어있는 인터넷 영화평/상품명 처리시 Okt 
(만약 띄어쓰기 없다면 느린 처리 속도는 감수해야함)
'''


# 워드 클라우드
# WordCloud 설치 : pip install wordcloud

from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import Image

'''
언어를 분석할 떄, stopwords 라는 용어가 나온다
stopwords 또는 불용어 란, 우리가 언어를 분석할 때,
의미가 있는 단어와, 의미가 없는 단어나 조사 등이 있다.
이렇게 의미가 없는 것들을 stopwods 라고 한다.

예) 다음 문장이 있다.
    "Family is not an important thing. It's everything."

Family, important, thing, everything 은 의미가 있다고 보고
나머지 아래 같은 것들은 의미가 없다 판단하여
stopwords로 정의한다.

'''
'''
# alice.txt
text = open('c:/python_data/09. alice.txt').read()
alice_mask = np.array(Image.open('c:/python_data/09. alice_mask.png'))

stopwords = set(STOPWORDS)
stopwords.add("said")
'''

# 워드 클라우드 폰트 설정
import matplotlib.pyplot as plt
import platform
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~')

'''
plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

wc = WordCloud(background_color = 'white',
               max_words = 2000,
               mask = alice_mask,
               stopwords = stopwords)
wc = wc.generate(text)


# wc.words_
plt.figure(figsize = (12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
'''

# a_new_hope.txt
text = open('./data/09. a_new_hope.txt').read()

text = text.replace('HAN', 'Han')
text = text.replace("LUKE'S", 'Luke')

mask = np.array(Image.open('./data/09. stormtrooper_mask.png'))

stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words = 1000,
               mask = mask,
               stopwords = stopwords,
               margin =10,
               random_state=1).generate(text)

default_colors = wc.to_array()



import random

def gray_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return 'hsl(0, 0%%, %d%%)' % random.randint(60, 100)

plt.figure(figsize=(12, 12))

plt.imshow(wc.recolor(color_func=gray_color_func, random_state=3), interpolation='bilinear')

plt.axis('off')
plt.show()

