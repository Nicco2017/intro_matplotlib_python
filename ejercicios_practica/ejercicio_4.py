# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from cProfile import label
from tkinter import Y
from matplotlib import markers
from matplotlib.cbook import ls_mapper
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    grafico = plt.figure()
    grafico.suptitle('Grafico ejemplo 4')
    fig_1 = grafico.add_subplot(2, 2, 1)
    fig_2 = grafico.add_subplot(2, 2, 2)
    fig_3 = grafico.add_subplot(2, 2, 3)
    fig_4 = grafico.add_subplot(2, 2, 4)

    fig_1.plot(x, y1, c='red', marker= '*')
    fig_1.set_facecolor('white')
    fig_1.grid(ls='dashed')
    fig_1.set_title('Grafico "cubo"', fontsize= 10) 
    fig_1.set_ylabel('Eje Y - Grafico 1', fontsize= 6)
    fig_1.set_xlabel('Eje X - Grafico 1', fontsize= 6)
    fig_1.legend('Y= X ** 2')

    fig_2.plot(x, y2, c='blue', marker= '*')
    fig_2.set_facecolor('white')
    fig_2.grid(ls='dashed')
    fig_2.set_title('Grafico "cubo"', fontsize= 10)
    fig_2.set_ylabel('Eje Y - Grafico 2', fontsize= 6)
    fig_2.set_xlabel('Eje X - Grafico 2', fontsize= 6)
    fig_2.legend('Y= X ** 3')   

    fig_3.plot(x, y3, c='green', marker= '*')
    fig_3.set_facecolor('white')
    fig_3.grid(ls='dashed')
    fig_3.set_title('Grafico "cuarta"', fontsize= 10)
    fig_3.set_ylabel('Eje Y - Grafico 3', fontsize= 6)
    fig_3.set_xlabel('Eje X - Grafico 3', fontsize= 6)
    fig_3.legend('Y= X ** 4')

    fig_4.scatter(x, y4, c='yellow')
    fig_4.set_facecolor('white')
    fig_4.grid(ls='dashed')
    fig_4.set_title('Grafico "RAIZ', fontsize= 10)
    fig_4.set_ylabel('Eje Y - Grafico 4', fontsize= 6)
    fig_4.set_xlabel('Eje X - Grafico 4', fontsize= 6)
    fig_4.legend('Y= np.sqrt(x)')

    plt.show()

    print("terminamos")