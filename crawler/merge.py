''' This file is to combine crawler with the analyzer
'''
from readbility.readbility import Text
import json

def one_website_return(url):
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

    return json.dumps(output)


def one_website_print(url):
    output = one_website_return(url)
    print(output)



def total_website_return(day="Thu"):
    from crawler import crawlerforrss
    arr=crawlerforrss(day)
    output = dict()

    for i in range(len(arr)):
        text = Text(arr[i][4].encode('utf-8'))

        one_output = {'title':'null', 'description':'null','senRate':0, 'readRate':0, 'url':'null', 'category':'null'}
        one_output['title'] = arr[i][0]
        one_output['description'] = arr[i][3]
        one_output['senRate'] = 0  # TODO: sentiment analysis
        one_output['readRate'] = text.avg_grade()
        one_output['url'] = arr[i][1]
        one_output['category'] = arr[i][5]

        output[i] = one_output

    return json.dumps(output)



def total_website_print(day = "Thu"):
    output = total_website_return(day)
    print(output)


if __name__ == '__main__':
    # one_website_print("http://www.bbc.com/news/world-europe-34595409")

    total_website_print()