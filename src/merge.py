''' This file is to combine crawler with the analyzer
'''

from R_readbility import Text
import json
from UserURLinput import UserUrlInput
from NB_NaiveBayes import NBtrain, NBtest
import time

def one_website_return(url):
    '''
    :param url: url
    :return: a dictionary
    '''

    arr=UserUrlInput(url)
    # return a list containing [title,time,description,content,category]

    Read_text = Text(arr[3].encode('utf-8'))

    text = arr[3].encode('utf-8')

    output = {"url":url, "domain": "null", "title": arr[0], "description": arr[2], "category": "null", "readability": 0, "sentiment": "null" }

    output["domain"] = url.split('/', 3)[2]
    output["category"] = NBtest(text, Cat_train).final_class
    output["sentiment"] = NBtest(text, Senti_train).final_class
    output["readability"] = Read_text.avg_grade()

    return output


def one_website_print(url):
    '''
    :param url:
    :return: a json
    '''
    output = one_website_return(url)
    print(json.dumps(output))



def total_website_return(day="Thu"):
    '''
    :param day:
    :return: a list of dict
    '''
    from crawler import crawlerforrss
    arr=crawlerforrss(day)
    output = []

    for i in range(len(arr)):
        text = Text(arr[i][4].encode('utf-8'))

        one_output = {"title":"null", "description":"null","senRate":0, "readRate":0, "url":"null", "category":"null"}
        one_output["title"] = arr[i][0]
        one_output["description"] = arr[i][3]
        one_output["senRate"] = 0  # TODO: sentiment analysis
        one_output["readRate"] = text.avg_grade()
        one_output["url"] = arr[i][1]
        one_output["category"] = arr[i][5]
        one_output["readby"] = "Unread"

        output.append(one_output)

    return output



def total_website_print(day = "Thu"):
    output = total_website_return(day)
    print(json.dumps(output))


if __name__ == '__main__':
    # import sys
    # if sys.argv[1] == '-u':
    #     one_website_print(sys.argv[2])
    # elif sys.argv[1] == '-d':
    #     total_website_print(sys.argv[2])
    # else:
    #     print('merge.py -u <url>')
    #     print('merge.py -d <day>')

    Cat_train = NBtrain('category')
    # result = NBtest(text, train)
    # print(result.prob)
    # print(result.final_class)
    Senti_train = NBtrain('sentiment')
    # result = NBtest(text, train)
    # print(result.prob)
    # print(result.final_class)


    start_time = time.time()
    one_website_print("http://www.bbc.com/news/world-europe-34595409")
    elapsed_time = time.time() - start_time
    print(elapsed_time)



    # print(total_website_return()[0])
    # total_website_print()
    start_time = time.time()
    one_website_print("http://www.bbc.com/news/world-europe-34602621")
    elapsed_time = time.time() - start_time
    print(elapsed_time)

