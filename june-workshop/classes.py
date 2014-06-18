### Object Oriented programming
import datetime
from collections import defaultdict

"""
- Create a Person class with `first_name`, `last_name`, `organization` as attributes.
- Create a method `add_phone_numbers`, which appends phone numbers.
- Create a property `email`, `phone_numbers`.
"""

class Person(object):
    def __init__(self, first_name, last_name="", organization=""):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.organization = organization.strip()
        self.__phone_numbers = []
        self.__emails = []

    @property
    def phone_numbers(self):
        return self.__phone_numbers

    def add_phone_number(self, phone_number):
        return self.__phone_numbers.append(phone_number)

    @property
    def email(self):
        try:
            return self.__emails[-1]
        except IndexError:
            return ""

    def add_email(self, email):
        if '@' in email and '.' in email:
            self.__emails.append(email)
        else:
            raise Exception(u"Invalid email address {}".format(value))

    def get_emails(self):
        return self.__emails

"""
- Create a class `Address` which will have `pincode`, `full address`.
"""


class Address(object):
    '''Address contains pincode and full address'''
    def __init__(self, full_address="", pincode=""):
        self.full_address = full_address

        if pincode:
            if not isinstance(pincode, int):
                raise Exception("Pincode {} is not integer".format(pincode))
            if not len(str(pincode)) == 6:
                raise Exception("Pincode must be 6 digit")

        self.pincode = pincode

    def __repr__(self):
        return u"{}, pincode: {}".format(self.full_address, self.pincode)

"""
- Create a class `ExtraDetails` which has attributes `website`, `nickname`, `notes`.
"""


class ExtraDetails(object):
    """ExtraDetails which is some time useful like where you meet etc...
    """
    def __init__(self, website="", nickname="", notes=""):
        if website:
            if False in (website.startswith(("http", "www")),  '.' in website):
                raise Exception("{} is not valid url".format(website))

        self.website = website
        self.nickname = nickname
        self.notes = notes


"""
- Create class `Contact` which will inherit from `Person`, `ExtraDetails` and
composes of `Address`.

- Add a new attribute `special_dates` which is a dict where `key` is
occasion name and value is `date` object.
"""
class Contact(Person, ExtraDetails):
    """Contact class which contains details of a person, place etc...
    """
    def __init__(self, **kwargs):
        """
        Params for person:
        first_name, last_name, organization, phone_number, email

        Params for ExtraDetails:
        website, notes, nickname

        Params for Address :
        full_address, pincode
        """
        Person.__init__(self,
                        first_name=kwargs.get('first_name', ''),
                        last_name=kwargs.get('last_name', ''),
                        organization=kwargs.get('organization', ''))

        phone_number = kwargs.get('phone_number')
        if phone_number:
            self.add_phone_number(phone_number)

        email = kwargs.get('email')
        if email:
            self.add_email(email)

        ExtraDetails.__init__(self,
                              website=kwargs.get('website', ''),
                              notes=kwargs.get('notes', ''),
                              nickname=kwargs.get('nickname', ''))

        self.address = Address(full_address=kwargs.get('full_address', ''),
                               pincode=kwargs.get('pincode', ''))

        self.special_dates = {}

    def __repr__(self):
        return u"<{}'s contact detail's>".format(self.first_name)


"""
- Create a class called `ContactBook` and add a class method called `add` which
stores the contacts in attribute `contact` which is list`.

- Add a class method `index` which returns dict with keys as alphabets and values
as list of contact starting with the alphabet.

"""


class ContactBook(object):
    version = '0.1'
    objects = []

    @classmethod
    def add(cls, contact):
        cls.objects.append(contact)

    @classmethod
    def all(cls):
        return cls.objects

    @classmethod
    def index(cls):
        d = defaultdict(list)
        for contact in cls.all():
            d[contact.first_name[0].lower()].append(contact)
        return d


if __name__ == "__main__":
    contact = Contact(first_name="Kracekumar",
                      last_name="",
                      website="http://kracekumar.com",
                      notes="Co-host of bangpypers",
                      full_address="bellandhur gate, bangalore",
                      phone_number="8553029521",
                      email="me@kracekumar.com")
    contact.special_dates["mom's-bidrthay"] = datetime.date(1970, 02, 01)
    print vars(contact)
    ContactBook.add(contact)
    contact = Contact(first_name="Siva",
                      last_name="",
                      website="http://sivaa.in",
                      notes="Host of Bangalore Django User Group",
                      full_address="bellandhur gate, bangalore",
                      phone_number="786569",
                      email="sivaa@sivaa.in")
    ContactBook.add(contact)
    print ContactBook.all()
    print ContactBook.index()
