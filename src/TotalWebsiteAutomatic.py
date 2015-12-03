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
    from io import StringIO
    
    #arr=[title,time,description,content,category]
    domain="abcnews.go.com"
    arr=total_abc_crawl(url)
    #get category, readability, sentiment, add domain and form json
    
    
    
    domain="america.aljazeera.com"
    arr=total_aljamerica_crawl(url)
        
    
    domain="www.aljazeera.com"
    arr=total_aljnew_crawl(url)
    
    
    domain="www.bbc.com"
    arr=total_bbc_crawl(url)
    
    
    domain="www.cnn.com"
    arr=total_cnn_crawl(url)
    
    
    domain="money.cnn.com"
    arr=total_cnn_money_crawl(url)
    
    
    domain="www.dogonews.com"
    arr=total_dogo_crawl(url)
    
    
    domain="www.nbcnews.com"
    arr=total_nbc_crawl(url)
    
    
    domain="www.newscientist.com"
    arr=total_newscie_crawl(url)
    
    
    domain="www.reuters.com"
    arr=total_reuters_crawl(url)
    
    
    domain="www.sportingnews.com"
    arr=total_sport_crawl(url)
    
    
    domain="www.time.com"
    arr=total_time_crawl(url)