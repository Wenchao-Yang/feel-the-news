from R_readbility import Text
import json
from NB_NaiveBayes import NBtrain, NBtest
import time

Cat_train = NBtrain('category')
Senti_train = NBtrain('sentiment')


def total_web_dump(arr, domain):

    '''arr is in the format: [URL,title,time,description,content,category]'''

    all_info = []
    for i in range(len(arr[0])):

        text = arr[4][i].encode('utf-8')
        Read_text = Text(text) # For readability

        one_article = {"url":arr[0][i], "title": arr[1][i], "description": arr[3][i], "category": "null", "readability": 0, "sentiment": "null" }
        one_article["category"] = NBtest(text, Cat_train).final_class
        one_article["sentiment"] = NBtest(text, Senti_train).final_class
        one_article["readability"] = Read_text.avg_grade()

        all_info.append(one_article)

    date = time.strftime("%d%m%Y")
    with open(date+'_'+domain+'.json', 'w') as f:
        json.dump(all_info, f)
    f.close()



def TotalWebsiteAutomatic():
    from C_abctrial import total_abc_crawl
    from C_aljazeeratrial import total_aljamerica_crawl
    from C_aljazeeratrial2 import total_aljnew_crawl
    from C_bbctrial import total_bbc_crawl
    from C_cnntrial import total_cnn_crawl,total_cnn_money_crawl
    from C_dogotrial import total_dogo_crawl
    from C_nbctrial import total_nbc_crawl
    from C_newscietrial import total_newscie_crawl
    from C_reuterstrial import total_reuters_crawl
    from C_sporttrial import total_sport_crawl
    from C_timetrial import total_time_crawl
    
    # in the format: [URL,title,time,description,content,category]
    domain="abcnews.go.com"
    arr=total_abc_crawl()
    #get category, readability, sentiment, add domain and form json
    total_web_dump(arr, domain)

    
    domain="america.aljazeera.com"
    arr=total_aljamerica_crawl()
    total_web_dump(arr, domain)
    
    domain="www.aljazeera.com"
    arr=total_aljnew_crawl()
    total_web_dump(arr, domain)
    
    domain="www.bbc.com"
    arr=total_bbc_crawl()
    total_web_dump(arr, domain)
    
    domain="www.cnn.com"
    arr=total_cnn_crawl()
    total_web_dump(arr, domain)
    
    domain="money.cnn.com"
    arr=total_cnn_money_crawl()
    total_web_dump(arr, domain)
    
    domain="www.dogonews.com"
    arr=total_dogo_crawl()
    total_web_dump(arr, domain)
    
    domain="www.nbcnews.com"
    arr=total_nbc_crawl()
    total_web_dump(arr, domain)
    
    domain="www.newscientist.com"
    arr=total_newscie_crawl()
    total_web_dump(arr, domain)
    
    domain="www.reuters.com"
    arr=total_reuters_crawl()
    total_web_dump(arr, domain)
    
    domain="www.sportingnews.com"
    arr=total_sport_crawl()
    total_web_dump(arr, domain)
    
    
    domain="www.time.com"
    arr=total_time_crawl()
    total_web_dump(arr, domain)


if __name__ == '__main__':
    TotalWebsiteAutomatic()