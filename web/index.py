#coding:utf-8

import cgi

print("Content-type: text/html; charset=utf-8\n")

#print("<h1>Bonjour</h1>")

html = """<!DOCTYPE html>
<head>
    <charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Bonjour!</h1>
    <p>Bla bla bla</p>
</body>
</html>
"""

print(html)