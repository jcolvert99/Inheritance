class Person:

    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Phone Number:', self.__phone_number)


class Customer(Person):
    def __init__(self, name, address, phone_number, cust_no, mailing_list):
        Person.__init__(self, name, address, phone_number)

        self.__cust_no = cust_no
        self.__mailing_list = mailing_list

    # polymorphism
    def print_person(self):
        Person.print_person(self)
        print('Customer Number:', self.__cust_no)
        if self.__mailing_list:
            print('On mailing list: Yes')
        else:
            print('On mailing list: No')
