import pandas as pd
import numpy as np
import sys
from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import Error
import mysql.connector as sql

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
    
    
    
df=pd.read_excel("C:/Users/ACER/PFA/ibtissem.xls",header=0)
df.drop(columns=["Groupe de sonnerie", "Canal src.","Centre de coûts","Canal dst."],inplace=True)
dft=df[df.Statut=='ANSWERED']
values=range(1,999)
sortant = dft[dft.Source.isin(values)]
sortant.drop(columns=["Statut"],inplace=True)
sortant[['Durée','Last']] = sortant.Durée.str.split("(",expand=True) 
sortant.drop(columns=["Last"],inplace=True)
final=sortant['Durée'].str.replace('s','').astype(str)

sortant.Durée=final


dff=df[df.Statut=='ANSWERED']
values=range(1,999)
file=range(1000,9999)
sor = dff[dff.Destination.isin(file)]
sor.drop(columns=["Statut"],inplace=True)

dff.drop( dff[dff.Source.isin(values)].index, inplace=True)
dff.drop( dff[dff.Destination.isin(file)].index, inplace=True)
dff.drop(columns=["Statut"],inplace=True)


dff=dff.reset_index()
dff.drop(columns=["index"],inplace=True)
sor=sor.reset_index()
sor.drop(columns=["index"],inplace=True)
sor[['Durée','Last']] = sor.Durée.str.split("(",expand=True) 
sor.drop(columns=["Last"],inplace=True)
final=sor['Durée'].str.replace('s','').astype(str)

sor.Durée=final
dff[['Durée','Last']] = dff.Durée.str.split("(",expand=True) 
dff.drop(columns=["Last"],inplace=True)
debut=dff['Durée'].str.replace('s','').astype(str)

dff.Durée=debut

df_new_column = pd.DataFrame([[60],[70],[80]], columns=['date_conversation'] )
df_new_column1 = pd.DataFrame([[60],[70],[80]], columns=['file'] )
df_new_column2 = pd.DataFrame([[60],[70],[80]], columns=['duree'] )

dff = pd.concat([dff,df_new_column], axis=1)
dff = pd.concat([dff,df_new_column1], axis=1)
dff = pd.concat([dff,df_new_column2], axis=1)

for i in range(0,len(dff)):
    for j in range(0,len(sor)):
     if dff.Source.loc[i]==sor.Source.loc[j]:
         dff.file.loc[i]=sor.Destination.loc[j]
         dff.duree.loc[i]=sor.Durée.loc[j]
         dff.date_conversation.loc[i]=sor.Date.loc[j]
dff=dff.reset_index()
dff.drop(columns=["index"],inplace=True)
db_connection = sql.connect(host='127.0.0.1', database='pfa', user='root', password='iteb1234')
db_cursor = db_connection.cursor() 
db_cursor.execute('SELECT * FROM entrant_answered')
table_rows = db_cursor.fetchall()
new = pd.DataFrame(table_rows)
new.rename(columns = {0: 'Date', 1: 'Source',2: 'Destination',3: 'Durée',4: ' file',5: ' date_conversation',6: 'durée'}, inplace = True)
for l in range(0,len(dff)):
 for c in range(0,len(new)):
        if new.Date.loc[c]==dff.Date.loc[l]:
            if new.Source.loc[c]==dff.Source.loc[l]:
                dff.loc[l]=np.NaN
index_with_nan = dff.index[dff.isnull().any(axis=1)]

dff.drop(index_with_nan,0, inplace=True)
def dataframet(sortant):
     try:
         connction=mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="iteb1234",
                                           database="pfa",
                                           charset="utf8")
         cur=connction.cursor()

         connction.commit()
         for (row, rs)in sortant.iterrows():
             Date_debut_appel=str(rs[0])
             source=str(int(rs[1]))
             destination=str(int(rs[2]))
             duree_conversation=str(rs[3])
             
             query="insert into sortant_answered values ('"+Date_debut_appel+"','"+source+"','"+destination+"','"+duree_conversation+"')";
             cur.execute(query)
         connction.commit()
         cur.close()
     except Error as e:
         print("erreur in mysql connection=",e)
     finally:
         if connction.is_connected():
             connction.close()
def data(dff):
    try:
        connction=mysql.connector.connect(host="localhost",
                                          user="root",
                                          password="iteb1234",
                                          database="pfa",
                                          charset="utf8")
        cur=connction.cursor()

        connction.commit()
        for (row, rs)in dff.iterrows():
           
            Date_debut_appel=str(rs[0])
            Source=str(int(rs[1]))
           
            destination=str(int(rs[2]))
            duree_appel=str(int(rs[3]))
            file=str(int(rs[5]))
            date_conversation=str(rs[4])
            durée=str(int(rs[6]))
            
            query="insert into Entrant_Answered values ('"+Date_debut_appel+"','"+Source+"','"+destination+"','"+duree_appel+"','"+file+"','"+date_conversation+"','"+durée+"')"
            cur.execute(query)
        connction.commit()
        cur.close()
    except Error as e:
        print("erreur in mysql connection=",e)
    finally:
        if connction.is_connected():
            connction.close()






data(dff)
print("\ndataframe to mysql data transformed succes ")



dataframet(sortant)
print("\ndataframe to mysql data transformed succes ")















