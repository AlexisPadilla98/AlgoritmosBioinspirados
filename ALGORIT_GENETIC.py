import random

# Función objetivo
def funcion_objetivo(individuo):
    suma = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            suma += 2**i
    return suma**2 + 2

# Función de recombinación
def recombinacion_uniforme(individuo1, individuo2):
    hijo1 = individuo1[:]
    hijo2 = individuo2[:]
    punto_de_cruzamiento = random.randint(0, len(individuo1) - 1)
    for i in range(punto_de_cruzamiento, len(individuo1)):
        hijo1[i], hijo2[i] = individuo2[i], individuo1[i]

    return hijo1, hijo2

# Función de mutación
def mutacion(individuo):
    punto_de_mutacion = random.randint(0, len(individuo) - 1)
    individuo[punto_de_mutacion] = 1 - individuo[punto_de_mutacion]

    return individuo

# Crear la población inicial
poblacion = []
for _ in range(30):
    individuo = [random.randint(0, 1) for _ in range(4)]
    poblacion.append(individuo)

# Iteraciones
for generacion in range(5):
    print(f"Generación {generacion + 1}:")
    
    # Calcular la aptitud inicial
    for individuo in poblacion:
        aptitud = funcion_objetivo(individuo)
        individuo.append(aptitud)
    
    # Encontrar el individuo más apto
    mas_apto = max(poblacion, key=lambda x: x[-1])
    
    print("El individuo más apto es:", mas_apto)
    
    # Aplicar el operador de recombinación
    nuevos_individuos = []
    for _ in range(30):
        individuo1, individuo2 = random.sample(poblacion, 2)
        hijo1, hijo2 = recombinacion_uniforme(individuo1[:-1], individuo2[:-1])
        nuevos_individuos.append(hijo1 + [funcion_objetivo(hijo1)])
        nuevos_individuos.append(hijo2 + [funcion_objetivo(hijo2)])
    
    # Reemplazar la población antigua con los nuevos individuos
    poblacion = nuevos_individuos
    
    # Encontrar el individuo más apto después de la recombinación
    mas_apto = max(poblacion, key=lambda x: x[-1])
    
    print("El individuo más apto después de la recombinación es:", mas_apto)
    
    # Aplicar el operador de mutación
    for i in range(len(poblacion)):
        poblacion[i] = mutacion(poblacion[i][:-1]) + [funcion_objetivo(poblacion[i][:-1])]
