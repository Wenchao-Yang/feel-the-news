def crawlerforrss(day):
    import xml.etree.ElementTree as ET
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    import lxml

    bbcrssurl="http://feeds.bbci.co.uk/news/world/rss.xml"

    handle=urllib.urlopen(bbcrssurl)

    bbcrsscontent=handle.read()
    handle.close()
    root = ET.fromstring(bbcrsscontent)
    count=0
    arr=[]
    for child in root[0]:
        if child.tag=="item" and child.find('pubDate').text.find(day)>=0: 
            count+=1
            title=child.find('title').text
            time=child.find('pubDate').text
            url=child.find('link').text
            description=child.find('description').text
            
            handle=urllib.urlopen(url)
            bbcnewscontent=handle.read()
            handle.close()
            parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
            [x.extract() for x in parsed_html.find('div', attrs={'class':'story-body__inner'}).findAll('script')]
            [x.extract() for x in parsed_html.find('div', attrs={'class':'story-body__inner'}).findAll('figure')]
            content=parsed_html.body.find('div', attrs={'class':'story-body__inner'}).text
            category=parsed_html.find("meta", {'property':"og:article:section"})['content']
            val=[title,url,time,description,content,category]
            arr.append(val)
            if count==2:
                break


    return arr
    