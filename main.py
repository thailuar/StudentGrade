from tkinter import *
from tkinter import ttk

c0 = '#050e22'
c1 = '#8386bc'

window = Tk()
window.title('Student Grade')
window.geometry('300x400')
window.resizable(False, False)
window.configure(bg=c0)


#Header
header_title = Label(window, text="Student Grade", width=23, height=1, padx=0, relief="flat", anchor="center",
                     font='Ivy 16 bold', bg=c0, fg=c1)
header_title.place(x=0, y=20)
hd_line = Label(window, text="", width=300, relief="flat", anchor="nw", font='Arial 1', bg=c1, fg=c1)
hd_line.place(x=0, y=60)

#entry
e_name = Label(window, text='Name: ', font='Arial 14', bg=c0, fg=c1)
e_name.place(x=10, y=80)
name_e = Entry(window, width=10, font='Ivy 10 bold', justify='center', bg=c1, fg=c0, relief='solid')
name_e.place(x=200, y=85)
e_class = Label(window, text='Class: ', font='Arial 14', bg=c0, fg=c1)
e_class.place(x=10, y=110)
class_e = Entry(window, width=10, font='Ivy 10 bold', justify='center', bg=c1, fg=c0, relief='solid')
class_e.place(x=200, y=115)
e_1 = Label(window, text='First test: ', font='Arial 14', bg=c0, fg=c1)
e_1.place(x=10, y=140)
first_e = Entry(window, width=3, font='Ivy 10 bold', justify='center', bg=c1, fg=c0, relief='solid')
first_e.place(x=200, y=145)
e_2 = Label(window, text='Second test: ', font='Arial 14', bg=c0, fg=c1)
e_2.place(x=10, y=170)
second_e = Entry(window, width=3, font='Ivy 10 bold', justify='center', bg=c1, fg=c0, relief='solid')
second_e.place(x=200, y=175)
e_3 = Label(window, text='Third test: ', font='Arial 14', bg=c0, fg=c1)
e_3.place(x=10, y=200)
third_e = Entry(window, width=3, font='Ivy 10 bold', justify='center', bg=c1, fg=c0, relief='solid')
third_e.place(x=200, y=205)
e_4 = Label(window, text='Forth test: ', font='Arial 14', bg=c0, fg=c1)
e_4.place(x=10, y=230)
forth_e = Entry(window, width=3, font='Ivy 10 bold', justify='center', bg=c1, fg=c0, relief='solid')
forth_e.place(x=200, y=235)
e_final = Label(window, text='Total: ', font='Arial 13', bg=c0, fg=c1)
e_final.place(x=50, y=270)
total_e = Label(window, width=4, font='Ivy 10 bold', justify='center', relief='solid', bg=c1, fg=c0)
total_e.place(x=195, y=270)
e_situation = Label(window, text='', font='Arial 14', bg=c0, fg=c1)
e_situation.place(x=50, y=350)

#button
button_e = Button(window, text="OK", width=10, height=1, overrelief='solid', bg=c1, fg=c0,
                  font='Ivy 10 bold', anchor="center", relief='raised')
button_e.place(x=100, y=310)


#functions
def grade():
    first = float(first_e.get())
    second = float(second_e.get())
    third = float(third_e.get())
    forth = float(forth_e.get())
    total = (first + second + third + forth) / 4
    name = str(name_e.get())

    if total < 7:
        e_situation['text'] = (name + ' is reproved')
    else:
        e_situation['text'] = (name, ' is approved')

    total_e['text'] = "{:.{}f}".format(total, 2)


button_ee = Button(window, command=grade, text="OK", width=10, height=1, overrelief='solid', bg=c1, fg=c0,
                  font='Ivy 10 bold', anchor="center", relief='raised')
button_ee.place(x=100, y=310)


window.mainloop()
