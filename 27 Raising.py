

def calcular_razones(L1,L2):
    razones = []
    for index in range(len(L1)):
        try:
            razones.append(L1[index]/L2[index])
        except ZeroDivisionError:
            razones.append(float('nan'))
        except:
            raise ValueError('calcular_razones tiene argumentos inválidos', L1[index], L2[index])
    return razones

calcular_razones([1,'h'],[3,4])