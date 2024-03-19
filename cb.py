class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_query):
        results = []
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == "2":
            print("\nContacts:")
            contact_book.view_contacts()

        elif choice == "3":
            search_query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_query)
            if results:
                print("\nSearch results:")
                for i, result in enumerate(results, start=1):
                    print(f"{i}. Name: {result.name}, Phone: {result.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                name = input("Enter new name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone_number, email, address)
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")

        elif choice == "5":
            index = int(input("Enter index of contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
