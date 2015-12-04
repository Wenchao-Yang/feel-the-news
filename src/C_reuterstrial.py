def specific_reuters_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    temptitle=parsed_html.find('title')
    title=''
    if temptitle!=None:
        title=temptitle.text
    time=''
    tempdescription=parsed_html.find('meta', attrs={'name': 'description'})
    description=''
    if tempdescription!=None:
        description=tempdescription['content']
    tempcat=parsed_html.find('span', attrs={'class': 'article-section'})
    if tempcat==None:
        category=''
    else:
        category=tempcat.text
    tempcon=parsed_html.find('span', attrs={'id': 'articleText'})
    if tempcon==None:
        return None
    content=tempcon.text
    if content=='':
        return None
    if description=='':
        return None
    if title=='':
        return None
    return [title,time,description,content,category]


def total_reuters_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.reuters.com")

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
        if url.find('http')==-1 and url.find('/article/')!=-1 and url.find('/video/')==-1 and find_duplicate_in_URL(URL, 'http://www.reuters.com'+url)==False:
            url='http://www.reuters.com'+url
            arr=specific_reuters_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    return [URL,title,time,description,content,category]


def find_duplicate_in_URL(URL, url):
    for i in range(len(URL)):
        if URL[i]==url:
            return True
    return False