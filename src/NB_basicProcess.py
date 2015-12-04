# coding=utf-8
__author__ = 'yang'


# Package needed in this file
# string
# nltk.corpus
# nltk.stem.porter (Already installed when I used it)


# import os
# import time
# t1=time.localtime()
# os.system("curl -s -XPOST localhost:9200/_bulk --data-binary @dataReadyToIndex.txt; echo;")
# t2=time.localtime()
# print( time.mktime(t2)-time.mktime(t1) )


# Remove Punctuation
import string
table = string.maketrans("", "")

def removePunc(s):
    s = " ".join(s.split()) # remove whitespace
    return s.translate(table, string.punctuation)


# Remove StopWord
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
def removeStop(text):
    import warnings
    warnings.filterwarnings("ignore")
    return ' '.join([word for word in text.split() if word not in cachedStopWords])


# Stem word
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

def stem(text):
    '''
    Assume punctuation has been removed.
    '''
    # wordList = [porter_stemmer.stem(word) for word in text.split(" ")]

    text_list = text.split(" ")
    wordList = []
    for word in text_list:
        try:
            word = porter_stemmer.stem(word)
        except UnicodeDecodeError:
            # print(word)
            continue
        # if isinstance(word,str):

        wordList.append(word)

    text = " ".join(wordList)
    text = text.encode('utf8')
    # return unicode # TODO: check whether it matters
    return text


def addSpace(text):
    # loop text, add space after period if there is not
    text_list = text.split()
    text_list_len = len(text_list)
    for i in range(text_list_len):
        if '.' in text_list[i]:
            text_list[i] = text_list[i].replace('.', '. ')
    text = ' '.join(text_list)
    return text

# def removeNum(text):


if __name__ == '__main__':

    print('Test remove_Stop:')
    test = "Anyone know of any fun cheap magic the gathering decks(modern format)? #mtg"
    print(removeStop(test))

    print('Test remove_punc:')
    test="hello, world. I'm a person, not a robot... Please: Haha \n \t let's see"
    print(removePunc(test))

    print('Tset stem:')
    test = "white house strongly condemned visit moscow syrian president bashar alassada spokesman criticised russia putting red carpet welcome the"
    print(stem(test))


    print('Test addSpace:')
    test = "hello, world.I'm a person, not a robot... Please: Haha \n \t let's see.the"
    print(addSpace(test))