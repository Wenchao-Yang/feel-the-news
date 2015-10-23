def below_5():
    import datetime
    import mysql.connector

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()

    query = ("SELECT * FROM demo "
             "WHERE readRate<5")


    cursor.execute(query)

    for (title, description, senRate, readRate, url, category,readby) in cursor:
        print("{}, {}, {}, {}, {}, {}, {}".format(
                title, description, senRate, readRate, url, category,readby))

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

    for (title, description, senRate, readRate, url, category,readby) in cursor:
        print("{}, {}, {}, {}, {}, {}, {}".format(
                title, description, senRate, readRate, url, category,readby))

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

    for (title, description, senRate, readRate, url, category,readby) in cursor:
        print("{}, {}, {}, {}, {}, {}, {}".format(
                title, description, senRate, readRate, url, category,readby))
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

    for (title, description, senRate, readRate, url, category,readby) in cursor:
        print("{}, {}, {}, {}, {}, {}, {}".format(
                title, description, senRate, readRate, url, category,readby))

    cursor.close()
    cnx.close()
    
    
    
def call_search(arg):
    if arg==1:
        below_5()
    if arg==2:
        f5_to_10()
    if arg==3:
        f10_to_15()
    if arg==4:
        above_15()
        
