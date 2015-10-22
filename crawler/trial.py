def crawlerforspecificwebsite(urltext):

    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup


    bbcrssurl=urltext

    handle=urllib.urlopen(bbcrssurl)

    bbcnewscontent=handle.read()
    handle.close()

    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')


    [x.extract() for x in parsed_html.find('div', attrs={'class':'story-body__inner'}).findAll('script')]
    [x.extract() for x in parsed_html.find('div', attrs={'class':'story-body__inner'}).findAll('figure')]
    content= parsed_html.body.find('div', attrs={'class':'story-body__inner'}).text

    section=parsed_html.find("meta", {'property':"og:article:section"})['content']
    description=parsed_html.find("meta", {'property':"og:description"})['content']
    date=parsed_html.find("div", {'class':"date date--v2"}).text
    arr=[content,section,description,date]

    return arr