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
    if content=='':
        return None
    if description=='':
        return None
    if title=='':
        return None
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
        url=hit['href']
        if url.find("http")==-1 and url.find('/articles/')!=-1 and url.find('/2015/')!=-1 and url.find('/video/')==-1 find_duplicate_in_URL(URL, 'http://america.aljazeera.com'+url)==False:
            url='http://america.aljazeera.com'+url
            arr=specific_aljamerica_crawl(url)   
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