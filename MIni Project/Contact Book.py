print("\n--- 3. Mini-Project: Contact Book ---")
print("Features: Add, View, Search, Delete contacts. Saves to 'contacts.txt'.\n")

CONTACTS_FILE = "contacts.txt"

def save_contacts(contacts):
    """Save contacts to file with error handling."""
    try:
        with open(CONTACTS_FILE, "w") as file:
            for name, phone in contacts.items():
                file.write(f"{name}|{phone}\n")
        print("✅ Contacts saved successfully.")
    except Exception as e:
        print(f"❌ Error saving contacts: {e}")

def load_contacts():
    """Load contacts from file with error handling."""
    contacts = {}
    try:
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line and "|" in line:
                    name, phone = line.split("|", 1)
                    contacts[name] = phone
        print(f"✅ Loaded {len(contacts)} contacts.")
    except FileNotFoundError:
        print("ℹ️ No existing contacts file. Starting fresh.")
    except Exception as e:
        print(f"❌ Error loading contacts: {e}")
    return contacts

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    if name in contacts:
        print(f"⚠️ Contact '{name}' already exists! Updating...")
    
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("❌ Phone cannot be empty!")
        return
    
    contacts[name] = phone
    print(f"✅ Contact '{name}' added/updated!")
    save_contacts(contacts)

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("📭 No contacts found.")
        return
    
    print("\n--- Contact List ---")
    for name, phone in contacts.items():
        print(f"👤 {name}: {phone}")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"✅ Found: {name} -> {contacts[name]}")
    else:
        print(f"❌ Contact '{name}' not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"✅ Contact '{name}' deleted.")
        save_contacts(contacts)
    else:
        print(f"❌ Contact '{name}' not found.")

# Main Application Loop
def main():
    contacts = load_contacts()
    
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()