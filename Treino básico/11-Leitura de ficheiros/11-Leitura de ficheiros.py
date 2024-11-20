'''
r - read
w - write
a - append
r+ - read and write
'''

ficheiro_de_empregados = open("empregados.txt", encoding='utf-8')

for empregado in ficheiro_de_empregados.readlines():
    print(empregado)
ficheiro_de_empregados.close()