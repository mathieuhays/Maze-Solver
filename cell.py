from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self._win = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self._x1 = min(x1, x2)
        self._x2 = max(x1, x2)
        self._y1 = min(y1, y2)
        self._y2 = max(y1, y2)
        if self.has_left_wall:
            self._win.draw_line(Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
            ))
        if self.has_top_wall:
            self._win.draw_line(Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
            ))
        if self.has_right_wall:
            self._win.draw_line(Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2)
            ))
        if self.has_bottom_wall:
            self._win.draw_line(Line(
                Point(self._x2, self._y2),
                Point(self._x1, self._y2)
            ))

    def get_center_point(self):
        return Point(
            self._x1 + ((self._x2 - self._x1)/2),
            self._y1 + ((self._y2 - self._y1)/2)
        )

    def draw_move(self, to_cell, undo=False):
        local_point = self.get_center_point()
        to_point = to_cell.get_center_point()
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(Line(local_point, to_point), fill_color)
