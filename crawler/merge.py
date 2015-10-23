''' This file is to combine crawler with the analyzer
'''

from readbility import Text
import json

def one_website_return(url):
    '''
    :param url: url
    :return: a dictionary
    '''
    from trial import crawlerforspecificwebsite
    arr=crawlerforspecificwebsite(url)

    text = Text(arr[0].encode('utf-8'))

    output = {'title':'null', 'description':'null','senRate':0, 'readRate':0, 'url':'null', 'category':'null'}
    output['title'] = arr[1]
    output['description'] = arr[3]
    output['senRate'] = 0  # TODO: sentiment analysis
    output['readRate'] = text.avg_grade()
    output['url'] = url
    output['category'] = arr[2]
    output['readby'] = 'unread'

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

        one_output = {'title':'null', 'description':'null','senRate':0, 'readRate':0, 'url':'null', 'category':'null'}
        one_output['title'] = arr[i][0]
        one_output['description'] = arr[i][3]
        one_output['senRate'] = 0  # TODO: sentiment analysis
        one_output['readRate'] = text.avg_grade()
        one_output['url'] = arr[i][1]
        one_output['category'] = arr[i][5]
        one_output['readby'] = 'unread'

        output.append(one_output)

    return output



def total_website_print(day = "Thu"):
    output = total_website_return(day)
    print(json.dumps(output))


if __name__ == '__main__':
    import sys
    if sys.argv[1] == '-u':
        one_website_print(sys.argv[2])
    elif sys.argv[1] == '-d':
        total_website_print(sys.argv[2])
    else:
        print('merge.py -u <url>')
        print('merge.py -d <day>')


    # one_website_print("http://www.bbc.com/news/world-europe-34595409")

    # print(total_website_return()[0])
    # total_website_print()
    # one_website_print("http://www.bbc.com/news/world-europe-34602621")