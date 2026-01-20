import tkinter as tk

window = tk.Tk()
window.title("Label Example")
window.geometry("300x200")

label = tk.Label(window, text="Hello Sakshi!", font=("Arial", 16))
label.pack()

window.mainloop()
