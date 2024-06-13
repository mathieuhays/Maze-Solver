from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_bottom_wall = False
    c1.draw(100, 100, 200, 200)

    c2 = Cell(win)
    c2.has_top_wall = False
    c2.has_right_wall = False
    c2.draw(100, 200, 200, 300)

    c3 = Cell(win)
    c3.has_left_wall = False
    c3.draw(200, 200, 300, 300)

    c1.draw_move(c2)
    c2.draw_move(c3, True)

    win.wait_for_close()


if __name__ == '__main__':
    main()
