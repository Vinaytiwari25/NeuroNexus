class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                print("------------------------")

    def search_contact(self, keyword):
        results = [(name, details) for name, details in self.contacts.items() if keyword.lower() in name.lower()]
        if not results:
            print(f"No contacts found with the keyword '{keyword}'.")
        else:
            print("\nSearch Results:")
            for name, details in results:
                print(f"Name: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                print("------------------------")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['Phone'] = phone
            if email:
                self.contacts[name]['Email'] = email
            if address:
                self.contacts[name]['Address'] = address
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found in the contact book.")

def user_interface():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter a name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter the new phone number (press Enter to skip): ")
            email = input("Enter the new email address (press Enter to skip): ")
            address = input("Enter the new address (press Enter to skip): ")
            contact_book.update_contact(name, phone, email, address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

user_interface()
