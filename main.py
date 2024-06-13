from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    Cell(
        win,
        Point(150, 100),
        Point(200, 150)
    ).draw()

    Cell(
        win,
        Point(250, 100),
        Point(300, 150),
        has_bottom_wall=False
    ).draw()

    Cell(
        win,
        Point(150, 200),
        Point(200, 250),
        has_right_wall=False
    ).draw()

    Cell(
        win,
        Point(250, 200),
        Point(300, 250),
        has_left_wall=False
    ).draw()

    Cell(
        win,
        Point(350, 200),
        Point(400, 250),
        has_top_wall=False
    ).draw()

    Cell(
        win,
        Point(200, 400),
        Point(300, 500),
        has_left_wall=False,
        has_right_wall=False
    ).draw()

    Cell(
        win,
        Point(500, 400),
        Point(600, 500),
        has_top_wall=False,
        has_bottom_wall=False
    ).draw()

    win.wait_for_close()


if __name__ == '__main__':
    main()
