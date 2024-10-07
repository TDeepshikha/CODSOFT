class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contacts:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

    def run(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Delete Contact")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                self.add_contact(name, phone)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                name = input("Enter contact name to delete: ")
                self.delete_contact(name)
            elif choice == '4':
                print("Exiting the contact book.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
