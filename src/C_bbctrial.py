def specific_bbc_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    bbcrssurl=url
    handle=urllib.urlopen(bbcrssurl)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    if url.find('/sport/')!=-1:
        temp=parsed_html.find('div', attrs={'class':'article'})
        if temp==None:
            temp=parsed_html.find('div', attrs={'id':'story-body'})
        if temp==None:
            return None
        [x.extract() for x in temp.findAll('script')]
        [x.extract() for x in temp.findAll('figure')]
        [x.extract() for x in temp.findAll('style')]
        content= temp.text
        
    else:
        temp=parsed_html.find('div', attrs={'class':'story-body__inner'})
        if temp==None:
            temp=parsed_html.find('div', attrs={'class':'text-wrapper'})
        if temp==None:
            return None
        [x.extract() for x in temp.findAll('script')]
        [x.extract() for x in temp.findAll('figure')]
        [x.extract() for x in temp.findAll('style')]
        content= temp.text

    category=''
    tempdes=parsed_html.find("meta", {'name':"description"})
    description=''
    if tempdes!=None:
        description=tempdes['content']
    time=''
    temptitle=parsed_html.find('title')
    title=''
    if temptitle!=None:
        title=temptitle.text
    print 'yes'
    return [title,time,description,content,category]






def total_bbc_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.bbc.com")

    bbcnewscontent=handle.read()
    handle.close()
    URL=[]
    title=[]
    time=[]
    description=[]
    content=[]
    category=[]
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a', attrs={'class':'media__link'}):
        url=hit['href']
        if url.startswith('/'):
            url="http://www.bbc.com"+url
            print url
            arr=specific_bbc_crawl(url)
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])


    print [URL,title,time,description,content,category]
    
def total_bbc_sport_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.bbc.com/sport/0/")

    bbcnewscontent=handle.read()
    handle.close()
    URL=[]
    title=[]
    time=[]
    description=[]
    content=[]
    category=[]
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a',  href=True):
        url=hit['href']
        if url.startswith('/sport/') and (len(URL)==0 or URL[-1].find(url)==-1):
            url="http://www.bbc.com"+url
            print url
            arr=specific_bbc_crawl(url)
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])


    return [URL,title,time,description,content,category]