import unittest
import start


class TestFunkyFinance(unittest.TestCase):
    def test_it_finds_i(self):
        arguments = {
            "p": 2000,
            "r": 1,
            "t": 10
        }
        result = start.solve_for_i(**arguments)
        self.assertEqual(result, "200")
        self.assertNotEqual(result, 200)

    def test_it_finds_t(self):
        arguments = {
            "p": 2000,
            "r": 1,
            "i": 200
        }
        result = start.solve_for_t(**arguments)
        self.assertEqual(result, "10")
        self.assertNotEqual(result, 10)

    def test_it_finds_r(self):
        arguments = {
            "p": 2000,
            "i": 200,
            "t": 10
        }
        result = start.solve_for_r(**arguments)
        self.assertEqual(result, "1")
        self.assertNotEqual(result, 1)

    def test_it_finds_p(self):
        arguments = {
            "r": 1,
            "i": 200,
            "t": 10
        }
        result = start.solve_for_p(**arguments)
        self.assertEqual(result, "2000")
        self.assertNotEqual(result, 2000)

    def test_it_gives_correct_solving_equation(self):
        returned_function = start.solve_equation(['r', 'i', 't'])
        self.assertEqual(returned_function, start.solve_for_p)

        returned_function = start.solve_equation(['r', 'i', 'p'])
        self.assertEqual(returned_function, start.solve_for_t)

        returned_function = start.solve_equation(['r', 'p', 't'])
        self.assertEqual(returned_function, start.solve_for_i)

        returned_function = start.solve_equation(['i', 'p', 't'])
        self.assertEqual(returned_function, start.solve_for_r)

    def test_it_is_numeric(self):
        is_numeric = start.is_valid_numeric("123")
        self.assertTrue(is_numeric)

        is_numeric = start.is_valid_numeric("123.32")
        self.assertTrue(is_numeric)

        is_not_numeric = start.is_valid_numeric("asdad")
        self.assertFalse(is_not_numeric)

        is_not_numeric = start.is_valid_numeric("12.325")
        self.assertFalse(is_not_numeric)


if __name__ == '__main__':
    unittest.main()
