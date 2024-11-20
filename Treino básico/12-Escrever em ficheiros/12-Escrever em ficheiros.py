
#Para testar podemos alterar o nome do ficheiro html que o programa cria para ver se cria um novo 
#Podemos tb alterar o texto

file = open("index.html", "w", encoding='utf-8')

file.write("<p>Isto é um parágrafo em HTML</p>")

file.close()