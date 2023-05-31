# AS91896 / AS91897


'''

Julie's Party Hire
This program will help keep track of which items are currently 
being hired with information such as the customer's full name,
receipt number, item name and quantity. The user can choose rows 
on the hire list to delete once item are returned.


'''


# Import Tkinter and Submodules
from itertools import count
from os import remove
from this import d
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from turtle import back, bgcolor
from unicodedata import name
from tkinter import messagebox


# Program settings
root = Tk()
root.title("Julie's Party Hire List") # title of our window
root.config(background="#a29597") # a29597 is a hex colour code for a light brown colour.
root.geometry("800x600") # size of our window
count = 0


# Define customized fonts
labelfont = Font(
    family="Georgia",
    size = 16,
    weight="bold")

entryfont = Font(
    family="Georgia",
    size = 12,
    weight="normal")

listfont = Font(
    family="Georgia",
    size = 13,
    weight="normal")

errorfont = Font(
    family="Georgia",
    size = 12,
    weight="bold")

headingfont = Font(
    family="Georgia",
    size = 13,
    weight="bold")

buttonfont = Font(
    family="Georgia",
    size = 13,
    weight="bold")


# Create a treeview widget
#  ↳ defining a style
style = ttk.Style()


#  ↳ selecting a theme for the treeview widget
style.theme_use("clam")
style.configure("Treeview", 
    background="gray",
    foreground="black",
    rowheight=25,
    fieldbackground="#e9e9e9",
    font=listfont
    )
style.configure("Treeview.Heading", font=headingfont)


style.map('Treeview',
    background=[('selected', '#8b7b7d')])


# Define our Treeview widget
my_tree = ttk.Treeview(root)


#  ↳ define our column
my_tree['columns'] = ("Name", "Receipt", "Item", "Quantity")


#  ↳ formatte our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=CENTER, width=150)
my_tree.column("Receipt", anchor=CENTER, width=150)
my_tree.column("Item", anchor=CENTER, width=150)
my_tree.column("Quantity", anchor=CENTER, width=150)


#  ↳ create headings
my_tree.heading("#0", text=" ", anchor=CENTER)
my_tree.heading("Name", text="Customer's full Name",anchor=CENTER)
my_tree.heading("Receipt", text="Receipt Number", anchor=CENTER)
my_tree.heading("Item", text="Item hired", anchor=CENTER) 
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)

my_tree.pack(pady=20)


# Define a frame for displaying entry boxes
add_frame = Frame(root, bg="#8b7b7d") 
add_frame.pack()


# Create labels
nl = Label(add_frame, text="Customer's full Name", font=labelfont, fg="White", bg="#8b7b7d") # nl = Name Label
nl.grid(row=0, column=0)

rl = Label(add_frame, text="Receipt Number", font=labelfont, fg="White", bg="#8b7b7d")
rl.grid(row=0, column=1)

il = Label(add_frame, text="Item hired", font=labelfont, fg="White", bg="#8b7b7d")
il.grid(row=0, column=2)

ql = Label(add_frame, text="Quantity", font=labelfont, fg="White", bg="#8b7b7d")
ql.grid(row=0, column=3)

# Create entry boxes
name_box = Entry(add_frame, font=entryfont)
name_box.grid(row=1, column=0)

receipt_box = Entry(add_frame, font=entryfont)
receipt_box.grid(row=1, column=1)

item_box = Entry(add_frame, font=entryfont)
item_box.grid(row=1, column=2)

quantity_box = Entry(add_frame, font=entryfont)
quantity_box.grid(row=1, column=3)


# Create error labels
name_box_error = Label(add_frame, font=errorfont, fg="Red")
name_box_error.grid(row = 2, column=0)

receipt_box_error = Label(add_frame, font=errorfont, fg="Red")
receipt_box_error.grid(row = 2, column=1) 

item_box_error = Label(add_frame, font=errorfont, fg="Red")
item_box_error.grid(row = 2, column=2)

