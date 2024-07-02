import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")

        # Create GUI components
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.contacts_listbox = tk.Listbox(self.root)
        self.contacts_listbox.pack(fill="both", expand=True)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        # Load contacts from file
        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            self.contacts_listbox.insert("end", f"{name} - {phone} - {email}")
            self.save_contacts()
            self.name_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.email_entry.delete(0, "end")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts_listbox.delete(selected_index)
            self.save_contacts()

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    self.contacts_listbox.insert("end", line.strip())
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for i in range(self.contacts_listbox.size()):
                file.write(self.contacts_listbox.get(i) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
