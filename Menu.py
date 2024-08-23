#encoding: utf-8

import os
from AjoutEmploye import *
from entities.Employe import *

def showMenu():
    print("1.Ajouter un employe")
    print("2.Lister les employes")
    print("3.Detail d'un employe")
    print("4.Modifier un employe")
    print("5.Supprimer un employe")
    n= input("Veuillez choisir le numero de votre choix: ")
    while int(n) < 1 or int(n) > 5:
        n= input("Veuillez choisir le numero de votre choix: ")
        
    print("La valeur choisie ",n);
    if(int(n)==1):
        print("\n*************************AJOUT D'EMPLOYE**********************************\n");
        print("Veuillez saisir les infos de l'employe ");
        nom=input("Nom de l'employe: ")
        prenom=input("Prenom de l'employe: ")
        dateNaissance=input("Date de Naissance de l'employe: ")
        username=input("Nom d'utilisateur l'employe: ")
        email=input("Email de l'employe: ")
        password=input("Mot de passe de l'employe: ")
        phone= input("Numero de telephone: ")
        employe=Employe(nom,prenom,username,email,dateNaissance,phone,password)
        addEmploye(employe)
    elif(int(n)==2):
        print("*************************LISTE D'EMPLOYE**********************************");
    elif(int(n)==3):
        print("*************************DETAIL D'EMPLOYE**********************************");
    elif(int(n)==4):
        print("*************************MODIFICATION D'EMPLOYE**********************************");
    elif(int(n)==5):
        print("*************************SUPPRESSION D'EMPLOYE**********************************");
   
print("Bienvenue a l'application Gestion des Employes\n")
showMenu()
    
