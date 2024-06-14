from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self._win = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = min(x1, x2)
        self._x2 = max(x1, x2)
        self._y1 = min(y1, y2)
        self._y2 = max(y1, y2)

        if self._win is None:
            return

        default_color = "white"
        active_color = "black"

        left_wall_color = default_color
        top_wall_color = default_color
        right_wall_color = default_color
        bottom_wall_color = default_color

        if self.has_left_wall:
            left_wall_color = active_color
        if self.has_top_wall:
            top_wall_color = active_color
        if self.has_right_wall:
            right_wall_color = active_color
        if self.has_bottom_wall:
            bottom_wall_color = active_color

        self._win.draw_line(Line(
            Point(self._x1, self._y1),
            Point(self._x1, self._y2)
        ), left_wall_color)
        self._win.draw_line(Line(
            Point(self._x1, self._y1),
            Point(self._x2, self._y1)
        ), top_wall_color)
        self._win.draw_line(Line(
            Point(self._x2, self._y1),
            Point(self._x2, self._y2)
        ), right_wall_color)
        self._win.draw_line(Line(
            Point(self._x2, self._y2),
            Point(self._x1, self._y2)
        ), bottom_wall_color)

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
