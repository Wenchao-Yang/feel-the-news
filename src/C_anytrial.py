def any_crawl(url):
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen(url)
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
    title=''
    if temptitle!=None:
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
    print title
    print content
    print description
