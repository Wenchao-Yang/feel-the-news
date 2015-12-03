def specific_time_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    temptitle=parsed_html.title
    title=''
    if temptitle!=None:
        title=parsed_html.title.text
    time=''
    tempdescription=parsed_html.find('meta', attrs={'name': 'description'})
    description=''
    if tempdescription!=None:
        description=parsed_html.find('meta', attrs={'name': 'description'})['content']
    category=''

    temp=parsed_html.find('div', attrs={'class': 'clipper-content'})
    if temp==None:
        return None
    [x.extract() for x in temp.findAll('script')]
    content=temp.text
    if description==''
        return None
    if title==''
        return None
    return [title,time,description,content,category]


def total_time_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.time.com")

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
        if hit.has_attr('data-event') and (hit.parent.name=='h2' or hit.parent.name=='h3' or hit.parent.name=='h4'):
            url=hit['href']
            if url.find('time.com')!=-1:
                arr=specific_time_crawl(url)   
                if arr!=None:
                    URL.append(url)
                    title.append(arr[0])
                    time.append(arr[1])
                    description.append(arr[2])
                    content.append(arr[3])
                    category.append(arr[4])
    return [URL,title,time,description,content,category]

