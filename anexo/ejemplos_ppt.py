#!/usr/bin/env python
'''
Matplotlib [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import matplotlib.pyplot as plt


def simple_plot():
    # Dibujar una recta y = 2x
    x = [0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
    y = []
    for i in x:
        y.append(2*i)

    plt.figure()
    plt.plot(x, y, color='m', marker='^')
    plt.show()

    # Dibujar una senoidal y = sin(x)
    x = np.linspace(start=0, stop=2*np.pi, num=100)
    y = np.sin(x)

    fig = plt.figure()      # Definir tamaño figura
    ax = fig.add_subplot()  # Definir cuantos gráficos tendrá

    ax.plot(x, y)           # Graficar con plot en mi gráfico "ax"
    ax.set_facecolor('whitesmoke')
    ax.set_title("Mi senoidal")
    ax.set_ylabel("Amplitud")
    ax.set_xlabel("[rad]")
    plt.show()              # Mostrar el gráfico


def multi_plot():
    # Dibujar múltiples líneas en un mismo gráfico
    x = np.linspace(start=0, stop=4*np.pi, num=100)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, np.sin(x), color='b', marker='^', label='y=sin(x)')
    ax.plot(x, 2*np.sin(x), color='c', marker='+', label='y=2*sin(x)')
    ax.plot(x, 3*np.sin(x), color='g', marker='.', label='y=3*sin(x)')
    ax.plot(x, 4*np.sin(x), color='k', label='y=4*sin(x)')
    ax.set_facecolor('whitesmoke')
    ax.set_title("Senoidales")
    ax.set_ylabel("Y[amplitud]")
    ax.set_xlabel("X[rads]")
    ax.set_xlim([0, 4*np.pi])  # Limito el eje "Y" entre 0 y 4*pi
    ax.set_ylim([-4, 4])       # Limito el eje "X" entre -4 y 4
    ax.legend()
    plt.show(block=False)

    # Dibujar 4 gráficos en una misma figura
    fig = plt.figure()
    # Ejemplo de uso --> ax = fig.add_subplot(nrows, ncols, index)
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1.plot(x, np.sin(x), color='b', marker='^', label='y=sin(x)')
    ax1.set_facecolor('whitesmoke')
    ax1.set_title("Senoidal1")
    ax1.set_ylabel("Y[amplitud]")
    ax1.set_xlabel("X[rads]")
    ax1.set_xlim([0, 4*np.pi])
    ax1.set_ylim([-4, 4])
    ax1.legend()

    ax2.plot(x, 2*np.sin(x), color='c', marker='+', label='y=2*sin(x)')
    ax2.set_facecolor('whitesmoke')
    ax2.set_title("Senoidal2")
    ax2.set_ylabel("Y[amplitud]")
    ax2.set_xlabel("X[rads]")
    ax2.set_xlim([0, 4*np.pi])
    ax2.set_ylim([-4, 4])
    ax2.legend()

    ax3.plot(x, 3*np.sin(x), color='g', marker='.', label='y=3*sin(x)')
    ax3.set_facecolor('whitesmoke')
    ax3.set_title("Senoidal3", position=(0.5, 0.85))  # h=center, v=top
    ax3.set_ylabel("Y[amplitud]")
    ax3.set_xlabel("X[rads]")
    ax3.set_xlim([0, 4*np.pi])
    ax3.set_ylim([-4, 4])
    ax3.legend()

    ax4.plot(x, 4*np.sin(x), color='k', label='y=4*sin(x)')
    ax4.set_facecolor('whitesmoke')
    ax4.set_title("Senoidal4", position=(0.5, 0.85))  # h=center, v=top
    ax4.set_ylabel("Y[amplitud]")
    ax4.set_xlabel("X[rads]")
    ax4.set_xlim([0, 4*np.pi])
    ax4.set_ylim([-4, 4])
    ax4.legend()

    # Graficar la figura con los 4 axes
    plt.show()


def marker_color():
    # Veremos para que sirven los "marker"
    # Supongamos que estoy midiendo la velocidad de un auto en diferentes
    # intervalos de tiempo en segundos, supongamos que realicé 4 mediciones
    # a 0seg, 1seg, 2seg y 3seg distintas velocidades en km/h:
    t = [0, 1, 2, 3]
    vel = [0, 10, 40, 40]

    # Realizaremos dos gráficos, uno sin marker y otro con marker
    # Dibujar 2 gráficos en una misma figura
    fig = plt.figure()
    fig.suptitle('Velocidad de un coche', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(t, vel)
    ax1.set_facecolor('whitesmoke')
    ax2.plot(t, vel, marker='^', mec='r', ms=10)
    ax2.set_facecolor('whitesmoke')
    plt.show(block=False)

    # Realizaremos dos gráficos, con distinto tipo de línea y color
    # Dibujar 2 gráficos en una misma figura
    fig = plt.figure()
    fig.suptitle('Velocidad de un coche', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(t, vel, color='r')
    ax1.set_facecolor('whitesmoke')
    ax2.plot(t, vel, c=(0, 0.5, 0.5), ls='--', lw='2')
    ax2.set_facecolor('whitesmoke')
    plt.show()


def grid():
    # Veremos los distintos tipos de grids
    x = range(-10, 10, 1)
    y = []
    for i in x:
        y.append(i**2)

    # Realizaremos dos gráficos, con distinto tipo de línea y color
    # Dibujar 2 gráficos en una misma figura
    fig = plt.figure()
    fig.suptitle('Función cuadrática', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y, color='darkred')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(ls='dashed')
    ax2.plot(x, y, c='darkgreen', ls='--')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls='dashdot')
    plt.show()


def line_plot():
    # Generaremos la función y=X^2 (x al cuadrado)
    x = range(-10, 11, 4)
    y = []
    for i in x:
        y.append(i**2)

    fig = plt.figure()
    fig.suptitle('Graficar Y=X**2', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(x, y, c='darkred', marker='*', label='y=x**2')
    ax.legend()
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show()


def scatter_plot():
    # Demostración de la utilidad del scatter plot
    # Generaremos una linea y=x con ruido sumando
    # valores aleatorios uniformes en cada punto
    sample_size = 20
    x = np.linspace(0, 10, sample_size)
    # A los valores de X sumar valores aleatoreos entre -1 y 1
    y = x + np.random.uniform(-1, 1, sample_size)

    fig = plt.figure()
    fig.suptitle('Line vs Scatter', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y, c='darkcyan')
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
    ax2.scatter(x, y, c='darkcyan')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show()

    np.random.shuffle(x)  # Mezclar valores de X
    # A los valores de X sumar valores aleatoreos entre -1 y 1
    y = x + np.random.uniform(-1, 1, sample_size)

    fig = plt.figure()
    fig.suptitle('Line vs Scatter', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y, c='darkmagenta')
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
    ax2.scatter(x, y, c='darkmagenta')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show()


def bar_plot():
    # Utilizar el gráfico de barras para comparar el consumo
    # de fruta por trimestre
    trimestres = ['En-Mar', 'Abr-Jun', 'Jul-Sep', 'Oct-Dic']
    fruta = [25, 23, 16, 21]

    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(trimestres, fruta, label='fruta')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()


def pie_plot():
    # Utilizar gráfico de torta para evaluar la distribución
    # Segmetar el consumo en una lista de diccionarios tal como
    # si hubiera venido de un archivo.
    # Ahora los trimestres van del 0 al 3
    consumo = {'carne': 20, 'fruta': 25, 'verdura': 22}

    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax = fig.add_subplot()

    ax.pie(consumo.values(), labels=consumo.keys(),
           autopct='%1.1f%%', shadow=True, startangle=90
           )
    # Igualo la relacion de aspecto para que se vea como un círculo
    ax.axis('equal')
    plt.show()

    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0)  # solo resaltar el consumo de carne

    ax.pie(consumo.values(), labels=consumo.keys(),
           explode=explode, autopct='%1.1f%%', shadow=True, startangle=90
           )
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ---- Introducción y personalización de gráficos ---- #
    simple_plot()
    multi_plot()
    #marker_color()
    grid()
    # ---------------- Tipos de gráficos ---------------- #
    line_plot()
    scatter_plot()
    bar_plot()
    #pie_plot()
