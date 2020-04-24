# Naive Bayes Classifier의 이해 - 한글
# 문장의 유사도 측정
'''
'메리가 좋아'
'고양이도 좋아'
'난 수업이 지루해'
'메리는 이쁜 고양이야'
'난 마치고 메리랑 놀거야'
'''

from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk

pos_tagger = Okt()

train = [('메리가 좋아', 'pos'),
         ('고양이도 좋아', 'pos'),
         ('난 수업이 지루해', 'neg'),
         ('메리는 이쁜 고양이야', 'pos'),
         ('난 마치고 메리랑 놀거야', 'pos')]


all_words = set(word.lower()
                for sentence in train # sentence : '메리가 좋아'
                for word in word_tokenize(sentence[0])) # tokenize : 쪼개다! 분리하다! / word : '메리가', '좋아'

all_words
type(all_words) # set

print(all_words)
#{'수업이', '이쁜', '메리랑', '고양이도', '좋아', '놀거야', '마치고', '메리는', '난', '메리가', '고양이야', '지루해'}


t = [({word: (word in word_tokenize(x[0]))
        for word in all_words}, x[1]) for x in train]    # 원래는 붙여써야함!

type(t) # list
type(t[0]) # typle
type(t[0][0]) # dict


t
print(t)
'''
[({'수업이': False, '이쁜': False, '메리랑': False, '고양이도': False, '좋아': True, '놀거야': False, '마치고': False,
   '메리는': False, '난': False, '메리가': True, '고양이야': False, '지루해': False}, 'pos'),
 ({'수업이': False, '이쁜': False, '메리랑': False, '고양이도': True, '좋아': True, '놀거야': False, '마치고': False,
   '메리는': False, '난': False, '메리가': False, '고양이야': False, '지루해': False}, 'pos'),
 ({'수업이': True, '이쁜': False, '메리랑': False, '고양이도': False, '좋아': False, '놀거야': False, '마치고': False,
   '메리는': False, '난': True, '메리가': False, '고양이야': False, '지루해': True}, 'neg'),
 ({'수업이': False, '이쁜': True, '메리랑': False, '고양이도': False, '좋아': False, '놀거야': False, '마치고': False,
   '메리는': True, '난': False, '메리가': False, '고양이야': True, '지루해': False}, 'pos'),
 ({'수업이': False, '이쁜': False, '메리랑': True, '고양이도': False, '좋아': False, '놀거야': True, '마치고': True,
   '메리는': False, '난': True, '메리가': False, '고양이야': False, '지루해': False}, 'pos')]
'''

classifier = nltk.NaiveBayesClassifier.train(t)
type(classifier) # nltk.classify.naivebayes.NaiveBayesClassifier
#<nltk.classify.naivebayes.NaiveBayesClassifier at 0x226383da888>

classifier.show_most_informative_features()
'''
 classifier.show_most_informative_features()
Most Informative Features
                       난 = True              neg : pos    =      2.5 : 1.0
                      좋아 = False             neg : pos    =      1.5 : 1.0
                     메리는 = False             neg : pos    =      1.1 : 1.0
                     메리랑 = False             neg : pos    =      1.1 : 1.0
                    고양이야 = False             neg : pos    =      1.1 : 1.0
                     마치고 = False             neg : pos    =      1.1 : 1.0
                    고양이도 = False             neg : pos    =      1.1 : 1.0
                     놀거야 = False             neg : pos    =      1.1 : 1.0
                     메리가 = False             neg : pos    =      1.1 : 1.0
                      이쁜 = False             neg : pos    =      1.1 : 1.0
'''
