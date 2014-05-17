# -*- coding: utf-8 -*-

# Create a new class called Person which has attributes
# like first_name, last_name, age. Add a method called is_major
# which will return True if age > 18

import requests


class Person:
    def __init__(self, first_name, last_name=None, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_major(self):
        return self.age >= 18

# Test is_major using unittest


# Create a new class called Address with attributes street, state,
# country, pincode. Consider pincode can be only six digit

class Address(object):
    def __init__(self, street, state, pincode):
        self.street = street
        self.state = state
        self.pincode = str(pincode)

    def is_valid_pincode(self):
        try:
            int(self.pincode)
        except:
            return False
        return len(self.pincode) == 6

    def get_full_address(self):
        return "{}\n{}\n{}\n".format(self.street, self.state, self.pincode)


# Write a method is_valid_pincode which will return True if
# pincode is 6 digit

# write a method called get_full_address which concatenates street, state,
# country, pincode


# Test is_valid_pincode

# Create a new class ContactInfo with attributes like phone_no, email.
# phone_no can be None

class ContactInfo(object):
    def __init__(self, email, phone_no=None):
        self.email = email
        self.phone_no = phone_no

# Create a new class Customer which inherits from Person and composes of Address
# and ContactInfo.


class Customer(Person):
    def __init__(self, first_name, last_name=None, age=0, street="",
                 state="", pincode="", email="", phone_no=""):
        super(Person, self).__init__(first_name, last_name, age)
        self.address = Address(street=street, state=state, pincode=pincode)
        self.contact_info = ContactInfo(email, phone_no)

    @property
    def email(self):
        return self.contact_info.email
    
    @email.setter
    def email(self, value):
        self.contact_info.email = value

    @email.deleter
    def email(self):
        del self.contact_info.email

# For the next exercise, create a new virtualenv and install requests inside it.

# Create a new class called Github which will have username and base url as attributes.
# Write get_user_info and get_repos which will make http request and get required details
# https://api.github.com/users/{username} => Userinfo
# https://api.github.com/users/{username}/repos


class Github(object):
    children_ref = []

    @staticmethod
    def children(child):
        Github.children_ref.append(child)

    def __init__(self, username):
        self.username = username
        Github.children(self)

    def get_user_info(self):
        result = requests.get("https://api.github.com/users/{}".format(self.username))
        if result.status_code == 200:
            return result.json()
        raise Exception("Github returned {}".format(r.status_code))

    def get_repos(self):
        result = requests.get("https://api.github.com/users/{}/repos".format(self.username))
        if result.status_code == 200:
            return result.json()
        raise Exception("Github returned {}".format(r.status_code))

    def fetch_email(self):
        self.email = self.get_user_info().get('email', '')
# Add a class variable children to keep track of all objects created.

def main():
    pass


if __name__ == "__main__":
    main()

