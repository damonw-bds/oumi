class ContactManager:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone_number': phone_number, 'email': email}
    
    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")
    
    def update_contact(self, name, phone_number, email):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email}
        else:
            print("Contact not found")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

# Create an instance of ContactManager
contacts_manager = ContactManager()

# Add some contacts
contacts_manager.add_contact('Alice', '1234567890', 'alice@example.com')
contacts_manager.add_contact('Bob', '9876543210', 'bob@example.com')

# Display a contact
print(contacts_manager.get_contact('Alice'))

# Update a contact
contacts_manager.update_contact('Alice', '5555555555', 'newalice@example.com')
print(contacts_manager.get_contact('Alice'))

# Delete a contact
contacts_manager.delete_contact('Bob')
print(contacts_manager.get_contact('Bob'))  # Should show 'Contact not found'