#Programa 9.7 - Criação de página HTML com Python
with open("index3.html", "w", encoding="utf-8") as page:
    page.write("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
        <meta charset="utf-8">
        <title>PAGE WITH PYTHON</title>
        </head>
        <body>
        <h1>Hello World</h1>
    """)
    for l in range(100):
        page.write("<p>{line}</p>")
    page.write("""
        </body>
        </html>
    """)
