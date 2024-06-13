from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2)


class Cell:
    def __init__(
            self,
            window,
            p1,
            p2,
            has_left_wall=True,
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True
    ):
        self.__window = window
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(
                Point(self.__x1, self.__y1),
                Point(self.__x1, self.__y2)
            ))
        if self.has_top_wall:
            self.__window.draw_line(Line(
                Point(self.__x1, self.__y1),
                Point(self.__x2, self.__y1)
            ))
        if self.has_right_wall:
            self.__window.draw_line(Line(
                Point(self.__x2, self.__y1),
                Point(self.__x2, self.__y2)
            ))
        if self.has_bottom_wall:
            self.__window.draw_line(Line(
                Point(self.__x2, self.__y2),
                Point(self.__x1, self.__y2)
            ))
