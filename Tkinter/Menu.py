from tkinter import *
from AjoutEmploye import createWindow 

def openAddUser():
    print("Ajout Employe")
    createWindow()

fenetre = Tk()
fenetre.geometry("400x400")
fenetre.title("MENU")
fenetre.grid() 

mainmenu= Menu(fenetre)
first_menu=Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Ajout Employe", command=openAddUser)
first_menu.add_command(label="Liste Employe")
first_menu.add_command(label="Modifier Employe")
first_menu.add_command(label="Supprimer Employe")

second_menu=Menu(mainmenu,tearoff=0)
second_menu.add_command(label="Ajout Compte")
second_menu.add_command(label="Ajout Compte")
second_menu.add_command(label="Ajout Compte")
second_menu.add_command(label="Ajout Compte")

mainmenu.add_cascade(label="Gestion Employe", menu=first_menu)
mainmenu.add_cascade(label="Gestion Compte", menu=second_menu)

fenetre.config(menu=mainmenu)
fenetre.mainloop()