quantity_box_error = Label(add_frame, font=errorfont, fg="Red")
quantity_box_error.grid(row = 2, column=3)


# Function for checking the validity of each user input
def check_add_record_validity():
    #  ↳ clearing all error labels 
    clear_all_error_labels()
    
    #  ↳ define variable to check validity of fields
    allValid = True
    
    #  ↳ check if name is empty
    if name_box.get() == '':

        # Show error label to user
        name_box_error.config(text="This field is required")

        # Set allValid to False
        allValid = False

        #  ↳ check if receipt number includes any numbers 
    elif not name_box.get().isalpha() :
         
         #show error label to user
         name_box_error.config(text="Please only use letters")

  
    # Setting a variable because we need to use it more than once. 
    receipt_box_input = receipt_box.get()

    #  ↳ check if receipt number is empty
    if receipt_box_input == '':
        
        # Show error label to user
        receipt_box_error.config(text="This field is required")

        # Set allValid to False
        allValid = False

    #  ↳ check if receipt number includes any alphabets
    elif not receipt_box_input.strip().isdigit():
        
        # Show error label to user
        receipt_box_error.config(text="Please only use numbers")

        # Set allValid to False
        allValid = False
    
    #  ↳ check if item is empty
    if item_box.get() == '':

        # Show error label to user
        item_box_error.config(text="This field is required")

        # Set allValid to False
        allValid = False

#  ↳ check if receipt number includes any numbers 
    elif not item_box.get().isalpha() :
         
         #show error label to user
         item_box_error.config(text="Please only use letters")

      
    
    # Setting a variable because we need to use it more than once. 
    quantity_box_input = quantity_box.get()

  #cannot be blank, correct data type (integer), 1-500 boundary values
    if (quantity_box.get().isdigit()):
        if 0 < int(quantity_box.get()) <= 500:
            entry_check = 0
    
        else:
                quantity_box_error.config(text="Required (Numbers 1-500)")
                quantity_box_error.config(text="Required (Numbers 1-500)")

 
    else:
                quantity_box_error.config(text="Required (Numbers 1-500)")
                quantity_box_error.config(text="Required (Numbers 1-500)")


#if all inputs are valid, append to allow for printing
    if entry_check == 0:
        add_record()

    
# Command to clear all labels before checking again. 
def clear_all_error_labels():
    name_box_error.config(text="")
    receipt_box_error.config(text="")
    item_box_error.config(text="")
    quantity_box_error.config(text="")


# Define command to add record
def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text=" ", 
        values=(name_box.get(), receipt_box.get(), item_box.get(), quantity_box.get()))
    count += 1

    #  ↳ clear boxes once data was displayed
    name_box.delete(0, END)
    receipt_box.delete(0, END)
    item_box.delete(0, END)
    quantity_box.delete(0, END)


# Define command to remove ALL records 
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


# Define command to remove ALL selected
def remove_selected():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


# Button to add records
add_record_button = Button(root, text="Add Record",
    font=buttonfont, command=check_add_record_validity) # commands to check validity when pressed
add_record_button.config(width=16)
add_record_button.pack(pady=20)


# Messagebox to pop up when the user presses "Remove ALL" button
def remove_all_confirm():
    if messagebox.askokcancel('WARNING', 'This cannot be undone. Are you sure?', icon="warning") == True:
        remove_all() # commands to remove ALL when pressed YES
    else:
        return  


# Button to remove all SELECTED.
remove_selected_button = Button(root, text="Remove all selected", font=buttonfont, command=remove_selected)
remove_selected_button.config(width=16)
remove_selected_button.pack()



# Button to remove ALL.
remove_all_button = Button(root, text="Remove all records",
    font=buttonfont, fg="Red", command=remove_all_confirm) # commands for the message box to pop up
remove_all_button.config(width=16)
remove_all_button.pack(pady=20)


# Run the program
root.mainloop()





