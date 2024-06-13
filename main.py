from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(500, 500)), "red")
    win.draw_line(Line(Point(50, 90), Point(700, 200)), "black")
    win.wait_for_close()


if __name__ == '__main__':
    main()
