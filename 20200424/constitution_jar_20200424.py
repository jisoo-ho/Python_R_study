###################################################
# 한국어 자연어 처리 Kkma / KoNLPy 코엔엘파이
# KoNLPy 코엔엘파이 
###################################################


# 꼬꼬마에 대하여
from konlpy.corpus import kolaw
from konlpy.tag import Kkma
from konlpy.utils import concordance

# 헌법 관련된 텍스트 불러오기
constitution = kolaw.open('./constitution.txt').read()

print(constitution)

# 몇번째 줄에 '민주'라는 단어가 있는지 찾아줌
r = concordance(u'민주', constitution, show=False)
print("show=False => ", r)

# show=False => 문장으로 안나타나고
# show=True => 문장으로 나타남


# 텍스트 마이닝 작업 시 고려사항 : 정확성, 속도
from konlpy.tag import Kkma # 정확성 때문에 Kkma 사용, 맨 처음 시작시 시간이 좀 걸림 (variable들 날리면 더 걸림)
from konlpy.utils import pprint

kkma = Kkma()

text = u'네, 안녕하세요. 반갑습니다.'

# 문장 단위로 찾아냄
text_s = kkma.sentences(text)
print("text_s => ", text_s)

# 리스트에 담겨서 나옴
print("type(text_s) => ", type(text_s))
print("type_s[0] => ", text_s[0])
print("type_s[0] => ", text_s[-1])


# tagset : 형식들에 대한 정보 파악
kkma = Kkma()
print(kkma.tagset)

text = "자연어처리는 재미있습니다. \
        그러나 한국어 분석은 쉽지 않습니다."
        
# 명사 추출기, Noun extractor
text_nouns = kkma.nouns(text)
print(text_nouns)


# 형태소 해석, Parse phrase to morphemes
# 나중에 조사들을 추출해서 버리고
# 의미있는 것들만 분석에 활용한다

text_morphs = kkma.morphs(text)
print(text_morphs)


# POS태그
pos_tagger = kkma.pos(text)
print(pos_tagger)

print(len(pos_tagger))
print(type(pos_tagger))
print(type(pos_tagger[0]))



# flatten=False : 문장단위에 따라서 묶음이 달라짐
#                 True일 땐 하나하나 다 풀어서 저장
pos_tagger_f = kkma.pos(text, flatten=False)

print(pos_tagger_f)
print(len(pos_tagger_f))
print(type(pos_tagger_f))
print(type(pos_tagger_f[0]))


constitution = kolaw.open('./constitution.txt').read()
pos_const = kkma.pos(constitution)
print(len(pos_const))


# 보통 명사만 추출 -> 가나다 순
pos_const_NNG = [word[0] for word in pos_const if word[1] == 'NNG']
print(len(pos_const_NNG))

pos_const_NNG.sort()
print(pos_const_NNG[:10])
print(pos_const_NNG[-10:])


# 모든 명사 추출 (모든 명사들을 추출할 수 있는 약어 리스트)
NN_list = ['NN', 'NNB', 'NNG', 'NNM', 'NNP', 'NP']

# 모든 명사의 개수 파악하기
pos_const_NN = [word[0] for word in pos_const if word[1] in NN_list]
print(len(pos_const_NN))

pos_const_NN.sort()
print(pos_const_NN[:10])
print(pos_const_NN[-10:])


# set로 묶어서 unique한 값 찾
s = set(pos_const_NN)
print(len(s))


# 전체 데이터를 다 테스트하기 보다는 일부 데이터만 테스트를 먼저 진행하는 것이
# 개발 속도를 향상시킬 수 있음

# 문제) 어떤 단어가 몇개 있는지 for 구문으로 dict 타입으로 추가해주기
# 단어의 갯수 : 938
def getNounCnt(pos_list):
    noun_cnt = {}
    
    for noun in pos_list:
        if noun_cnt.get(noun):
            noun_cnt[noun] += 1
        else:
            noun_cnt[noun] = 1
            
    return noun_cnt

noun_dict = getNounCnt(pos_const_NN)
print(len(noun_dict), noun_dict)



from collections import Counter

# most_common : 의미있는 것을 찾기 위해 명사들 중 가장 많이 나온 것들만 뽑아내기

counter = Counter(pos_const)
print(counter.most_common(10))



##################################################################
# 육아휴직 관련 법안 대한민국 국회 제 1809890호 의안

import nltk

from konlpy.corpus import kobill

# 텍스트 파일은 kobill 내부에 있음
# 법안 관련 파일 8-9개 정도 들어있

files_ko = kobill.fileids()
doc_ko = kobill.open('1809890.txt').read()

doc_ko

# Twitter
from konlpy.tag import Okt
import matplotlib.pyplot as plt

t = Okt()
tokens_ko = t.nouns(doc_ko)
tokens_ko

ko = nltk.Text(tokens_ko, name='대한민국 국회 의안 제 1809890호')

print(len(ko.tokens))
print(len(set(ko.tokens)))
ko.vocab()

# chart 1
plt.figure(figsize=(12, 6))
ko.plot(50)
plt.show()

# 한글자씩 나오는 데이터 처리 // 필요없는 단어도 처리 
stop_words = ['.', '(', ')', ',', "'", '%', '-', 'X', ').', 'x', '의', '자', '액', '제', '월', '수', '중', '것', '표', '명', '및',
             '법', '생', '략', '에', '안', '번', '호', '을', '이', '다', '만', '로', '가', '를', '세', '위', '정', '항', '함', '음',
             '따라서', '일부', '해당', '현재', '다음', '인']
    
ko = [each_word for each_word in ko if each_word not in stop_words]
ko

# chart 2
ko = nltk.Text(ko, name='대한민국 국회 의안 제 1809890호')

plt.figure(figsize=(12, 6))
ko.plot(50)
plt.show()

# chart 3
ko.count('초등학교')

plt.figure(figsize=(12, 6))

ko.dispersion_plot(['육아휴직', '초등학교', '공무원'])

ko.concordance('초등학교')

data = ko.vocab().most_common(150) #노출빈도수 만들고 상위 150개 데이터를 튜플 리스트로 반환


# wordcloud
# for mac : font_path='/Library/Fonts/AppleGothic.ttf'
from wordcloud import WordCloud

wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
                      relative_scaling=0.2,
                      background_color='white',).generate_from_frequencies(dict(data))

plt.figure(figsize=(12, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



