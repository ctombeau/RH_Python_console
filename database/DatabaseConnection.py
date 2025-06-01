import mysql.connector

# Se connecter à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplace par ton utilisateur MySQL
    password="Edma1995",  # Remplace par ton mot de passe
    database="mabanque"  # Remplace par le nom de ta base de données
)


def showEmploye():
    cur = conn.cursor()
    cur.execute("SELECT * FROM client")
    for row in cur.fetchall():
        print(row)
    conn.close()
    
    
def saveEmploye(Employe e):