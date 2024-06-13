from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(150, 100, 200, 150)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(250, 100, 300, 150)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(150, 200, 200, 250)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(250, 200, 300, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(350, 200, 400, 250)

    c = Cell(win)
    c.has_left_wall = False
    c.has_right_wall = False
    c.draw(200, 400, 300, 500)

    c = Cell(win)
    c.has_top_wall = False
    c.has_bottom_wall = False
    c.draw(500, 400, 600, 500)

    win.wait_for_close()


if __name__ == '__main__':
    main()
