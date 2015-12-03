# coding=utf-8
__author__ = 'yang'

import os
from collections import defaultdict
import json
from NaiveBayes import NBtext

# only used when you train the model for the first time
def rawDataProcess(classes, classes_dir, current_dir, project = 'category'):
    '''
    This function aims to generate dictionaries, which includes:
    1. 'text_' + project + '.json': a defauldict, keys are classes, values are lists of original articles
    2. 'prior_'+project+'.json': a defaultdict, keys are classes, values are number of articles in each classes
        Can be used to calculate prior probabilities
    3. 'num_'+project+'.json': a defaultdict, keys are classes, values are total number of words in that article
    4. 'wordfreq_' + project +'.json': a defaultdict, keys are classes, values are defaultdict (keys are words, values
        are the number of occurence of the words)
    5. 'vocab_' + project +'.json': a list of all vocabularies in the train data

    '''

    text_dict = defaultdict(list)  # a dict of list storing original text

    i = -1  # keep track of which class it is working on
    for dir in classes_dir:
        i += 1
        for root, dirs, files in os.walk(dir):

            for file in files:
                if file.endswith(".txt"):
                    os.chdir(dir)
                    with open(file, "r") as myfile:
                        text = myfile.read().replace('\n', '')

                        # process text
                        text = NBtext(text).text

                        class1 = classes[i]
                        text_dict[class1].append(text)
                        myfile.close()

    # reset it to current directory
    os.chdir(current_dir)
    with open('text_'+project+'.json', 'w') as f:
        json.dump(text_dict, f)




def rawDataProcess_sentiment(classes, classes_dir, current_dir, project = 'sentiment'):

    text_dict = defaultdict(list)  # a dict of list storing original text

    i = -1  # keep track of which class it is working on
    for dir in classes_dir:
        i += 1
        for root, dirs, files in os.walk(dir):

            for file in files:
                if file.endswith(".txt"):
                    os.chdir(dir)
                    with open(file, "r") as myfile:
                        lines = myfile.readlines()
                        record = False
                        review = ''
                        for line in lines:

                            if line[0:12] == '<review_text':
                                record = True
                                continue
                            if line[0:13] == '</review_text':
                                record = False
                                text = NBtext(review, sentiment=True).text # sentiment analysis

                                class1 = classes[i]
                                text_dict[class1].append(text)
                                review = ''

                            if (record):

                                review += (line.replace('\n', ' '))

                        myfile.close()

    # reset it to current directory
    os.chdir(current_dir)
    with open('text_'+project+'.json', 'w') as f:
        json.dump(text_dict, f)




def genDict(classes, current_dir, project):

    os.chdir(current_dir)

    with open('text_'+project+'.json') as f:
        text_dict = json.load(f)


    prior_dict = defaultdict(int)
    for class1 in classes:
        prior_dict[class1] += len(text_dict[class1])

    with open('prior_'+project+'.json', 'w') as f:
        json.dump(prior_dict, f)

    text_dict_concate = defaultdict(str) # concatednated string
    wordfreq_dict = defaultdict(lambda: defaultdict(int))
    num_dict = defaultdict(int) # total number of words for each class

    for class1 in classes:
        text_dict_concate[class1] = ' '.join(text_dict[class1])

        word_list = text_dict_concate[class1].split()
        for word in word_list:
            wordfreq_dict[class1][word] += 1

        num_dict[class1] = sum(wordfreq_dict[class1].values())

    with open('num_'+project+'.json','w') as f:
        json.dump(num_dict, f)

    with open('wordfreq_' + project +'.json', 'w') as f:
        json.dump(wordfreq_dict, f)


    vocabulary = wordfreq_dict[ classes[0] ].keys()
    vocabulary = set(vocabulary)

    for class1 in classes[1:]:
        vocabulary = vocabulary | set( wordfreq_dict[ class1 ].keys() )

    with open('vocab_' + project +'.json', 'w') as f:
        json.dump(list(vocabulary), f)


    # words = "apple banana apple strawberry banana lemon"
    # d = defaultdict(int)
    # for word in words.split():
    # d[word] += 1


if __name__ == '__main__':

    # uncomment them later
    '''
    classes = ['business', 'entertainment', 'politics', 'sport', 'tech']
    classes_dir = ['/Users/yang/Box Sync/UIUC/1 CS 411/project/bbcdata/business',
                   '/Users/yang/Box Sync/UIUC/1 CS 411/project/bbcdata/entertainment',
                   '/Users/yang/Box Sync/UIUC/1 CS 411/project/bbcdata/politics',
                   '/Users/yang/Box Sync/UIUC/1 CS 411/project/bbcdata/sport',
                   '/Users/yang/Box Sync/UIUC/1 CS 411/project/bbcdata/tech']

    current_dir = '/Users/yang/PycharmProjects/feel-the-news/naiveBayes'

    rawDataProcess(classes=classes, classes_dir=classes_dir, current_dir=current_dir, project = 'category')
    genDict(classes = classes, current_dir = current_dir, project='category')
    '''

    current_dir = '/Users/yang/PycharmProjects/feel-the-news/naiveBayes'
    classes = ['negative', 'positive']

    classes_dir = ['/Users/yang/Box Sync/UIUC/1 CS 411/project/sentiment/negative',
                   '/Users/yang/Box Sync/UIUC/1 CS 411/project/sentiment/positive']

    rawDataProcess_sentiment(classes=classes, current_dir=current_dir, classes_dir=classes_dir)
    genDict(classes = classes, current_dir = current_dir, project='sentiment')



