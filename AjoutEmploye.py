#encoding: utf-8

import os
from entities.Employe import *

def addEmploye(e) :
    path="C:/Python/Employe.txt"
    n=numberOfLine()
    f=open(path,"a")
    f.write(str(n+1)+";"+e.nom +";"+e.prenom+";"+e.username+";"+e.email+";"+e.password+";"+e.phone+"\n")
    f.close()
    #print(e.nom +" "+e.prenom+" "+e.username)
    
def listEmploye():
    path="C:/Python/Employe.txt"
    f=open(path,"r")
    lines=f.readlines()
    f.close
    for line in lines:
        print(line.strip())

def updateEmploye():
    print(numberOfLine())
    pass

def deleteEmploye():
    pass
    
def numberOfLine():
    n=0
    path="C:/Python/Employe.txt"
    f=open(path,"r")
    lines=f.readlines()
    f.close
    for line in lines:
        #print(line.strip())
        n=n+1
    return n