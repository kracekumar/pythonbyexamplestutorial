import unittest
from class_may import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        print "calling setup"
        self.person = Person(first_name="krace",
                             last_name="kumar",
                             age=24)
    def test_get_age(self):
        self.assertEqual(self.person.get_age(), 24)

    def test_is_major(self):
        self.assertTrue(self.person.is_major())

if __name__ == "__main__":
    unittest.main()

