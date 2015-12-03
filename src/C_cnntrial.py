def specific_cnn_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    content=''
    title=''
    temptitle=parsed_html.title
    if temptitle!=None:
        title=temptitle.text
    time=''
    description=''
    tempdes=parsed_html.find('meta', attrs={'name': 'description'})
    if tempdes!=None:
        description=tempdes['content']
    category=''
    for hit in parsed_html.findAll('p', attrs={'class': 'zn-body__paragraph'}):
        content=content+hit.text
    if content=='':
        return None
    print 'yes'
    return [title,time,description,content,category]


def specific_cnn_money_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    content=''
    title=''
    temptitle=parsed_html.title
    if temptitle!=None:
        title=temptitle.text
    time=''
    description=''
    tempdes=parsed_html.find('meta', attrs={'name': 'description'})
    if tempdes!=None:
        description=tempdes['content']
    category=''
    tempcon=parsed_html.find('div', attrs={'id': 'storytext'})
    if tempcon==None:
        return None
    
    [x.extract() for x in tempcon.findAll('script')]
    [x.extract() for x in tempcon.findAll('figure')]
    [x.extract() for x in tempcon.findAll('style')]
    content=tempcon.text
    print 'yes'
    return [title,time,description,content,category]




def total_cnn_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.cnn.com")
    
    bbcnewscontent=handle.read()
    handle.close()
    URL=[]
    title=[]
    time=[]
    description=[]
    content=[]
    category=[]
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('span', attrs={'class':'cd__headline-text'}):
        url=hit.previous['href']
        if url.startswith('/') and url.find('videos')==-1:
            url="http://www.cnn.com"+url
            arr=specific_cnn_crawl(url)
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    handle=urllib.urlopen("http://www.cnn.com/entertainment")
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('span', attrs={'class':'cd__headline-text'}):
        url=hit.previous['href']
        if url.startswith('/') and url.find('videos')==-1:
            url="http://www.cnn.com"+url
            print url
            arr=specific_cnn_crawl(url)
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    return [URL,title,time,description,content,category]

def total_cnn_money_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://money.cnn.com/news/")
    
    bbcnewscontent=handle.read()
    handle.close()
    URL=[]
    title=[]
    time=[]
    description=[]
    content=[]
    category=[]
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a', href=True):
        url=hit['href']
        if url.startswith('/2015') and url.find('videos')==-1:
            url="http://money.cnn.com"+url
            print url
            arr=specific_cnn_money_crawl(url)
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    

    return [URL,title,time,description,content,category]

