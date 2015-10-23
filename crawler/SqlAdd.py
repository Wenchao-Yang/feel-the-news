def single_add(url):
    import mysql.connector
    import json
    from merge import one_website_return

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()

    add_demo = ("INSERT INTO demo "
                "(title, description, senRate, readRate, url, category, readby) "
                "VALUES (%(title)s, %(description)s, %(senRate)s, %(readRate)s, %(url)s, %(category)s, %(readby)s)")

    demo_data=one_website_return(url)
    cursor.execute(add_demo,demo_data)


    cnx.commit()
    cursor.close()
    cnx.close()
    return json.dumps(demo_data)


def multi_add(day="Fri"):
    import mysql.connector
    import json
    from merge import total_website_return

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()


    add_demo = ("INSERT INTO demo "
                "(title, description, senRate, readRate, url, category, readby) "
                "VALUES (%(title)s, %(description)s, %(senRate)s, %(readRate)s, %(url)s, %(category)s, %(readby)s)")

    demo_data=total_website_return(day)

    for i in range(len(demo_data)):
        cursor.execute(add_demo,demo_data[i])

    cnx.commit()
    cursor.close()
    cnx.close()
    return json.dumps(demo_data)



def deletefrom(url):
    import mysql.connector
    import json

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()

    delete_demo = ("DELETE FROM demo WHERE url = '"+url+"'")

    cursor.execute(delete_demo)


    cnx.commit()
    cursor.close()
    cnx.close()

def updatein(url):
    import mysql.connector
    import json

    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')

    cursor = cnx.cursor()

    update_demo = ("UPDATE demo SET readby='Read' WHERE url = '"+url+"'")

    cursor.execute(update_demo)


    cnx.commit()
    cursor.close()
    cnx.close()

