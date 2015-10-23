def below_5():
    import datetime
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()
    query = ("SELECT * FROM demo "
             "WHERE readRate<5")
    cursor.execute(query)
    output = []
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        one_output = {"title":"null", "description":"null","senRate":0, "readRate":0, "url":"null", "category":"null"}
        one_output["title"] = title
        one_output["description"] = description
        one_output["senRate"] = senRate  
        one_output["readRate"] = readRate
        one_output["url"] =url
        one_output["category"] = category
        one_output["readby"] = readby
        output.append(one_output)
    cursor.close()
    cnx.close()
    return json.dumps(output)



def f5_to_10():
    import datetime
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()
    query = ("SELECT * FROM demo "
             "WHERE readRate>=5 AND readRate<10")
    cursor.execute(query)
    output = []
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        one_output = {"title":"null", "description":"null","senRate":0, "readRate":0, "url":"null", "category":"null"}
        one_output["title"] = title
        one_output["description"] = description
        one_output["senRate"] = senRate  
        one_output["readRate"] = readRate
        one_output["url"] =url
        one_output["category"] = category
        one_output["readby"] = readby
        output.append(one_output)
    cursor.close()
    cnx.close()
    return json.dumps(output)



def f10_to_15():
    import datetime
    import mysql.connector
    import json
    #cnx = mysql.connector.connect(user='', password='',
    #                             host='',
    #                              database='demo')
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()
    query = ("SELECT * FROM demo "
             "WHERE readRate>=10 AND readRate<=15")
    cursor.execute(query)
    output = []
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        one_output = {"title":"null", "description":"null","senRate":0, "readRate":0, "url":"null", "category":"null"}
        one_output["title"] = title
        one_output["description"] = description
        one_output["senRate"] = senRate  
        one_output["readRate"] = readRate
        one_output["url"] =url
        one_output["category"] = category
        one_output["readby"] = readby
        output.append(one_output)
    cursor.close()
    cnx.close()
    return json.dumps(output)

def above_15():
    import datetime
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()
    query = ("SELECT * FROM demo "
             "WHERE readRate>=15")
    cursor.execute(query)
    output = []
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        one_output = {"title":"null", "description":"null","senRate":0, "readRate":0, "url":"null", "category":"null"}
        one_output["title"] = title
        one_output["description"] = description
        one_output["senRate"] = senRate  
        one_output["readRate"] = readRate
        one_output["url"] =url
        one_output["category"] = category
        one_output["readby"] = readby
        output.append(one_output)
    cursor.close()
    cnx.close()
    return json.dumps(output)


def printall():
    import datetime
    import mysql.connector
    import json
    cnx = mysql.connector.connect(user='root', password='1111',
                                  database='start')
    cursor = cnx.cursor()
    query = ("SELECT * FROM demo ")
    cursor.execute(query)
    output = []
    for (title, description, senRate, readRate, url, category,readby) in cursor:
        one_output = {"title":"null", "description":"null","senRate":0, "readRate":0, "url":"null", "category":"null"}
        one_output["title"] = title
        one_output["description"] = description
        one_output["senRate"] = senRate  
        one_output["readRate"] = readRate
        one_output["url"] =url
        one_output["category"] = category
        one_output["readby"] = readby
        output.append(one_output)
    cursor.close()
    cnx.close()
    return json.dumps(output)



def call_search(arg):
    if arg=='0':
        return printall()
    if arg=='1':
        return below_5()
    if arg=='2':
        return f5_to_10()
    if arg=='3':
        return f10_to_15()
    if arg=='4':
        return above_15()
