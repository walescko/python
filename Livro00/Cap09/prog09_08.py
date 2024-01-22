#Programa 9.8 - Geração de uma págna web a partir de um dicionário
movies = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Os Nerds contra-atacam"],
    "policial": ["Chuva Negra", "Desejo ded Matar", "Xeque-mate"],
    "guerra": ["Rambo", "Platoon", "Até o último homem"]
}

with open("filmes.html", "w", encoding="utf-8") as page:
    page.write("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
        <meta charset="utf-8">
        <title>PAGE WITH PYTHON</title>
        </head>
        <body>
    """)
    for c, v in movies.items():
        page.write(f"<h1>{c}</h1>\n")
        for e in v:
            page.write(f"<h2>{e}</h2>\n")

    page.write("<body></html>")
    