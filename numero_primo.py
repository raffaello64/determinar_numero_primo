def num_primo(numero):
    if (numero == 1):
        return 'El número no es primo'	
    elif (numero == 2):
        return 'El número es primo'
    else:
        for x in range(2,numero):
            if(numero % x == 0):
                return 'El número no es primo'
        return 'El número es primo'
numero = int(input('Ingrese un número: '))             
print(num_primo(numero))
