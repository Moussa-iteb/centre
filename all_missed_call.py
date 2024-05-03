import pandas as pd  
import numpy as np
from datetime import timedelta
import sys

from datetime import date, time, datetime
import mysql.connector as sql
import mysql.connector
from mysql.connector import Error



for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
df=pd.read_excel("C:/Users/ACER/PFA/vv.xls",header=0)
df.Date=pd.to_datetime(df['Date']).dt.strftime('%d-%m-%Y %H:%M:%S')
df.drop(columns=["Time since last call", "Number of attempts","Status"],inplace=True)
file=range(1,999)
df.drop( df[df.Source.isin(file)].index, inplace=True)
df.drop_duplicates(subset ="Source", keep = 'last', inplace=True)
df=df.reset_index()
df.drop(columns=["index"],inplace=True)
db_connection = sql.connect(host='127.0.0.1', database='pfa', user='root', password='iteb1234')
db_cursor = db_connection.cursor() 
db_cursor.execute('SELECT * FROM entrant_answered')
table_rows = db_cursor.fetchall()
new = pd.DataFrame(table_rows)
new.rename(columns = {0: 'Date', 1: 'Source',2: 'Destination',3: 'Durée'}, inplace = True)
df2=new[['Date','Source']]
df3=df[['Date','Source','Destination']]

df2.Date=pd.to_datetime(df2['Date']).dt.strftime('%d-%m-%Y %H:%M:%S')

df2[['Date1','Date2']] = df2.Date.str.split(" ",expand=True) 
debut=df2['Date1'].str.replace('-','').astype(float)
Debut2=df2['Date2'].str.replace(':','').astype(float)
df2.Date1=debut
df2.Date2=Debut2


df3[['Date1','Date2']] = df3.Date.str.split(" ",expand=True) 
debutt=df3['Date1'].str.replace('-','').astype(float)
Debut22=df3['Date2'].str.replace(':','').astype(float)
df3.Date1=debutt
df3.Date2=Debut22

for i in range (0,len(df2)):
    
    for j in range (0,len(df3)):
             if df2.Source.loc[i]==df3.Source.loc[j]:
               if df2.Date1.loc[i]<=df3.Date1.loc[j]:
                if df2.Date2.loc[i]<df3.Date2.loc[j]:
                  df3.loc[j]=np.NaN
index_with_nan = df3.index[df3.isnull().any(axis=1)]

df3.drop(index_with_nan,0, inplace=True)
df3.drop(columns=["Date1"],inplace=True)
df3.drop(columns=["Date2"],inplace=True)
print(df3)

def dataframet(df3):
     try:
         connction=mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="iteb1234",
                                           database="pfa",
                                           charset="utf8")
         cur=connction.cursor()

         connction.commit()
         for (row, rs)in df3.iterrows():
             Date_debut_appel=str(rs[0])
             source=str(int(rs[1]))
             poste=str(rs[2])
             
             query="insert into a_e_no_answer_busy values ('"+Date_debut_appel+"','"+source+"','"+poste+"')";
             cur.execute(query)
         connction.commit()
         cur.close()
     except Error as e:
         print("erreur in mysql connection=",e)
     finally:
         if connction.is_connected():
             connction.close()
dataframet(df3)
print("\ndataframe to mysql data transformed succes ")



