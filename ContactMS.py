import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts_listbox.insert(tk.END, f"{name}, {phone}, {email}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Information", "Please fill in all fields.")

def delete_contact():
    try:
        index = contacts_listbox.curselection()
        contacts_listbox.delete(index)
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")


root = tk.Tk()
root.title("Contact Management System")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)


add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=0, columnspan=2, pady=10)

contacts_listbox = tk.Listbox(root, width=40)
contacts_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
