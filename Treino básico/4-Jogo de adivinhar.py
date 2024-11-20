palavra_secreta = "adeus"
adivinha = ""
numero_de_tentativas = 0
numero_limite_de_tentativas = len(palavra_secreta)
sem_tentativas = False

while adivinha != palavra_secreta and not(sem_tentativas):
    if numero_de_tentativas < numero_limite_de_tentativas:
        adivinha = input("Tenta adivinhar a palavra, tens " + str(numero_limite_de_tentativas - numero_de_tentativas) + " tentativas: ")
        numero_de_tentativas += 1
    else:
        sem_tentativas = True

if sem_tentativas:
    print("Ficaste sem tentativas, Perdeste o jogo")
else:
    print("Ganhaste! :)")