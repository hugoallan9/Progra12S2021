'''
#Strings
cadena = "Egemplo"

print(cadena[1])
print(cadena[-1])
print(cadena[4:len(cadena)+1])

#Las cadenas son inmutables
#cadena[1] = "j"
#La manera correcta de corregir el error
cadena = cadena[0] + 'j' + cadena[2:]
print(cadena)
'''

#Usando for en cadena
cadena = "Hola Mundo"
for letra in cadena:
    if letra.upper() == 'O' or letra.upper() == 'I':
        print('La letra  "o" u la letra "i" forman parte de la cadena')
        break
