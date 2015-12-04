def specific_abc_crawl(url):
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
    temptime=parsed_html.find('span',attrs={'class': 'timestamp'})
    time=''
    if temptime!=None:
        time=temptime.text
    tempdescription=parsed_html.find('meta', attrs={'property': 'og:description'})
    description=''
    if tempdescription!=None:
        description=tempdescription['content']
    category=''
    tempcon=parsed_html.find('div', attrs={'class': 'article-copy'})
    content=''
    if tempcon!=None:
        content=tempcon.text
    if content=='':
        return None
    if description=='':
        return None
    if title=='':
        return None
    # print 'yes'
    return [title,time,description,content,category]


def total_abc_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://abcnews.go.com/")
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
        if url[0]=='/' and url.find("http")==-1 and find_duplicate_in_URL(URL, 'http://abcnews.go.com'+url)==False:
            url='http://abcnews.go.com'+url
            # print url
            arr=specific_abc_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    handle=urllib.urlopen("http://abcnews.go.com/Health")
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a', href=True):
        url=hit['href']
        if url[0]=='/' and url.find("http")==-1 and find_duplicate_in_URL(URL, 'http://abcnews.go.com'+url)==False:
            url='http://abcnews.go.com'+url
            # print url
            arr=specific_abc_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    handle=urllib.urlopen("http://abcnews.go.com/Technology")
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a', href=True):
        url=hit['href']
        if url[0]=='/' and url.find("http")==-1 and find_duplicate_in_URL(URL, 'http://abcnews.go.com'+url)==False:
            url='http://abcnews.go.com'+url
            # print url
            arr=specific_abc_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    handle=urllib.urlopen("http://abcnews.go.com/Politics")
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a', href=True):
        url=hit['href']
        if url[0]=='/' and url.find("http")==-1 and find_duplicate_in_URL(URL, 'http://abcnews.go.com'+url)==False:
            url='http://abcnews.go.com'+url
            # print url
            arr=specific_abc_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    handle=urllib.urlopen("http://abcnews.go.com/Entertainment")
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    for hit in parsed_html.findAll('a', href=True):
        url=hit['href']
        if url[0]=='/' and url.find("http")==-1 and find_duplicate_in_URL(URL, 'http://abcnews.go.com'+url)==False:
            url='http://abcnews.go.com'+url
            # print url
            arr=specific_abc_crawl(url)   
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