# coding:utf-8

import sys
import os
import urllib.parse
import html

print("Content-type: text/html; charset=utf-8\n")

# Fonction pour lire les données POST
def parse_post_data():
    try:
        content_length = int(os.environ.get("CONTENT_LENGTH", 0))
        post_data = sys.stdin.read(content_length)
        return urllib.parse.parse_qs(post_data)
    except Exception as e:
        return {}

# Récupération des données
form = parse_post_data()

# Début HTML
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Résultats</title>
</head>
<body>
    <h1>Page de résultats</h1>
"""

print(html_content)

# Traitement du champ "username"
username = form.get("username", [None])[0]
if username:
    username = html.escape(username)
    print(f"<p>Bonjour {username} !</p>")
else:
    print("<p>Pseudo non transmis.</p>")

# Fin HTML
html_end = """
</body>
</html>
"""
print(html_end)
