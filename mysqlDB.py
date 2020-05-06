import Pandas_
import pandas as pd
import pymysql

conn=pymysql.connect(database="crimes",user="root",password="aks")
cursor=conn.cursor()
cursor.execute("use crimes")
# ALTER TABLE vendors
# ADD COLUMN vendor_group INT
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS crimes (ID INTEGER PRIMARY KEY)')
    lista=Pandas_.lista_columns()
    for x in lista:
        if x!="ID":
            print("ALTER TABLE crimes ADD COLUMN {} VARCHAR(40);".format(x))
            cursor.execute("ALTER TABLE crimes ADD COLUMN `{}` VARCHAR(40);".format(x))
create_table()