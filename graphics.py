from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__request_closing = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def should_stop(self):
        return self.__request_closing

    def close(self):
        self.__running = False
        self.__request_closing = True

    def draw_line(self, line, fill_color="black", width=2):
        line.draw(self.__canvas, fill_color, width)

    def reset(self):
        self.__canvas.delete("all")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color="black", width=2):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=width)
