expressao = input("Digite a expressão matemática: ")

resultado = 0
operador = '+'
numero = ''

for caractere in expressao:
    if caractere in '0123456789': 
        numero += caractere
    elif caractere in ['+', '-', '*', '/']: 
        if operador == '+':
            resultado += int(numero)
        elif operador == '-':
            resultado -= int(numero)
        elif operador == '*':
            resultado *= int(numero)
        elif operador == '/':
            if int(numero) == 0:  
                print("Erro: divisão por zero!")
                exit()  
            resultado /= int(numero)
        numero = '' 
        operador = caractere


if numero:
    if operador == '+':
        resultado += int(numero)
    elif operador == '-':
        resultado -= int(numero)
    elif operador == '*':
        resultado *= int(numero)
    elif operador == '/':
        if int(numero) == 0:  
            print("Erro: divisão por zero!")
            exit()  
        resultado /= int(numero)

print("O resultado da expressão é:", resultado)
