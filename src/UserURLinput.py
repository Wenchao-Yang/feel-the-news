def UserUrlInput(url):

    '''Aims to crawl one specific article'''

    from C_anytrial import any_crawl
    from C_abctrial import specific_abc_crawl
    from C_aljazeeratrial import specific_aljamerica_crawl
    from C_aljazeeratrial2 import specific_aljnew_crawl
    from C_bbctrial import specific_bbc_crawl
    from C_cnntrial import specific_cnn_crawl,specific_cnn_money_crawl
    from C_dogotrial import specific_dogo_crawl
    from C_nbctrial import specific_nbc_crawl
    from C_newscietrial import specific_newscie_crawl
    from C_reuterstrial import specific_reuters_crawl
    from C_sporttrial import specific_sport_crawl
    from C_timetrial import specific_time_crawl
    from io import StringIO
    import urllib
    import urllib2 
    if url.startswith("http://")!=True and url.startswith("https://")!=True:
        url="http://"+url
    print url
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(url,data = None,headers = headers)
    try: 
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, err:
        return None
    except urllib2.URLError, err:
        return None
    arr=None
    if url.find("abcnews.go.com")!=-1:
        arr=specific_abc_crawl(url)
    elif url.find("america.aljazeera.com")!=-1:
        arr=specific_aljamerica_crawl(url)
    elif url.find("www.aljazeera.com")!=-1:
        arr=specific_aljnew_crawl(url)
    elif url.find("www.bbc.com")!=-1:
        arr=specific_bbc_crawl(url)
    elif url.find("www.cnn.com")!=-1:
        arr=specific_cnn_crawl(url)
    elif url.find("money.cnn.com")!=-1:
        arr=specific_cnn_money_crawl(url)
    elif url.find("www.dogonews.com")!=-1:
        arr=specific_dogo_crawl(url)
    elif url.find("www.nbcnews.com")!=-1:
        arr=specific_nbc_crawl(url)
    elif url.find("www.newscientist.com")!=-1:
        arr=specific_newscie_crawl(url)
    elif url.find("www.reuters.com")!=-1:
        arr=specific_reuters_crawl(url)
    elif url.find("www.sportingnews.com")!=-1:
        arr=specific_sport_crawl(url)
    elif url.find("www.time.com")!=-1:
        arr=specific_time_crawl(url)
    
    if arr==None:
        arr=any_crawl(url)
    return arr

    ''':return a list containing [title,time,description,content,category]'''

        