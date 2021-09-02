
a = -1
b = 5


try:
    a = int(input('Ingrese un número: \n'))
    b = int(input('Ingrese otro número: \n'))
    print('a/b =', a/b)
    print('a+b = ', a+b)
except ValueError:
    print('No se pudo convertir el número')
except ZeroDivisionError:
    print('No se puedo dividir dentro de cero')
except:
    print('Un error no conocido')
else:
    print('El programa ha finalizado sin errores')
finally:
    a = -1
    b = 5

print(a,b)
