from tkinter import *
import backend

selected_row = []

def selected(event):
    global selected_row
    index = listbox.curselection()[0]
    selected_row = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_row[1])
    e2.delete(0, END)
    e2.insert(END, selected_row[2])
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    e4.delete(0, END)
    e4.insert(END, selected_row[4])
    e5.delete(0, END)
    e5.insert(END, selected_row[5])
    e6.delete(0, END)
    e6.insert(END, selected_row[6])

def delete_cmd():
    backend.delete(selected_row[0])  # Pass the ID of the selected row to the delete function

def view_cmd():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)

def search_cmd():
    listbox.delete(0, END)
    for row in backend.search(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get()):
        listbox.insert(END, row)

def add_cmd():
    backend.insert(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get())
    listbox.delete(0, END)
    view_cmd()  # Call the view_cmd() function to refresh the listbox

win = Tk()
win.wm_title("Daily Routine")

l1 = Label(win, text="Date", bg="#F3F4F6", fg="dark orange", font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l1.grid(row=0, column=0, sticky=N+S+E+W)

l2 = Label(win, text="Earnings", bg="#F3F4F6", fg="dark orange", font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l2.grid(row=0, column=2, sticky=N+S+E+W)

l3 = Label(win, text="Exercise", bg="#F3F4F6", fg="dark orange", font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l3.grid(row=1, column=0, sticky=N+S+E+W)

l4 = Label(win, text="Study", bg="#F3F4F6", fg="dark orange", font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l4.grid(row=1, column=2, sticky=N+S+E+W)

l5 = Label(win, text="Diet", bg="#F3F4F6", fg="dark orange", font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l5.grid(row=2, column=0, sticky=N+S+E+W)

l6 = Label(win, text="Expenses", bg="#F3F4F6", fg="dark orange", font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l6.grid(row=2, column=2, sticky=N+S+E+W)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

earning_text = StringVar()
e2 = Entry(win, textvariable=earning_text)
e2.grid(row=0, column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=1, column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1, column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2, column=1)

expense_text = StringVar()
e6 = Entry(win, textvariable=expense_text)
e6.grid(row=2, column=3)

listbox = Listbox(win, height=10, width=40)
listbox.grid(row=3, column=0, rowspan=10, columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=9, sticky=N+S)

listbox.bind('<<ListboxSelect>>', selected)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

b1 = Button(win, text='ADD', width=12, pady=5, command=add_cmd, bg="white", fg="blue", font="Lato 12", borderwidth=2, relief="groove")
b1.grid(row=3, column=3)

b2 = Button(win, text='SEARCH', width=12, pady=5, command=search_cmd, bg="white", fg="blue", font="Lato 12", borderwidth=2, relief="groove")
b2.grid(row=4, column=3)

b3 = Button(win, text='DELETE', width=12, pady=5, command=delete_cmd, bg="white", fg="blue", font="Lato 12", borderwidth=2, relief="groove")
b3.grid(row=5, column=3)

b4 = Button(win, text='VIEW', width=12, pady=5, command=view_cmd, bg="white", fg="blue", font="Lato 12", borderwidth=2, relief="groove")
b4.grid(row=6, column=3)

b5 = Button(win, text='CLOSE', width=12, pady=5, command=win.destroy, bg="white", fg="blue", font="Lato 12", borderwidth=2, relief="groove")
b5.grid(row=7, column=3)

win.mainloop()