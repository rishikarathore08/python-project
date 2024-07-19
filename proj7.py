# A contact book
import json
import os 

class Contact:
    def __init__(self,name, phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
            return {"name": self.name, "phone": self.phone, "email": self.email}

    @staticmethod
    def from_dict(contact_dict):
        return contact(contact_dict['name'],contact_dict['phone'],contact_dict['email'])

    def __str__(self):
        return f"Name: {self.name},Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self,file_name='contacts.json'):
        self.file_name = file_name
        self.contact = self.load_contacts()

    def load_contacts(self):
     if os.path.exists(self,file_name):
        with open(self,file_name, 'r') as file :
            contact_list = json.load(file)
            return[Contact.from_dict(contact) for contact in contacts_list]
    return []

def save_contacts(self):
    with open(self,file_name, 'w')as file:
        json.dump([contact.to_dict() for contact in self.contacts],file)

def add_contact(self,name,phone,email):
    new_contact = [contact for contact in self.contact if name.lower() in contact.name.lower()]
    self.contacts.append(new_contact)
    self.save_contacts()
    print(f"Contact {name} added.")

def search_contact(self,name):
    found_contacts
    if not found_contacts:
        print(f"No contacts found with the name {name}.")
    else:
        for contact in found_contacts:
            print(contact)

def delete_contact(self,name ):
    contact_to_delete = None
    for contact in self.contact:
        if contact.name.lower() == name.lower():
            contact_to_delete =  contact
            break
    if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            self.save_contact()
            print(f"contact {name} deleted.")
    else:
        print(f"contact {name} not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\ncontact Book Menu:")
        print("1.Add Contact")
        print("2.Search Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter yourchoice:")

        if choice == '1':
            name = input("Enter name:")
            phone = input("Enter phone number:")
            email = input("enter email:")
            contact_book.add_contact(name,phone,email)
        elif choice == '2':
            name = input("Enter name to seach:")
            contact_book.search_contact(name)
        elif choice == '3':
            name = input("Enter name to search:")
            contact_book.search_contact(name)
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice.Please try again.")

if __name__ == "__main__":
                main()




