import unittest
from classes import Contact, ContactBook, ExtraDetails


class ContactBookTestCase(unittest.TestCase):
    def setUp(self):
        self.krace = Contact(first_name="Kracekumar",
                             last_name="",
                             website="http://kracekumar.com",
                             notes="Co-host of bangpypers",
                             full_address="bellandhur gate, bangalore",
                             phone_number="8553029521",
                             email="me@kracekumar.com")
        self.siva = Contact(first_name="Siva",
                            last_name="",
                            website="http://sivaa.in",
                            notes="Host of Bangalore Django User Group",
                            full_address="bellandhur gate, bangalore",
                            phone_number="786569",
                            email="sivaa@sivaa.in")

        ContactBook.add(self.krace)
        ContactBook.add(self.siva)

    def test_contact_book_add(self):
        self.assertTrue(len(ContactBook.all()), 2)

    def test_index(self):
        res = ContactBook.index()
        self.assertTrue(len(res['k']), 1)
        self.assertTrue(len(res['s']), 1)


class ExtraDetailsTestCase(unittest.TestCase):
    def test_invalid_website_without_dot(self):
        with self.assertRaises(Exception):
            ExtraDetails(website="http://kracekumar")

    def test_invalid_website_without_scheme(self):
        with self.assertRaises(Exception):
            ExtraDetails(website="kracekumar.com")

if __name__ == "__main__":
    unittest.main()
