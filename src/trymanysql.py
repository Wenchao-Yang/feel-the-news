    
def find_article_duplicate(url):
    import datetime
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    query = ("SELECT * FROM article WHERE url='"+url+"'")
    
    cursor.execute(query)
    flag=0
    for (newurl, title) in cursor:
        flag=1
    print flag
    cursor.close()
    cnx.close()
    return flag

    
def find_likeby_duplicate(email,url):
    import datetime
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    query = ("SELECT * FROM likeby WHERE url='"+url+"' AND email='"+email+"'")
    
    cursor.execute(query)
    flag=0
    for (newurl, newemail) in cursor:
        flag=1
    print flag
    cursor.close()
    cnx.close()


def single_add_webpage(url):
    import mysql.connector
    import json
    from merge import one_website_return
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    add_demo = ("INSERT INTO article "
                "(title, url) "
                "VALUES (%(title)s, %(url)s)")
    demo_data=any_crawl(url)
    cursor.execute(add_demo,demo_data)
    cnx.commit()
    cursor.close()
    cnx.close()


    

def delete_addby(email,url):
    import mysql.connector
    import json

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    delete_demo = ("DELETE FROM addby WHERE email='"+email+"' AND url = '"+url+"'")
    cursor.execute(delete_demo)
    cnx.commit()
    cursor.close()
    cnx.close()

    
def delete_likeby(email,url):
    import mysql.connector
    import json

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    delete_demo = ("DELETE FROM likeby WHERE email='"+email+"' AND url = '"+url+"'")
    cursor.execute(delete_demo)
    cnx.commit()
    cursor.close()
    cnx.close()



def add_likeby(email,url):
    import mysql.connector
    import json
    from merge import one_website_return
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    add_demo = ("INSERT INTO likeby "
                "(email, url) "
                "VALUES (%s, %s)")
    cursor.execute(add_demo,(email,url))
    cnx.commit()
    cursor.close()
    cnx.close()

def add_addby(email,url):
    import mysql.connector
    import json
    from merge import one_website_return
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    add_demo = ("INSERT INTO addby "
                "(email, url) "
                "VALUES (%s, %s)")
    cursor.execute(add_demo,(email,url))
    cnx.commit()
    cursor.close()
    cnx.close()


def join_display_user_like(email):
    import mysql.connector
    import json
    from merge import one_website_return
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    add_demo = ("SELECT title, article.url FROM article, likeby WHERE article.url=likeby.url AND likeby.email='"+email+"'")
    output = []
    cursor.execute(add_demo)
    for (title, url) in cursor:
        one_output = {"title":"null","url":"null"}
        one_output["title"] = title
        one_output["url"] =url
        output.append(one_output)
    cursor.close()
    cnx.close()
    print output



def single_add_user(email, name):
    import mysql.connector
    import json
    from merge import one_website_return
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    add_demo = ("INSERT INTO user "
                "(email, name) "
                "VALUES (%(email)s, %(name)s)")
    demo_data=add_user(email, name)
    cursor.execute(add_demo,demo_data)
    cnx.commit()
    cursor.close()
    cnx.close()

def any_crawl(url):
    from io import StringIO
    import urllib2 
    from bs4 import BeautifulSoup
    import json
    handle=urllib2.urlopen(url)
    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')

    temptitle=parsed_html.title
    if temptitle==None:
        return None
    title=temptitle.text
    one_output = {"title":"null","url":"null"}
    one_output["url"] =url
    one_output["title"] =title
    return one_output

def add_user(email, name):
    one_output = {"email":"null","name":"null"}
    one_output["email"] =email
    one_output["name"] =name
    return one_output

def find_duplicate_in_data(data, url):
    for i in range(len(data)):
        if data[i]['url']==url:
            print "hey!"
            return True
    return False

def many_crawl():
    from io import StringIO
    import urllib
    from bs4 import BeautifulSoup
    handle=urllib.urlopen("http://www.bbc.com")

    bbcnewscontent=handle.read()
    handle.close()
    parsed_html = BeautifulSoup(bbcnewscontent,'lxml')
    output=[]
    for hit in parsed_html.findAll('a', attrs={'class':'media__link'}):
        url=hit['href']
        if url.startswith('/'):
            url="http://www.bbc.com"+url
            print url
            if find_article_duplicate(url)==0 and (len(output)==0 or find_duplicate_in_data(output,url)==False):
                arr=any_crawl(url)
                if arr!=None:
                    output.append(arr)
    return output


def multi_add_webpage():
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='trial')
    cursor = cnx.cursor()
    add_demo = ("INSERT INTO article "
                "(title, url) "
                "VALUES (%(title)s, %(url)s)")
    demo_data=many_crawl()
    for i in range(len(demo_data)):
        cursor.execute(add_demo,demo_data[i])
    cnx.commit()
    cursor.close()
    cnx.close()

#single_add_user('aaaasssdas','ted')
#single_add_user('bbas','ken')
#http://www.bbc.com/news/blogs-trending-34992061
#http://www.bbc.com/news/world-us-canada-35000998

multi_add_webpage()