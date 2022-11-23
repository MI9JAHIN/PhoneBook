#Phone book app frame

from tkinter import *
from tkinter import ttk
from Phonebookview import *
from tkinter import messagebox


#colour
co0="#ffffff"
co1="#000000"
co2="#4456F0"
co3="#2CA461"
co4="#1666C6"
co5="#3403d8"

window = Tk()
window.title("")
window.geometry("800x500")
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)


#frames
frame_up = Frame(window, width=1000, height=50, bg=co4)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=1000, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=1000, height=500, bg=co4, relief="flat")
frame_table.grid(row=2, column=0, columnspan=2, padx=1, pady=1, sticky=NW)



#functions
def show():
    global tree

    listheader = ['Name', 'Gender', 'Telephone', 'Home']

    demo_list=view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=2, row=2, sticky='nsew')
    vsb.grid(column=3, row=2, sticky='ns')
    hsb.grid(column=2, row=3, sticky='ew')

    #tree head
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Gender', anchor=NW)
    tree.heading(2, text='Phone', anchor=NW)
    tree.heading(3, text='Home', anchor=NW)

    # tree  columns
    tree.column(0, width=200, anchor='nw')
    tree.column(1, width=175, anchor='nw')
    tree.column(2, width=200, anchor='nw')
    tree.column(3, width=200, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)
    
show()

def insert():
    Name=e_name.get()
    Gender=c_gender.get()
    Phone=e_phone.get()
    Home=e_home.get()

    data=[Name, Gender, Phone, Home]
    if Name=='' or Gender=='' or Phone=='' or Home=='':
        messagebox.showwarning('data','Somthing is missing please put all informatin')
    else:
        add(data)
        messagebox.showinfo('data','Data added successfully')

        e_name.delete(0, 'end')
        c_gender.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_home.delete(0, 'end')
        show()


def to_update():
    try:
        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']

        Name=str(tree_list[0])
        Gender=str(tree_list[1])
        Phone=str(tree_list[2])
        Home=str(tree_list[3])

        e_name.insert(0, Name)
        c_gender.insert(0, Gender)
        e_phone.insert(0, Phone)
        e_home.insert(0, Home)
        
        def confirm():
            new_name=e_name.get()
            new_gender=c_gender.get()
            new_phone=e_phone.get()
            new_home=e_home.get()

            data=[new_phone,new_name,new_gender,new_phone,new_home]
            update(data)

            messagebox.showinfo('Success','Updated Successfully')
            e_name.delete(0, 'end')
            c_gender.delete(0, 'end')
            e_phone.delete(0, 'end')
            e_home.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()
        b_confirm=Button(frame_down, text="Confirm ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'),command=confirm)
        b_confirm.place(x= 540, y=60)
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')


def to_remove():
    try:
        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']
        tree_phone=str[tree_list[2]]

        to_remove(tree_phone)

        messagebox.showinfo('Success','Delete Successfully')

        for widget in frame_table.winfo_children():
                widget.destroy()

        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')


def to_search():
    Name=e_search.get()

    data=search(Name)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('','end', values=item)

    e_search.delete(0,'end')



#frame_up widgets
app_name=Label(frame_up, text="PhoneBook", height=1, font=('Verdana 20 bold'), bg=co4, fg=co0)
app_name.place(x=5, y=5)

#frame down widgets
l_name=Label(frame_down, text="Name ", width=20 ,height=1, font=('Ivy 10 bold'), bg=co0,anchor=NW)
l_name.place(x=10, y=20)
e_name=Entry(frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

l_gender=Label(frame_down, text="Gender", width=20, height=1, font=('Ivy 10 bold'), bg=co0,anchor=NW)
l_gender.place(x=10, y=50)
c_gender=ttk.Combobox(frame_down, width=27)
c_gender['values']=['','F','M']
c_gender.place(x=80, y=50)

l_phone=Label(frame_down, text="Phone ", width=20 ,height=1, font=('Ivy 10 bold'), bg=co0,anchor=NW)
l_phone.place(x=10, y=80)
e_phone=Entry(frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
e_phone.place(x=80, y=80)

e_phone

l_home=Label(frame_down, text="Home ", width=20 ,height=1, font=('Ivy 10 bold'), bg=co0,anchor=NW)
l_home.place(x=10, y=110)
e_home=Entry(frame_down, width=30, justify='left', highlightthickness=1, relief="solid")
e_home.place(x=80, y=110)

e_search=Button(frame_down, text="Search ", height=1, bg=co0, fg=co1, font=('Ivy 10 bold'),command=to_search)
e_search.place(x=550, y=1)
e_search=Entry(frame_down, width=20, justify='left',font=('Ivy 11 bold'), highlightthickness=1, relief="solid")
e_search.place(x=620, y=3)

b_view=Button(frame_down, text="View ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'),command=show)
b_view.place(x=460, y=30)

b_Modify=Button(frame_down, text="Modify ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'),command=to_update)
b_Modify.place(x=460, y=60)

b_Settings=Button(frame_down, text="Settings ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'))
b_Settings.place(x=460, y=90)

b_add=Button(frame_down, text="ADD ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'), command=insert)
b_add.place(x=300, y=30)

b_delete=Button(frame_down, text="Delete ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'),command=to_remove)
b_delete.place(x=300, y=60)

b_ManageContacts=Button(frame_down, text="Manage Contacts ", height=1, bg=co4, fg=co0, font=('Ivy 10 bold'))
b_ManageContacts.place(x=300, y=90)



window.mainloop()