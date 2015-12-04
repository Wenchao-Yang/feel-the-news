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

    text = arr[3].encode('utf-8')
    Read_text = Text(text)

    output = {"url":url, "title": arr[0], "description": arr[2], "category": "null", "readRate": 0, "senRate": "null" }

    output["category"] = NBtest(text, Cat_train).final_class
    output["senRate"] = NBtest(text, Senti_train).final_class
    output["readRate"] = Read_text.avg_grade()

    return output


def one_website_print(url):
    '''
    :param url:
    :return: a json
    '''
    output = one_website_return(url)
    print(json.dumps(output))




if __name__ == '__main__':
    print ('asdfasdf');

    Cat_train = NBtrain('category')
    Senti_train = NBtrain('sentiment')

    import sys
    if sys.argv[1] == '-u':
        one_website_print(sys.argv[2])
    else:
        print('merge.py -u <url>')


    # result = NBtest(text, train)
    # print(result.prob)
    # print(result.final_class)

    # result = NBtest(text, train)
    # print(result.prob)
    # print(result.final_class)


    # start_time = time.time()
    # one_website_print("http://www.bbc.com/news/world-europe-34595409")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    #
    # # print(total_website_return()[0])
    # # total_website_print()
    # start_time = time.time()
    # one_website_print("http://www.bbc.com/news/world-europe-34602621")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    #
    # start_time = time.time()
    # one_website_print("http://blog.hubspot.com/blog/tabid/6307/bid/34010/How-to-Use-Photoshop-The-Ultimate-Guide-for-the-Design-Impaired-Marketer.aspx")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    #
    # start_time = time.time()
    # one_website_print("http://america.aljazeera.com/articles/2015/12/3/san-bernardino-shooting-motive-searched.html")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    #
    # start_time = time.time()
    # one_website_print("http://america.aljazeera.com/articles/2015/12/3/long-troubled-san-bernardino-in-shock-over-mass-shooting.html")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    #
    # start_time = time.time()
    # one_website_print("http://america.aljazeera.com/articles/2015/12/3/mass-shooting-by-week.html")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)
    #
    # start_time = time.time()
    # one_website_print("http://www.aljazeera.com/news/2015/10/afghan-refugee-shot-dead-enter-bulgaria-151016072352279.html")
    # elapsed_time = time.time() - start_time
    # print(elapsed_time)


