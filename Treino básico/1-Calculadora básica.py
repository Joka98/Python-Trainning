num1 = float(input("\nIntroduza o 1º número a utilizar na operação: "))
operaçao = input("\nIntroduza a operaçao: ")
num2 = float(input("\nIntroduza o 2º numero: "))
print("\n")

if operaçao == "+":
    print(num1 + num2)
elif operaçao == "-":
    print(num1 - num2)
elif operaçao == "/":
    if num2 == 0:
        print("\nNão é possível fazer a divisão por 0")
        quit()
    print(num1 / num2)
elif operaçao == "*":
    print(num1 * num2)
else:
    print("\nOperação inválida")