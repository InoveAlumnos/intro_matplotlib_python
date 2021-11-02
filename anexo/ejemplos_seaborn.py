#!/usr/bin/env python
'''
Seaborn [Python]
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
import matplotlib.gridspec as gridspec

# Para usar seabor, primero tienen que usar:
# pip3 install seaborn 
import seaborn as sns

# Defino el estilo para todos los gráficos
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def line_plot():
    # Demostracion de line plot junto con gird layout
    gs = gridspec.GridSpec(2, 2)     # (row, col)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
    ax2 = fig.add_subplot(gs[0, 1])  # row 0, col 1
    ax3 = fig.add_subplot(gs[1, :])  # row 1, toma todas las col

    x = np.linspace(0, 4*np.pi, 100)

    sns.lineplot(x=x, y=np.sin(x), color='darkgreen', label='y=sin(x)', ax=ax1)
    ax1.legend()

    sns.lineplot(x=x, y=np.sin(2*x), color='darkblue', label='y=sin(2*x)', ax=ax2)
    ax2.legend()

    sns.lineplot(x=x, y=np.sin(2*x) + np.sin(x), color='gold',
                 label='y=sin(2*x) + sin(x)', ax=ax3
                 )
    ax3.legend()
    plt.show()


def scatter_plot():
    # Demostración de la utilidad del scatter plot
    # Generaremos una linea y=x con ruido sumando
    # valores aleatorios uniformes en cada punto
    sample_size = 20
    x = np.linspace(0, 10, sample_size)
    y = x + np.random.uniform(-1, 1, sample_size)

    fig = plt.figure()
    fig.suptitle('Line vs Scatter', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    sns.lineplot(x=x, y=y, color='darkcyan', ax=ax1)
    sns.scatterplot(x=x, y=y, color='darkcyan', ax=ax2)
    plt.show(block=False)

    np.random.shuffle(x)
    y = x + np.random.uniform(-1, 1, sample_size)

    fig = plt.figure()
    fig.suptitle('Line vs Scatter', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    sns.lineplot(x=x, y=y, color='darkmagenta', ax=ax1)
    sns.scatterplot(x=x, y=y, color='darkmagenta', ax=ax2)
    plt.show()


def bar_plot():
    # Utilizar el gráfico de barras para comparar el consumo
    # de productos por trimestre
    trimestres = [1, 2, 3, 4]
    trimestres_label = ['En-Mar', 'Abr-Jun', 'Jul-Sep', 'Oct-Dic']
    carne = [20, 23, 30, 26]
    fruta = [25, 23, 16, 21]
    verdura = [22, 18, 15, 20]

    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    sns.barplot(x=trimestres, y=carne, label='carne', ax=ax1)
    ax1.set_facecolor('whitesmoke')
    ax1.legend()

    sns.barplot(x=trimestres, y=fruta, label='fruta', palette="pastel", ax=ax2)
    ax2.set_facecolor('whitesmoke')
    ax2.legend()

    sns.barplot(x=trimestres, y=verdura, label='verdura', palette='husl', ax=ax3)
    ax3.set_facecolor('whitesmoke')
    ax3.legend()
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ---------------- Tipos de gráficos ---------------- #
    line_plot()
    scatter_plot()
    bar_plot()
    # --------------------------------------------------- #
