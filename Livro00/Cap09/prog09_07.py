#Programa 9.7 - Criação de página HTML com Python
with open("index2.html", "w", encoding="utf-8") as page:
    page.write("<!DOCTYPE html>\n<")
    page.write("<html lang=\"pt-br\">\n")
    page.write("<head>\n")
    page.write("<meta charset=\"utf-8\">\n")
    page.write("<title>PAGE WITH PYTHON</title>\n")
    page.write("</head>\n")
    page.write("<body>\n")
    page.write("<h1>Hello World</h1>")
    for l in range(10):
        page.write("<p>{l}</p>\n")
    page.write("</body>\n")
    page.write("</html>\n")
