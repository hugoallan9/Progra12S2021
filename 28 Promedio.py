# [['Peter', 'Parker'], [80.0, 70.0, 85.0]]


def get_stats(lista_clase):
    nueva_lista = []
    for x in lista_clase:
        nueva_lista.append([x[0], x[1], avg(x[1])])
    return nueva_lista

def avg(calificaciones):
    return sum(calificaciones) / len(calificaciones)

test_grades = [[['Peter', 'Parker'], [10.0, 5.0, 85.0]],
               [['Bruce', 'Wayne'], [10.0, 8.0, 74.0]],
               [['Capitán', 'América'], [8.0, 10.0, 96.0]],
               [['Deadpool'], []]]

get_stats(test_grades)