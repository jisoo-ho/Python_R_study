### Googletrans - 파이썬을 위한 구글 번역 API ###
'''
Googletrans는
구글 번역 API(Google Translate API)를 구현한 파이썬 라이브러리.

파이썬과 Googletrans 를 이용해서
무료로 그리고 무제한으로 구글의 번역 기능을 사용할 수 있다.
'''

# Googletrans 설치
'''
pip install googletrans
conda install -c conda-forge googletrans
명령 프롬프트에서 pip 또는 conda를 통해서 설치를 진행
'''

### Googletrans 기본 사용 ###
'''
Googletrans 라이브러리를 이용해서
간단한 문장을 특정 언어로 (구글) 번역하고, 언어를 자동 감지하는 기능을 사용.
'''

# 1. 번역하기
# googletrans에서 Translator를 불러오기

from googletrans import Translator

translator = Translator()

# translate() 에 번역할 문장을 입력해주면, 아래 같은 결과를 출력.
print(translator.translate('안녕하세요'))
# 결과 : Translated(src=ko, dest=en, text=Hi, pronunciation=None, extra_data="{'translat...")
# 기본값인 영어로 번역되고(dest=en) 그 값은 Hi 이다(text=Hi)
print(translator.translate('안녕하세요').text)
# 이 함수가 가지고 있는 속성인 text 만 가지고 나와서 'Hi'를 출력한다.


# 2. 언어 설정하기

'''
src와 dest 에 언어 코드를 입력해줌으로써
source 언어와 destination 언어를 설정할 수 있다.
'''

from googletrans import Translator

translator = Translator()
print(translator.translate('안녕하세요', src='ko', dest='ja'))
# Translated(src=ko, dest=ja, text=こんにちは, pronunciation=Kon'nichiwa, extra_data="{'translat...")

print(translator.translate('안녕하세요', src='ko', dest='ja').text)
# こんにちは
print(translator.translate('안녕하세요', src='ko', dest='ja').pronunciation)
# Kon'nichiwa

'''
LANGUAGES = {    'af': 'afrikaans',    'sq': 'albanian',    'am': 'amharic',
             'ar': 'arabic',    'hy': 'armenian',    'az': 'azerbaijani',
             'eu': 'basque',    'be': 'belarusian',    'bn': 'bengali',
             'bs': 'bosnian',    'bg': 'bulgarian',    'ca': 'catalan',
             'ceb': 'cebuano',    'ny': 'chichewa',    'zh-cn': 'chinese (simplified)',
             'zh-tw': 'chinese (traditional)',    'co': 'corsican',    'hr': 'croatian',
             'cs': 'czech',    'da': 'danish',    'nl': 'dutch',    'en': 'english',
             'eo': 'esperanto',    'et': 'estonian',    'tl': 'filipino',
             'fi': 'finnish',    'fr': 'french',    'fy': 'frisian',    'gl': 'galician',
             'ka': 'georgian',    'de': 'german',    'el': 'greek',    'gu': 'gujarati',
             'ht': 'haitian creole',    'ha': 'hausa',    'haw': 'hawaiian',    'iw': 'hebrew',
             'hi': 'hindi',    'hmn': 'hmong',    'hu': 'hungarian',    'is': 'icelandic',
             'ig': 'igbo',    'id': 'indonesian',    'ga': 'irish',    'it': 'italian',
             'ja': 'japanese',    'jw': 'javanese',    'kn': 'kannada',    'kk': 'kazakh',
             'km': 'khmer',    'ko': 'korean',    'ku': 'kurdish (kurmanji)',    'ky': 'kyrgyz',
             'lo': 'lao',    'la': 'latin',    'lv': 'latvian',    'lt': 'lithuanian',
             'lb': 'luxembourgish',    'mk': 'macedonian',    'mg': 'malagasy',    'ms': 'malay',
             'ml': 'malayalam',    'mt': 'maltese',    'mi': 'maori',    'mr': 'marathi',
             'mn': 'mongolian',    'my': 'myanmar (burmese)',    'ne': 'nepali',    'no': 'norwegian',
             'ps': 'pashto',    'fa': 'persian',    'pl': 'polish',    'pt': 'portuguese',
             'pa': 'punjabi',    'ro': 'romanian',    'ru': 'russian',    'sm': 'samoan',
             'gd': 'scots gaelic',    'sr': 'serbian',    'st': 'sesotho',    'sn': 'shona',
             'sd': 'sindhi',    'si': 'sinhala',    'sk': 'slovak',    'sl': 'slovenian', 
             'so': 'somali',    'es': 'spanish',    'su': 'sundanese',    'sw': 'swahili',
             'sv': 'swedish',    'tg': 'tajik',    'ta': 'tamil',    'te': 'telugu',    'th': 'thai',
             'tr': 'turkish',    'uk': 'ukrainian',    'ur': 'urdu',    'uz': 'uzbek',
             'vi': 'vietnamese',    'cy': 'welsh',    'xh': 'xhosa',    'yi': 'yiddish',
             'yo': 'yoruba',    'zu': 'zulu',    'fil': 'Filipino',    'he': 'Hebrew'}
'''
