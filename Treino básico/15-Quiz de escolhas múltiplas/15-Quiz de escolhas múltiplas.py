from pergunta import Pergunta

perguntas_incitadas = [
    "\nDe que cor são as maçãs?\n\n(a) Vermelhas/Verdes\n(b) Roxas\n(c) Laranjas\n\n-> ",
    "\nDe que cor são as bananas?\n\n(a) Azuis\n(b) Brancas\n(c) Amarelas\n\n-> ",
    "\nDe que cor são os morangos?\n\n(a) Amarelos\n(b) Vermelhos\n(c) Brancos\n\n-> "
]

perguntas = [
    Pergunta(perguntas_incitadas[0], "a"),
    Pergunta(perguntas_incitadas[1], "c"),
    Pergunta(perguntas_incitadas[2], "b"),
]

def run_test(perguntas):
    pontuaçao = 0
    for pergunta in perguntas:
        resposta_dada = input(pergunta.pergunta)
        if resposta_dada == pergunta.resposta:
            pontuaçao += 1
    print("Tiveste " + str(pontuaçao) + "/" + str(len(perguntas)) + " corretas")

run_test(perguntas)