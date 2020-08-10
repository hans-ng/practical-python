import unittest
import stock

class TestStock(unittest.TestCase):
    def setUp(self):
        self.s = stock.Stock('GOOG', 100, 490.1)

    def test_create(self):
        self.assertEqual(self.s.name, 'GOOG')
        self.assertEqual(self.s.shares, 100)
        self.assertEqual(self.s.price, 490.1)

    def test_cost(self):
        self.assertEqual(self.s.cost, 49010.0)

    def test_sell(self):
        self.s.sell(20)
        self.assertEqual(self.s.shares, 80)

    def test_bad_shares(self):
        with self.assertRaises(TypeError):
            self.s.shares = '100'

if __name__ == '__main__':
    unittest.main()