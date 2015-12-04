def specific_newscie_crawl(url):
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
    temptime=parsed_html.find('p',attrs={'class': "published-date"})
    time=''
    if temptime!=None:
        time=temptime.text
    tempdescription=parsed_html.find('meta', attrs={'name': 'description'})
    description=''
    if tempdescription!=None:
        description=tempdescription['content']
    category=''
    tempcon=parsed_html.find('div', attrs={'class': 'article-content'})
    [x.extract() for x in tempcon.findAll('script')]
    content=''
    if tempcon!=None:
        content=tempcon.text
    if content=='':
        return None
    if description=='':
        return None
    if title=='':
        return None
    return [title,time,description,content,category]


def total_newscie_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("https://www.newscientist.com")
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
        if  find_duplicate_in_URL(URL, url)==False and url.find("www.newscientist.com")!=-1 and url.find("/article/")!=-1:
            print url
            arr=specific_newscie_crawl(url)   
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