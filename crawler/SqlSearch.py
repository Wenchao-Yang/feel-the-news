def below_5():
    import datetime
    import mysql.connector

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()

    query = ("SELECT * FROM demo "
             "WHERE readRate<5")


    cursor.execute(query)

    stra="["
    count=0
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        if count==0:
            count+=1
            stra+="{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
        else:
            stra+=",{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
    stra+="]"
    print(stra)
    
    cursor.close()
    cnx.close()
    
    
    
def f5_to_10():
    
    
    import datetime
    import mysql.connector

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()

    query = ("SELECT * FROM demo "
             "WHERE readRate>=5 AND readRate<10")


    cursor.execute(query)
    stra="["
    count=0
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        if count==0:
            count+=1
            stra+="{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
        else:
            stra+=",{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
    stra+="]"
    print(stra)
    cursor.close()
    cnx.close()
    
    
    
def f10_to_15():
    
    
    import datetime
    import mysql.connector

    #cnx = mysql.connector.connect(user='', password='',
    #                             host='',
    #                              database='demo')
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()

    query = ("SELECT * FROM demo "
             "WHERE readRate>=10 AND readRate<=15")


    cursor.execute(query)

    stra="["
    count=0
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        if count==0:
            count+=1
            stra+="{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
        else:
            stra+=",{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
    stra+="]"
    print(stra)
    
    cursor.close()
    cnx.close()
    
    
def above_15():
    
    
    import datetime
    import mysql.connector

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()

    query = ("SELECT * FROM demo "
             "WHERE readRate>=15")


    cursor.execute(query)

    stra="["
    count=0
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        if count==0:
            count+=1
            stra+="{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
        else:
            stra+=",{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
    stra+="]"
    print(stra)

    cursor.close()
    cnx.close()
    
    
def printall():
        
    import datetime
    import mysql.connector

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()

    query = ("SELECT * FROM demo ")


    cursor.execute(query)

    stra="["
    count=0
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        if count==0:
            count+=1
            stra+="{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
        else:
            stra+=",{\"title\":\""+title+"\", \"description\":\""+description+"\", \"senRate\":"+str(senRate)+", \"readRate\":"+str(readRate)+", \"url\":\""+url+"\", \"category\":\""+category+"\", \"readby\":\""+readby+"\"}"
    stra+="]"
    print(stra)

    cursor.close()
    cnx.close()
    
    
    
def call_search(arg):
    if arg==0:
        printall()
    if arg==1:
        below_5()
    if arg==2:
        f5_to_10()
    if arg==3:
        f10_to_15()
    if arg==4:
        above_15()
    
call_search(0)