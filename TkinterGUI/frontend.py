
from tkinter import *
from tkinter import messagebox
import backend

def view_command():
    booksList.delete(0,END)
    for row in backend.view():
        booksList.insert(END, row)

def search_command():
    booksList.delete(0,END)
    for row in backend.search(titleTextBlock.get(), authorTextBlock.get(), yearTextBlock.get(), isbnTextBlock.get()):
        booksList.insert(END, row)

def insert_command():
    if (titleTextBlock.get() != '') & (authorTextBlock.get() != '') & (yearTextBlock.get() != '') & (isbnTextBlock.get() != ''):
        backend.insert(titleTextBlock.get(), authorTextBlock.get(), yearTextBlock.get(), isbnTextBlock.get())
        messagebox.showinfo(title = "Added", message = "Book added succesfully!!")
    else:
        messagebox.showerror(title = "Error", message = "Not all the fields have values")

def get_selected_row(event):
    global selected_tuple
    selected_tuple = booksList.get(booksList.curselection()[0])
    titleTextBlock.delete(0,END)
    titleTextBlock.insert(END, selected_tuple[1])
    authorTextBlock.delete(0,END)
    authorTextBlock.insert(END, selected_tuple[2])
    yearTextBlock.delete(0,END)
    yearTextBlock.insert(END, selected_tuple[3])
    isbnTextBlock.delete(0,END)
    isbnTextBlock.insert(END, selected_tuple[4])

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    if (titleTextBlock.get() != '') & (authorTextBlock.get() != '') & (yearTextBlock.get() != '') & (isbnTextBlock.get() != ''):
        backend.update(selected_tuple[0], titleTextBlock.get(), authorTextBlock.get(), yearTextBlock.get(), isbnTextBlock.get())
    view_command()

mainWindow = Tk()
mainWindow.title("BookStore")

backend.create()

titleLabel = Label(mainWindow, text="Title")
titleLabel.grid(column=0, row=0)

titleTextBlock = Entry(mainWindow)
titleTextBlock.grid(column=1, row=0)

authorLabel = Label(mainWindow, text="Author")
authorLabel.grid(column=2, row=0)

authorTextBlock = Entry(mainWindow)
authorTextBlock.grid(column=3, row=0)

yearLabel = Label(mainWindow, text="Year")
yearLabel.grid(column=0, row=1)

yearTextBlock = Entry(mainWindow)
yearTextBlock.grid(column=1, row=1)

isbnLabel = Label(mainWindow, text="ISBN")
isbnLabel.grid(column=2, row=1)

isbnTextBlock = Entry(mainWindow)
isbnTextBlock.grid(column=3, row=1)

booksList = Listbox(mainWindow, height=6, width=35)
booksList.grid(column = 0, row = 2, columnspan = 2, rowspan = 6)
bookListScrollBar = Scrollbar(mainWindow)
bookListScrollBar.grid(column = 2, row = 2, rowspan = 6)
booksList.configure(yscrollcommand = bookListScrollBar.set)
bookListScrollBar.configure(command = booksList.yview)
booksList.bind('<<ListboxSelect>>', get_selected_row)


viewAllButton = Button (mainWindow, text = "View All", width = 12, command = view_command)
viewAllButton.grid(column=3, row=2)

searchAllButton = Button (mainWindow, text = "Search", width = 12, command = search_command)
searchAllButton.grid(column=3, row=3)

addAllButton = Button (mainWindow, text = "Add entry", width = 12, command = insert_command)
addAllButton.grid(column=3, row=4)

updateAllButton = Button (mainWindow, text = "update", width = 12, command = update_command)
updateAllButton.grid(column=3, row=5)

deleteAllButton = Button (mainWindow, text = "delete", width = 12, command = delete_command)
deleteAllButton.grid(column=3, row=6)

closeAllButton = Button (mainWindow, text = "close", width = 12, command = mainWindow.destroy)
closeAllButton.grid(column=3, row=7)

mainWindow.mainloop()

