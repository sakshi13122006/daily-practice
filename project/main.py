import tkinter as tk
from tkinter import ttk, messagebox
from asset_module import Asset
import logic
import re

logic.connect_db()

root = tk.Tk()
root.title("IT Asset Management System")
root.geometry("650x500")
root.resizable(False, False)

font = ("Segoe UI", 10)

def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    brand_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def valid_date(date):
    return re.match(r"\d{4}-\d{2}-\d{2}", date)

def add_asset_ui():
    if not valid_date(date_entry.get()):
        messagebox.showerror("Error", "Date format: YYYY-MM-DD")
        return

    asset = Asset(
        int(id_entry.get()),
        name_entry.get(),
        type_combo.get(),
        brand_entry.get(),
        status_combo.get(),
        date_entry.get()
    )
    logic.add_asset(asset)
    messagebox.showinfo("Success", "Asset Added")
    clear_fields()

def delete_asset_ui():
    logic.delete_asset(int(id_entry.get()))
    messagebox.showinfo("Deleted", "Asset Deleted")
    clear_fields()

def search_asset_ui():
    data = logic.search_asset(int(id_entry.get()))
    if data:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, data[1])
        type_combo.set(data[2])
        brand_entry.delete(0, tk.END)
        brand_entry.insert(0, data[3])
        status_combo.set(data[4])
        date_entry.delete(0, tk.END)
        date_entry.insert(0, data[5])
    else:
        messagebox.showerror("Not Found", "Asset not found")

# -------- Dashboard --------
def open_dashboard():
    win = tk.Toplevel(root)
    win.title("Dashboard")
    win.geometry("350x250")

    total, working, repair, disposed = logic.dashboard_counts()

    tk.Label(win, text="Dashboard", font=("Segoe UI", 14, "bold")).pack(pady=10)
    tk.Label(win, text=f"Total Assets: {total}", font=font).pack(pady=5)
    tk.Label(win, text=f"Working: {working}", font=font).pack(pady=5)
    tk.Label(win, text=f"In Repair: {repair}", font=font).pack(pady=5)
    tk.Label(win, text=f"Disposed: {disposed}", font=font).pack(pady=5)

# -------- View All Assets --------
def view_assets():
    win = tk.Toplevel(root)
    win.title("All Assets")
    win.geometry("700x300")

    cols = ("ID", "Name", "Type", "Brand", "Status", "Date")
    tree = ttk.Treeview(win, columns=cols, show="headings")

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in logic.fetch_all_assets():
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

# -------- UI --------
tk.Label(root, text="IT Asset Management System",
         font=("Segoe UI", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

labels = ["Asset ID", "Name", "Type", "Brand", "Status", "Purchase Date"]
for i, text in enumerate(labels):
    tk.Label(frame, text=text, font=font).grid(row=i, column=0, sticky="w", pady=3)

id_entry = tk.Entry(frame)
id_entry.grid(row=0, column=1)

name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1)

type_combo = ttk.Combobox(frame, values=["Computer", "Laptop", "Printer", "Router", "Other"])
type_combo.grid(row=2, column=1)
type_combo.current(0)

brand_entry = tk.Entry(frame)
brand_entry.grid(row=3, column=1)

status_combo = ttk.Combobox(frame, values=["Working", "In Repair", "Disposed"])
status_combo.grid(row=4, column=1)
status_combo.current(0)

date_entry = tk.Entry(frame)
date_entry.insert(0, "YYYY-MM-DD")
date_entry.grid(row=5, column=1)

btns = tk.Frame(root)
btns.pack(pady=15)

tk.Button(btns, text="Add", width=12, command=add_asset_ui).grid(row=0, column=0, padx=5)
tk.Button(btns, text="Search", width=12, command=search_asset_ui).grid(row=0, column=1, padx=5)
tk.Button(btns, text="Delete", width=12, command=delete_asset_ui).grid(row=0, column=2, padx=5)

extra = tk.Frame(root)
extra.pack(pady=10)

tk.Button(extra, text="Dashboard", width=15, command=open_dashboard).grid(row=0, column=0, padx=10)
tk.Button(extra, text="View All Assets", width=15, command=view_assets).grid(row=0, column=1, padx=10)

root.mainloop()
