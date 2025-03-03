import mysql.connector

# Se connecter à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplace par ton utilisateur MySQL
    password="Edma1995",  # Remplace par ton mot de passe
    database="mabanque"  # Remplace par le nom de ta base de données
)

# Créer un curseur
cur = conn.cursor()

# Exécuter une requête
cur.execute("SELECT * FROM client")

# Afficher les résultats
for row in cur.fetchall():
    print(row)

# Fermer la connexion
conn.close()
