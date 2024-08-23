#encoding: utf-8

import os

class Employe:
    def __init__(self,nom,prenom,username,email,dateNaissance,phone,password):
        self.nom=nom
        self.prenom=prenom
        self.username=username
        self.email=email
        self.dateNaissance=dateNaissance
        self.phone=phone
        self.password=password
