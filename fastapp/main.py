
from ctypes import util
import email
from logging import raiseExceptions
import sqlite3

from gettext import find
from sqlite3 import Cursor
from click import password_option
from fastapi import Depends, FastAPI,responses,status,HTTPException
import subprocess
from fastapi.middleware.cors import CORSMiddleware

from requests import Session, post
from requests import get
from pydantic import BaseModel
import mysql
import mysql.connector as sql
import mysql.connector
from mysql.connector import Error


class utilisateur(BaseModel):
    email:str
    nom:str
    password:str
class File(BaseModel):
    name:str

   


   

app=FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
         connction=mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="iteb1234",
                                           database="pfa")
         cur=connction.cursor()
         print("connection reussir")
except Error as error:
         print("erreur in mysql connection=",error)


@app.post("/addfile")
async def root(file:File):
    cmd = "python C:/Users/ACER/nett/all_calls.py C:/Users/ACER/nett/"+file.name
    cmd = subprocess.Popen(cmd,shell=True)
    return{"message":"hello world"}


@app.post("/add")
async def root(file:File):
    cmd = "python C:/Users/ACER/nett/all_missed_call.py C:/Users/ACER/nett/"+file.name
    cmd = subprocess.Popen(cmd,shell=True)
    return{"message":"hello world"}



@app.get("/admin")
def get_utilisateur():
   cur.execute("""select * from admin """)
   utilisateur=cur.fetchall()
   print(utilisateur)
   return {"data": utilisateur}
    


@app.post("/admin",status_code=status.HTTP_201_CREATED)
def login(uti:utilisateur):
    cur.execute("""insert into admin (email,nom,password) values (%s,%s,%s)""",(uti.email,uti.nom,uti.password)
    )
    new_utilisateur=cur.fetchone()
    if not utilisateur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"utilisateur with {email} was not found")
    connction.commit()
    return{"data":"created"}
@app.get("/admin/{email}")
def get_utilisateur(email:str):
    cur.execute("""SELECT * FROM admin WHERE email = %s""", (str(email)))
    utilisateur=cur.fetchone()
    return{"utilisateur_detail":utilisateur}
