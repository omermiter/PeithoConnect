import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from open_and_contact import create_list_and_run


root = tk.Tk()
root.geometry("400x400")
root.columnconfigure(0, weight=1)
first_run = True

mainframe = ttk.Frame(root, padding=(30,10))
mainframe.grid(column=0, row=0)


def select_file():
    filetypes = (
    ('text files', '*.csv'),
    ('All files', '*.*')
    )
        
    filename = fd.askopenfilename(
    title='Open a file',
    initialdir='/',
    filetypes=filetypes)
    file.set(str(filename))
    print(file.get())


def start():
    create_list_and_run(str(file.get()), first_run, username= str(username_entry.get()), password= str(password_entry.get()))



file = tk.StringVar()

username_label = ttk.Label(mainframe,text="Instagram Username: ", padding=(10,10))
username_label.grid(column=0, row=0, sticky="W")

username_entry = ttk.Entry(mainframe)
username_entry.grid(column=1, row=0, sticky="W")

password_label = ttk.Label(mainframe,text="Instagram Password: ", padding=(10,10))
password_label.grid(column=0, row=1, sticky="W")

password_entry = ttk.Entry(mainframe)
password_entry.grid(column=1, row=1, sticky="W")

select_file_btn = ttk.Button(text="Choose File", padding=(10,10), command=select_file)
select_file_btn.grid(column=0, row=2, sticky="S")

start_btn = ttk.Button(text="Start", padding=(10,10), command=start)
start_btn.grid(column=0, row=3, sticky="S")




root.mainloop()