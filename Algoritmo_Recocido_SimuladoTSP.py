import random
import math
import matplotlib.pyplot as plt

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

def calcular_longitud_ruta(ruta, ciudades):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancia(ciudades[ruta[i]], ciudades[ruta[i+1]])
    longitud += distancia(ciudades[ruta[-1]], ciudades[ruta[0]])
    return longitud

def recocido_simulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones):
    num_ciudades = len(ciudades)
    ruta_actual = list(range(num_ciudades))  # Ruta inicial ordenada
    mejor_ruta = ruta_actual
    mejor_longitud = calcular_longitud_ruta(ruta_actual, ciudades)
    
    temperatura = temperatura_inicial

    for _ in range(iteraciones):
        i, j = random.sample(range(num_ciudades), 2)
        ruta_vecina = ruta_actual[:]
        ruta_vecina[i], ruta_vecina[j] = ruta_vecina[j], ruta_vecina[i]
        longitud_vecina = calcular_longitud_ruta(ruta_vecina, ciudades)

        if longitud_vecina < mejor_longitud or random.random() < math.exp((mejor_longitud - longitud_vecina) / temperatura):
            ruta_actual = ruta_vecina
            mejor_longitud = longitud_vecina

        temperatura *= factor_enfriamiento

        if mejor_longitud < calcular_longitud_ruta(mejor_ruta, ciudades):
            mejor_ruta = ruta_actual

    return mejor_ruta, mejor_longitud

if __name__ == "__main__":
    ciudades = [(0, 0), (2, 4), (1, 3), (3, 5), (4, 1), (5, 2)]

    temperatura_inicial = 1000
    factor_enfriamiento = 0.95
    iteraciones = 1000

    mejor_ruta, mejor_longitud = recocido_simulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones)

    print("Mejor ruta encontrada:", mejor_ruta)
    print("Longitud de la mejor ruta:", mejor_longitud)

    coordenadas_ruta = [ciudades[i] for i in mejor_ruta]
    coordenadas_ruta.append(coordenadas_ruta[0])
    x_ruta, y_ruta = zip(*coordenadas_ruta)

    plt.figure(figsize=(12, 6))

    # Gráfica de la mejor ruta
    plt.subplot(1, 2, 1)
    plt.plot(x_ruta, y_ruta, marker='o', linestyle='-', color='red')
    for i, (x, y) in enumerate(coordenadas_ruta[:-1]):
        plt.text(x, y, str(mejor_ruta[i]), fontsize=12, ha='center', va='bottom')
    plt.title("Mejor Ruta")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
