#coding:utf-8

#import cgi

print("Content-type: text/html; charset=utf-8\n")

#print("<h1>Bonjour</h1>")

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Page Web avec Python</h1>
    
    <form method="post" action="res.py">
        <p>
            <input type="text" name="username">
            <input type="submit" value="Envoyer">
        </p>
    
    </form>

</body>
</html>
"""

print(html)