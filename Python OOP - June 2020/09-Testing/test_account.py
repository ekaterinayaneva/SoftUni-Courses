import types
import unittest

from polymorphism_and_magic_methods_6.account_TESTING import Account


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account('Ekaterina', 100)
        self.other = Account('Yordan', 200)
        self.third_account = Account('Test', 100)

    def test_add_transaction(self):
        self.account.add_transaction(50)
        self.account.add_transaction(100)
        self.assertEqual(self.account.balance, 250)
        self.assertEqual(len(self.account._transactions), 2)
        self.assertEqual(list(reversed(self.account)), [100, 50])

    def test_add_not_possible_transaction(self):
        with self.assertRaises(ValueError) as ex:
            self.account.add_transaction(50.5)

    def test_str(self):
        # result = str(self.account)
        # self.assertEqual(result, 'Account of Ekaterina with starting amount: 100')
        self.assertEqual(str(self.account), 'Account of Ekaterina with starting amount: 100')

    def test_repr(self):
        self.assertEqual(repr(self.account), f'Account(Ekaterina, 100)')

    def test_get_item(self):
        self.account.add_transaction(50)
        self.assertEqual(self.account[0], 50)

    # def test_get_item_error_index(self):
    #     with self.assertRaises(IndexError) as ex:
    #         self.assertEqual(self.account[0], 50)

    # def test_reversed(self):
    #     self.account.add_transaction(50)
    #     self.account.add_transaction(100)
    #     result = list(reversed(self.account))
    #     self.assertEqual(result, [100, 50])

    def test_gt_and_ge(self):
        self.assertGreater(self.other, self.account)
        self.assertGreaterEqual(self.account, self.third_account)

    def test_lt_and_le(self):
        self.assertLess(self.account, self.other)
        self.assertLessEqual(self.account, self.third_account)

    def test_eq(self):
        self.assertEqual(self.account, self.third_account)

    def test_ne(self):
        self.assertNotEqual(self.account, self.other)

    def test_validate_static_method(self):
        self.assertTrue((isinstance(self.account.validate_transaction, types.FunctionType)))

    def test_validate_transaction(self):
        result = self.account.validate_transaction(self.account, 50)
        self.assertEqual(result, 'New balance: 150')

    # def test_validate_not_possible_transaction(self):
    #     with self.assertRaises(ValueError) as ex:
    #         self.account.validate_transaction(self.account, -101)


if __name__ == '__main__':
    unittest.main()