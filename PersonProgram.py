import PersonClass as p


def main():

    name = 'John'
    address = '1234 Main St'
    phone_number = '111-222-3333'
    cust_no = 1234
    on_list_flag = False

    john_person = p.Person(name, address, phone_number, cust_no, on_list_flag)

    john_customer = p.Customer(
        name, address, phone_number, cust_no, on_list_flag)

    john_person.print_person()

    print()
    print()

    john_customer.print_person()


main()
