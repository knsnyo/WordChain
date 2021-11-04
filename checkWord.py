'''
알맞은 단어인지 확인
'''
from numpy import empty
import pandas as pd

# 명사 데이터
data = pd.read_csv("noun_dictionary.csv")
#print(word_noun)

# 알맞은 단어를 입력하였는지
def check(head, txt):
    if len(txt) < 2:
        return -1
    elif data[data['어휘']==txt].size == 0:
        return -2
    elif head[-1] != txt[0]:
        return -3
    else:
        return 1
