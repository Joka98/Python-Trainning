
try:
    #Coment and uncomment to get both results and try to input a character instead of a number
    #valor = 10/0
    num = int(input("\nIntroduza um número: "))
    print(num)
except ValueError:
    print("Tens de introduzir um número")
except ZeroDivisionError as err:
    print(err)