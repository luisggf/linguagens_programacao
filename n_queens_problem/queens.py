import random
from itertools import product

TABLE_WIDTH = 8
TABLE_HEIGHT = 8
NUM_QUEENS = 8


class Queens:
    def __init__(self, table):
        self.table = table

    def solve_n_queen(self):
        if NUM_QUEENS > 8 or NUM_QUEENS <= 0:
            return
        while 1:
            combinations = list(product(range(8), repeat=2))
            random.shuffle(combinations)
            placed_queens = 0
            self.table = generate_table()
            for comb in combinations:
                width_pos = comb[0]
                height_pos = comb[1]
                combinations.remove((width_pos, height_pos))
                if self.is_safe(width_pos, height_pos):
                    self.table[width_pos][height_pos] = 1
                    placed_queens += 1
                if placed_queens == NUM_QUEENS:
                    return self.table

    def is_safe(self, width, height):
        for i in range(TABLE_WIDTH):
            for j in range(TABLE_HEIGHT):
                if self.table[i][j] == 1:
                    if i == width or j == height:
                        return False
                    if abs(i - width) == abs(j - height):
                        return False
        return True


def generate_table():
    table = []
    for _ in range(TABLE_WIDTH):
        row = []
        for _ in range(TABLE_HEIGHT):
            row.append(0)
        table.append(row)
    return table
