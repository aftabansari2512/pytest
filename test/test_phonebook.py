import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):


    # This is run every time a test is set up
    def setUp(self) -> None:
        # this will be now created for each test cases, so no need to create instance in every test function
        # rather use self.phonebook
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Aftab", 12345)

        number = self.phonebook.lookup("Aftab")

        self.assertEqual(number, 12345)


    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

