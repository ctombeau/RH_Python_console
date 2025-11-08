# coding:utf-8

import cgi
import cgitb
import html  # Pour échapper les caractères spéciaux dans les entrées utilisateur

cgitb.enable()  # Active l'affichage des erreurs dans le navigateur

form = cgi.FieldStorage()

# En-tête HTTP
print("Content-type: text/html; charset=utf-8\n")

# Début de la page HTML
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Page de résultats</h1>
"""

print(html_content)

# Traitement du formulaire
try:
    username = form.getfirst("username", None)  # Récupère la valeur du champ 'username'

    if username:
        username = html.escape(username)  # Évite les injections HTML
        print(f"<p>Bonjour {username} !</p>")
    else:
        raise ValueError("Pseudo non transmis.")

except Exception as e:
    print(f"<p>Erreur : {e}</p>")

# Fin de la page HTML
html_end = """
</body>
</html>
"""

print(html_end)
