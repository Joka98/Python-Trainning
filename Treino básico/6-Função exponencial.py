
def elevar_ao_expoente(base, potencia):
    res = 1
    for index in range(potencia):
        res *= base
    return res

print(elevar_ao_expoente(2,10))