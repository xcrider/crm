from faker import Faker
import time

fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    @property
    def label_length(self):
        return 1 + len(self.first_name) + len(self.last_name)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}"

    def __repr__(self):
        return f"BaseContact(first_name = {self.first_name})"

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")


class BusinessContact(BaseContact):

    def __init__(self, company, position, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position

    # def create_contacts(*args, **kwargs):

    #     fposition = fake.job
    #     fcompany = fake.company
    #     super().create_contacts(self, *args, **kwargs, company = fcompany, position = fposition)


def execuction_time(func):
    def wrapper(contact_type, number):
        start = time.time()
        result = func(contact_type, number)
        end = time.time()
        timer = end - start
        print(f"Execution time = {timer}")
        return result
    return wrapper

@execuction_time
def create_contacts(contact_type, number):

    contact_list = []

    for i in range(0, number):
        contact = contact_type(first_name = fake.first_name(), last_name = fake.last_name(), phone_number = fake.phone_number(), email = fake.email())
        contact_list.append(contact)
    return contact_list


if __name__ == "__main__":

    person1 = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), phone_number = fake.phone_number(), email = fake.email())
    person2 = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), phone_number = fake.phone_number(), email = fake.email())
    person3 = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), phone_number = fake.phone_number(), email = fake.email())
    person4 = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), phone_number = fake.phone_number(), email = fake.email())

    person_list = [person1, person2, person3, person4]

    bperson = BusinessContact(first_name = fake.first_name(), last_name = fake.last_name(), phone_number = fake.phone_number(), company = fake.company(), position = fake.job(),email = fake.email())    

    print("\n By first name: ")
    by_fname = sorted(person_list, key=lambda person: person.first_name)

    for person in by_fname:
        print(person)

    print("\n By last name: ")
    by_lname = sorted(person_list, key=lambda person: person.last_name)

    for person in by_lname:
        print(person)

    print("\n By email: ")
    by_email = sorted(person_list, key=lambda person: person.last_name)

    for person in by_email:
        print(person)

    print("\nWywołanie funkcji tworzecej kontakty: ")
    print(create_contacts(BaseContact, 1000))
