import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patches as patches
import numpy as np
from queens import *


def add_queen_icon(ax, position):
    queen_icon = plt.imread('./n_queens_problem/ico/3405_white-queen.png')
    imagebox = OffsetImage(queen_icon, zoom=0.12)
    ab = AnnotationBbox(imagebox, position, frameon=False)
    ax.add_artist(ab)


def display_chessboard(matrix):
    fig, ax = plt.subplots()
    for i in range(8):
        for j in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'black'
            rect = patches.Rectangle(
                (i, j), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    ax.set_xticks(np.arange(0, 8, 1))
    ax.set_yticks(np.arange(0, 8, 1))
    ax.grid(which='both', color='black', linestyle='-', linewidth=1.5)

    for i in range(TABLE_HEIGHT):
        for j in range(TABLE_WIDTH):
            if matrix[i][j] == 1:
                add_queen_icon(ax, (j+0.5, i+0.5))

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Solução - Problema das 8 Rainhas")
    plt.axis('off')
    plt.show()
