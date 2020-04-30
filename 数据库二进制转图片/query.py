
# -*- coding: utf-8 -*-
import sqlite3


map = []

def checkDb(name=0, score=0, a='*'):
    con = sqlite3.connect('data.db')
    sql = '''select * from answer '''
    cursor = con.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    for key in res:
        map.append(key[2])
    con.commit()
    cursor.close()


checkDb()


img = open('map22222.png','wb')

img.write(map[2])

