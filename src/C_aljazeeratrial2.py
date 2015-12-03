def specific_aljnew_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    temptitle=parsed_html.find('title')
    if temptitle==None:
        title=''
    else:
        title=temptitle.text
    temptime=parsed_html.find('time')
    if temptime==None:
        time=''
    else:
        time=temptime.text
    tempdescription=parsed_html.find('meta', attrs={'name': 'description'})
    if tempdescription==None:
        description=''
    else:
        description=tempdescription['content']
    category=''
    tempcon=parsed_html.find('div', attrs={'class': 'article-body'})
    content=''
    if tempcon!=None:
        for hit in tempcon.findAll('p'):
            content=content+hit.text
    if content=='':
        return None
    if description==''
        return None
    if title==''
        return None
    return [title,time,description,content,category]


def total_aljnew_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.aljazeera.com/")

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
        if (url.find('/news/')!=-1 or url.find('/indepth/')!=-1 or url.find('/programmes/')!=-1 or url.find('/blogs/')!=-1) and (len(URL)==0 or URL[-1].find(url)==-1) and url.find(".html")!=-1 and url.find("http")==-1:
            url='http://www.aljazeera.com'+url
            arr=specific_aljnew_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    return [URL,title,time,description,content,category]