def any_crawl(url):
    from io import StringIO
    import urllib2 
    from bs4 import BeautifulSoup
    
    flag=0
    try: 
        response = urllib2.urlopen(url)
    except urllib2.HTTPError, err:
        flag=1
    except urllib2.URLError, err:
        flag=1
    if flag==1:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        req = urllib2.Request(url,data = None,headers = headers)
        handle=urllib2.urlopen(req)
    else:
        handle=urllib2.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    maxp=None
    maxnum=0
    
    parent=None
    parentnum=0
    
    [x.extract() for x in parsed_html.findAll('script')]
    [x.extract() for x in parsed_html.findAll('figure')]
    [x.extract() for x in parsed_html.findAll('style')]
    for hit in parsed_html.findAll('p'):
        if (len(hit.text)>maxnum and (hit.parent!=None and len(hit.parent.text)>len(hit.text) and len(hit.parent.text)>parentnum) and hit.findPreviousSibling('p')!=None):
            maxp=hit
            maxnum=len(hit.text)
            parent=hit.parent
            parentnum=len(parent.text)
    
    
    if parent=None:
        return None
    tempparent=parent
    tempparentsib=maxp.findPreviousSibling(tempparent.name)
    if tempparentsib==None:
        tempparentsib=maxp.findNextSibling(tempparent.name)
    if tempparentsib==None:
        parent=tempparent
    else:
        if tempparentsib.find('p')!=None:
            parent=tempparent.parent
    content=parent.text
    temptitle=parsed_html.title
    if temptitle==None:
        return None
    title=temptitle.text
        
    description=''
    tempdesc=parsed_html.find('meta', attrs={'name': 'description'})
    if tempdesc!=None:
        description=tempdesc['content']
    else:
        tempdesc=parsed_html.find('meta', attrs={'property': 'og:description'})
        if tempdesc!=None:
            description=tempdesc['content']
    if description=='':
        description=content[:100]
    time=''
    category=''
    return [title,time,description,content,category]
