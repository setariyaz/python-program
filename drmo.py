import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Gym Member List")
root.geometry("600x400")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Plan", "Fees", "Join Date"), show="headings")

# Define column headings
tree.heading("Name", text="Member Name")
tree.heading("Plan", text="Plan Name")
tree.heading("Fees", text="Fees (₹)")
tree.heading("Join Date", text="Join Date")

# Set column widths
tree.column("Name", width=150)
tree.column("Plan", width=100)
tree.column("Fees", width=80, anchor="center")
tree.column("Join Date", width=120)

# Insert some example data
members = [
    ("Riya Seta", "Gold", "2000", "2025-01-10"),
    ("Amit Patel", "Silver", "1500", "2025-02-15"),
    ("Neha Shah", "Platinum", "3000", "2025-03-01"),
]

for member in members:
    tree.insert("", tk.END, values=member)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Place Treeview
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Run the GUI
root.mainloop()
