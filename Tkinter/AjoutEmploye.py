from tkinter import *

def createWindow():
    fenetre = Tk()
    fenetre.geometry("400x400")
    fenetre.title("AJOUT D'UN EMPLOYE")
    fenetre.grid() 


    nom = Label(fenetre, text="Nom")
    nom.grid(row=0,column=0,pady=5)
    
    global inputNom
    var_nom=StringVar()
    inputNom = Entry(fenetre, width=30, textvariable=var_nom)
    inputNom.grid(row=0,column=1,pady=5)

    prenom = Label(fenetre, text="Prenom")
    prenom.grid(row=1,column=0,pady=5)
    
    global inputPrenom
    var_prenom=StringVar()
    inputPrenom = Entry(fenetre, width=30, textvariable=var_prenom)
    inputPrenom.grid(row=1,column=1,pady=5)

    dateNaissance = Label(fenetre, text="Date de Naissance")
    dateNaissance.grid(row=2,column=0,pady=5)

    global inputDateNaissance
    var_naissance=StringVar()
    inputDateNaissance = Entry(fenetre,  width=30, textvariable=var_naissance)
    inputDateNaissance.grid(row=2,column=1,pady=5)

    sexeLablel = Label(fenetre, text="Sexe")
    sexeLablel.grid(row=3,column=0,pady=5)
    
    global sexe
    sexe = StringVar()
    feminin = Radiobutton(fenetre, text="F", variable=sexe,value="F")
    masculin = Radiobutton(fenetre, text="M", variable=sexe,value="M")
    feminin.grid(row=3,column=1,pady=5)
    masculin.grid(row=3,column=2,pady=5)


    username = Label(fenetre, text="Nom utilisateur")
    username.grid(row=4,column=0,pady=5)
    
    global inputUsername
    var_username=StringVar()
    inputUsername = Entry(fenetre, width=30, textvariable=var_username)
    inputUsername.grid(row=4,column=1,pady=5)

    email = Label(fenetre, text="Email")
    email.grid(row=5,column=0,pady=5)
    
    global inputEmail
    var_email=StringVar()
    inputEmail = Entry(fenetre, width=30, textvariable=var_email)
    inputEmail.grid(row=5,column=1,pady=5)

    password = Label(fenetre, text="Mot de passe")
    password.grid(row=6,column=0,pady=5)
    
    global inputPassword
    var_password=StringVar()
    inputPassword = Entry(fenetre,  width=30, show="*",textvariable=var_password)
    inputPassword.grid(row=6,column=1,pady=5)

    password2 = Label(fenetre, text="Retapez Mot de Passe")
    password2.grid(row=7,column=0,pady=5)
    
    global inputPassword2
    var_password2=StringVar()
    inputPassword2 = Entry(fenetre, width=30, show="*", textvariable=var_password2)
    inputPassword2.grid(row=7,column=1,pady=5)

    phone = Label(fenetre, text="Telephone")
    phone.grid(row=8,column=0,pady=5)
    
    global inputPhone
    var_phone=StringVar()
    inputPhone = Entry(fenetre,  width=30,textvariable=var_phone)
    inputPhone.grid(row=8,column=1,pady=5)

    envoyer = Button(fenetre, text="AJOUTER", command=saveData)
    envoyer.grid(row=9,column=0,pady=5)

    quitter = Button(fenetre, text="QUITTER",command = fenetre.quit)
    quitter.grid(row=9,column=1,pady=5)

    fenetre.mainloop()
    cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
    cadre.grid(fill=BOTH)
    
def saveData():
    nom=inputNom.get()
    prenom=inputPrenom.get()
    username=inputUsername.get()
    email=inputEmail.get()
    dateNaissance=inputDateNaissance.get()
    password=inputPassword.get()
    password2=inputPassword2.get()
    phone=inputPhone.get()
    print(nom + " "+prenom+ " " + " ne le "+ dateNaissance+ " a le numero "+phone+" et username: "+username+" email "+ email+ " password: "+password)