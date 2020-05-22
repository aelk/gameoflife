import unittest
from life import next_board_state, dead_state, count_live_neighbors

class LifeTest(unittest.TestCase):
    def test_no_neighbors(self):
        width, height = 2, 3
        state = dead_state(width, height)
        for i in range(width):
            for j in range(height):
                actual = count_live_neighbors(state, (i, j))
                self.assertEqual(0, actual)

    def test_one_neighbor(self):
        state = [
            [0, 0, 1],
            [1, 1, 0]
        ]
        actual = count_live_neighbors(state, (0, 2))
        self.assertEqual(1, actual)

    def test_next_empty(self):
        expected = dead_state(3, 4)
        actual = next_board_state(expected)
        self.assertEqual(expected, actual)

    def test_next_underpopulation(self):
        initial_state = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        expected_state = dead_state(3, 3)
        actual_state = next_board_state(initial_state)
        self.assertEqual(expected_state, actual_state)

    def test_next_alive(self):
        initial_state = [
            [1, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
        ]
        expected_state = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0],
        ]
        actual_state = next_board_state(initial_state)
        self.assertEqual(expected_state, actual_state)

    def test_next_overpopulation(self):
        initial_state = [
            [1, 0, 1],
            [1, 1, 0],
            [0, 0, 1],
        ]
        expected_state = [
            [1, 0, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        actual_state = next_board_state(initial_state)
        self.assertEqual(expected_state, actual_state)

    def test_next_reproduction(self):
        initial_state = [
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expected_state = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        actual_state = next_board_state(initial_state)
        self.assertEqual(expected_state, actual_state)

if __name__ == '__main__':
    unittest.main()
