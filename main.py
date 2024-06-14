import time

from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)


    while not win.should_stop():
        m = Maze(100, 100, 8, 12, 50, 50, win)
        m.solve()

        if not win.should_stop():
            time.sleep(5)
            win.reset()

    #win.wait_for_close()


if __name__ == '__main__':
    main()
