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
        url='http://www.reuters.com'+hit['href']
        if url.find('/article/')!=-1 and url.find('/video/')==-1 and (len(URL)==0 or URL[-1].find(url)==-1):
            arr=specific_reuters_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    return [URL,arr,title,time,description,content,category]