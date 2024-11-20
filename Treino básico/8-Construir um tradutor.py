def tradutor(frase):
    traduçao = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                traduçao += "G"
            else:
                traduçao += "g"
        else:
            traduçao += letra
    return traduçao

print("\nEste tradutor traduz todas as letras vogais para um g minúsculo.\n")
print(tradutor(input("Escreva uma frase: ")))