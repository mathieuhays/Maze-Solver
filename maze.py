import random
import time
from cell import Cell

neighbor_directions = [
    (0, -1),  # top
    (1, 0),  # right
    (0, 1),  # bottom
    (-1, 0),  # left
]

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j, 0.01)

    def _draw_cell(self, i, j, sleep_s=0.1):
        x = self._x1 + (i * self._cell_size_x)
        y = self._y1 + (j * self._cell_size_y)
        self._cells[i][j].draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate(sleep_s)

    def _animate(self, sleep_s=0.1):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(sleep_s)

    def _break_entrance_and_exit(self):
        exit_x = self._num_cols - 1
        exit_y = self._num_rows - 1
        self._cells[0][0].has_top_wall = False
        self._cells[exit_x][exit_y].has_bottom_wall = False
        self._draw_cell(0, 0, 0.01)
        self._draw_cell(exit_x, exit_y, 0.01)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            possible_directions = []

            for dx, dy in neighbor_directions:
                cx = i + dx
                cy = j + dy

                if cx < 0 or cx >= self._num_cols:
                    continue
                if cy < 0 or cy >= self._num_rows:
                    continue
                if self._cells[cx][cy].visited:
                    continue

                possible_directions.append((dx, dy))

            if len(possible_directions) == 0:
                self._draw_cell(i, j, 0.02)
                return

            chosen = random.randrange(len(possible_directions))
            direction = possible_directions[chosen]
            next_cell = self._cells[i + direction[0]][j + direction[1]]

            if direction[0] == -1:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction[0] == 1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif direction[1] == -1:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction[1] == 1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False

            self._break_walls_r(i + direction[0], j + direction[1])

    def _reset_cells_visited(self):
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._cells[x][y].visited = False

    def solve(self):
        result = self._solve_r(0, 0)

        if result:
            self._cells[self._num_cols-1][self._num_rows-1].draw_end()
            self._animate()

        return result

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if self._win.should_stop():
            return True

        if i == 0 and j == 0:
            current.draw_start()
            self._animate()

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            # end cell, bottom right
            return True

        for dx, dy in neighbor_directions:
            cx = i + dx
            cy = j + dy

            if cx < 0 or cx >= self._num_cols:
                continue
            if cy < 0 or cy >= self._num_rows:
                continue

            new = self._cells[cx][cy]

            if new.visited:
                continue
            if dx == -1 and (current.has_left_wall or new.has_right_wall):
                continue
            if dx == 1 and (current.has_right_wall or new.has_left_wall):
                continue
            if dy == -1 and (current.has_top_wall or new.has_bottom_wall):
                continue
            if dy == 1 and (current.has_bottom_wall or new.has_top_wall):
                continue

            current.draw_move(new)

            result = self._solve_r(cx, cy)
            if result is True:
                return True

            self._animate()
            current.draw_move(new, True)

        return False
