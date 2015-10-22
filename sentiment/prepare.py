__author__ = 'yang'

# import os
# import time


# t1=time.localtime()
# os.system("curl -s -XPOST localhost:9200/_bulk --data-binary @dataReadyToIndex.txt; echo;")
# t2=time.localtime()
# print( time.mktime(t2)-time.mktime(t1) )


# Remove Punctuation
import string
table = string.maketrans("", "")
def remove_punc(s):
    s = " ".join(s.split()) # remove whitespace
    return s.translate(table, string.punctuation)


# Remove StopWord
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
def remove_Stop(text):
    return ' '.join([word for word in text.split() if word not in cachedStopWords])





if __name__ == '__main__':

    print('Test remove_Stop:')
    test = "Anyone know of any fun cheap magic the gathering decks(modern format)? #mtg"
    print(remove_Stop(test))

    print('Test remove_punc:')
    test="hello, world. I'm a person, not a robot... Please: Haha \n \t let's see"
    print(remove_punc(test))

