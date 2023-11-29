import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.label = tk.Label(root, text="Contact Book", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts found.")
        else:
            contact_list = "\n".join([f"{i+1}. {contact['Name']} - {contact['Phone']} - {contact['Email']}" for i, contact in enumerate(self.contacts)])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        name_to_search = self.name_entry.get().strip()
        if name_to_search:
            found_contacts = [contact for contact in self.contacts if contact['Name'].lower() == name_to_search.lower()]
            if found_contacts:
                contact_list = "\n".join([f"{i+1}. {contact['Name']} - {contact['Phone']} - {contact['Email']}" for i, contact in enumerate(found_contacts)])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("No Results", "No contacts found with the specified name.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name to search.")

    def update_contact(self):
        name_to_update = self.name_entry.get().strip()
        if name_to_update:
            for contact in self.contacts:
                if contact['Name'].lower() == name_to_update.lower():
                    contact['Phone'] = self.phone_entry.get().strip()
                    contact['Email'] = self.email_entry.get().strip()
                    messagebox.showinfo("Success", f"Contact '{name_to_update}' updated successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("No Results", f"No contacts found with the specified name '{name_to_update}'.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name to update.")

    def delete_contact(self):
        name_to_delete = self.name_entry.get().strip()
        if name_to_delete:
            for i, contact in enumerate(self.contacts):
                if contact['Name'].lower() == name_to_delete.lower():
                    del self.contacts[i]
                    messagebox.showinfo("Success", f"Contact '{name_to_delete}' deleted successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("No Results", f"No contacts found with the specified name '{name_to_delete}'.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
