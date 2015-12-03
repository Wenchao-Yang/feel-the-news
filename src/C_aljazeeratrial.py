def specific_aljamerica_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    tempall=parsed_html.find('div', attrs={'class': 'shareDiv'})
    title=''
    description=''
    if tempall!=None:
        title=tempall['data-title']
        description=tempall['data-description']
    time=''
    category=''
    tempcon=parsed_html.find('div', attrs={'class': 'parsys mainpar'})
    content=''
    if tempcon==None:
        return None
    for hit in tempcon.findAll('p'):
        content=content+hit.text
    return [title,time,description,content,category]


def total_aljamerica_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://america.aljazeera.com/")

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
        url='http://america.aljazeera.com'+hit['href']
        if url.find('/articles/')!=-1 and url.find('/2015/')!=-1 and url.find('/video/')==-1 and (len(URL)==0 or URL[-1].find(url)==-1):
            arr=specific_aljamerica_crawl(url)   
            if arr!=None:
                URL.append(url)
                title.append(arr[0])
                time.append(arr[1])
                description.append(arr[2])
                content.append(arr[3])
                category.append(arr[4])
    return [URL,arr,title,time,description,content,category]