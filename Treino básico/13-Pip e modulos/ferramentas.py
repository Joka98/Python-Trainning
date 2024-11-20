import random

feets_num_quilómetro = 3280.84
Artistas = ["Ski Mask", "J Cole", "Plaiboy Carti", "JID"]

def extensão_de_um_ficheiro(nomeficheiro):
    return nomeficheiro[nomeficheiro.index(".") + 1:]

def rolar_dado(num):
    return random.randint(1, num)

def rand_artista():
    return random.choice(Artistas)
