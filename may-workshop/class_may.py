# -*- coding: utf-8 -*-

# Create a new class called Person which has attributes
# like first_name, last_name, age. Add a method called is_major
# which will return True if age > 18
class Person(object):
    def __init__(self, first_name, age, last_name=None, *args, **kwargs):
        self.first_name = first_name
        self.__age = age
        self.last_name = last_name
    
    def get_age(self):
        return self.__age

    def is_major(self):
        return self.get_age() >= 18

        
# Test is_major using unittest

class Customer(Person):
    def __init__(self, first_name, age, email, last_name=None):
        super(Customer, self).__init__(first_name=first_name,
                                       last_name=last_name,
                                       age=age)
        self.email = email



    
# Create a new class called Address with attributes street, state,
# country, pincode. Consider pincode can be only six digit
# Write a method is_valid_pincode which will return True if
# pincode is 6 digit

# write a method called get_full_address which concatenates street, state,
# country, pincode


bit.ly/pymay14




# Test is_valid_pincode

# Create a new class ContactInfo with attributes like phone_no, email.
# phone_no can be None


# Create a new class Customer which inherits from Person and composes of Address
# and ContactInfo.


# For the next exercise, create a new virtualenv and install requests inside it.

# Create a new class called Twitter which will have two attributes url and
# handle. Write a method called get_tweets which will make http request and get
# latest tweets.

# Add a class variable children to keep track of all objects created.



def main():
    # person = Person(first_name="krace", last_name="kumar", age=24)
    # print person.first_name
    # print person.last_name
    # print person.get_age()
    # print person.is_major()
    cust = Customer(first_name="krace",
                    last_name="kumar",
                    age=24,
                    email="me2example.com")
    print Customer.mro()
    print cust.first_name, cust.get_age(), cust.email


if __name__ == "__main__":
    main()












