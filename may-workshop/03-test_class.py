# -*- coding: utf-8 -*-

import unittest
from class_sol import Person, Address, Github


class TestPerson(unittest.TestCase):
    def test_is_major(self):
        p = Person("kracekumar", "ramaraju", 24)
        self.assertTrue(p.is_major())


class TestAddress(unittest.TestCase):
    def test_is_valid_pincode_with_blr_pincode(self):
        a = Address("Dollar street, Bangalore", "Karnataka", "560102")
        self.assertTrue(a.is_valid_pincode())

    def test_is_valid_pincode_with_invalid_pincode(self):
        a = Address("Dollar street, Bangalore", "Karnataka", 5601020)
        self.assertFalse(a.is_valid_pincode())


class TestGithub(unittest.TestCase):
    def setUp(self):
        self.github = Github("kracekumar")
                
    def test_get_user_info(self):
        self.assertIsInstance(self.github.get_user_info(), dict)
    
    def test_get_repos(self):
        self.assertIsInstance(self.github.get_repos(), list)
    
    def test_fetch_email(self):
        self.github.fetch_email()
        self.assertTrue(self.github.email, "kracethekingmaker@gmail.com")

    def test_children(self):
        g = Github("pythonindia")
        self.assertTrue(len(Github.children_ref), 2)


if __name__ == "__main__":
    unittest.main()





