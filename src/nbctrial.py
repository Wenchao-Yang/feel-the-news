def specific_nbc_crawl(url):
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
    temptime=parsed_html.find('span',attrs={'class': "published"})
    time=''
    if temptime!=None:
        time=temptime.text
    tempdescription=parsed_html.find('meta', attrs={'name': 'description'})
    description=''
    if tempdescription!=None:
        description=tempdescription['content']
    category=''
    tempcon=parsed_html.find('div', attrs={'class': 'article-body'})
    content=''
    if tempcon!=None:
        [x.extract() for x in tempcon.findAll('script')]
        content=tempcon.text
    if content=='':
        return None
    print 'yes'
    return [title,time,description,content,category]


def total_nbc_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.nbcnews.com")
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
        if url.startswith('/') and url.count('/')>2 and (len(URL)==0 or URL[-1].find(url)==-1):
            url='http://www.nbcnews.com'+url
            print url
            arr=specific_nbc_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    print [URL,arr,title,time,description,content,category]
total_nbc_crawl()