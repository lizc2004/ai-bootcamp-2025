class Directory:
    """A class to store contacts"""

    def __init__(self):
        self.contacts = []

    def __len__(self):
        return len(self.contacts)  # Restituisce il numero di elementi nella directory

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            full_name = f"{contact.name} {contact.surname}" if isinstance(contact, Person) else contact.name
            if full_name == name:
                return contact
        return None

    def query(self, name):
        results = []
        for contact in self.contacts:
            full_name = f"{contact.name} {contact.surname}" if isinstance(contact, Person) else contact.name
            if name in full_name:
                results.append(contact)
        return results

    def find(self, term):
        results = []
        for contact in self.contacts:
            full_name = f"{contact.name} {contact.surname}" if isinstance(contact, Person) else contact.name
            phone = contact.phone if isinstance(contact, Person) or isinstance(contact, Business) else None
            if term in full_name or (phone and term in phone):
                results.append(contact)
        return results

class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
