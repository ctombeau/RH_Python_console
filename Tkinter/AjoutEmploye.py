from tkinter import *

fenetre = Tk()
champ_lebel = Label(fenetre, text="AJOUT D'UN EMPLOYE")
champ_lebel.pack() 


nom = Label(fenetre, text="Nom")
nom.pack()

inputNom = StringVar()
inputNomSaisie = Entry(fenetre, textvariable=inputNom, width=30)
inputNomSaisie.pack()


prenom = Label(fenetre, text="Prenom")
prenom.pack()

inputPrenom = StringVar()
inputPrenomSaisie = Entry(fenetre, textvariable=inputPrenom, width=30)
inputPrenomSaisie.pack()

dateNaissance = Label(fenetre, text="Date de Naissance")
dateNaissance.pack()

sexeLablel = Label(fenetre, text="Sexe")
sexeLablel.pack()

sexe = StringVar()
feminin = Radiobutton(fenetre, text="F", variable=sexe,value="F")
masculin = Radiobutton(fenetre, text="M", variable=sexe,value="M")
feminin.pack()
masculin.pack()
sexe.get()

inputDateNaissance = StringVar()
inputDateNaissanceSaisie = Entry(fenetre, textvariable=inputDateNaissance, width=30)
inputDateNaissanceSaisie.pack()

username = Label(fenetre, text="Nom utilisateur")
username.pack()

inputUsername = StringVar()
inputUsernameSaisie = Entry(fenetre, textvariable=inputUsername, width=30)
inputUsernameSaisie.pack()

email = Label(fenetre, text="Email")
email.pack()

inputEmail = StringVar()
inputEmailSaisie = Entry(fenetre, textvariable=inputEmail, width=30)
inputEmailSaisie.pack()

password = Label(fenetre, text="Mot de passe")
password.pack()

inputPassword = StringVar()
inputPasswordSaisie = Entry(fenetre, textvariable=inputPassword, width=30)
inputPasswordSaisie.pack()

password2 = Label(fenetre, text="Retapez Mot de Passe")
password2.pack()

inputPassword2 = StringVar()
inputPassword2Saisie = Entry(fenetre, textvariable=inputPassword2, width=30)
inputPassword2Saisie.pack()

phone = Label(fenetre, text="Telephone")
phone.pack()

inputPhone = StringVar()
inputPhoneSaisie = Entry(fenetre, textvariable=inputPhone, width=30)
inputPhoneSaisie.pack()

envoyer = Button(fenetre, text="AJOUTER")
envoyer.pack()

quitter = Button(fenetre, text="QUITTER",command = fenetre.quit)
quitter.pack()

fenetre.mainloop()
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)