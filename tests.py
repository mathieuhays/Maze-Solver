import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m._cells[0][0].has_top_wall)
        self.assertFalse(m._cells[9][9].has_bottom_wall)

    def test_maze_reset_visited(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m._cells[0][0].visited)
        self.assertFalse(m._cells[5][5].visited)



if __name__ == "__main__":
    unittest.main()
