from tkinter import *

win_width = 350
win_height = 300

# Center the main window
App = Tk()
App.title('Length Converter')
x = App.winfo_screenwidth()/2 - win_width/2
y = App.winfo_screenheight()/2 - win_height/2
App.geometry("+%d+%d" % (x, y))
App['background'] = '#D2D4D5'

# Make the window's size static
App.minsize(win_width, win_height)
App.maxsize(win_width, win_height)

# Part1: Title
title_msg = Label(App, text="Length Converter", font=('Times', 20, 'bold'), bg='#D2D4D5')
title_msg.grid(row=0, column=0, columnspan=2, padx=70, pady=20)

scales = ['Meter', 'Inch', 'Foot']

# Part2: Options
msg1 = Label(App, text='Convert from:', font=('Arial', 12), bg='#D2D4D5')
msg1.grid(row=1, column=0, pady=10)

_from = StringVar()
from_menu = OptionMenu(App, _from, *scales)
from_menu.grid(row=1, column=1)

msg2 = Label(App, text='To:', font=('Arial', 12), bg='#D2D4D5')
msg2.grid(row=2, column=0)

to_ = StringVar()
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=2, column=1)

# Part3: User input
enterL = Label(App, text='Enter your number: ', font=('Arial', 11), bg='#D2D4D5')
enterL.grid(row=3, column=0, pady=10)
enterE = Entry(App)
enterE.grid(row=3, column=1)


def convert():
    From = _from.get()
    To = to_.get()
    num = float(enterE.get())

    if From == 'Meter' and To == 'Foot':
        conv_num = num * 3.28
    elif From == 'Meter' and To == 'Inch':
        conv_num = num * 39.37

    elif From == 'Inch' and To == 'Foot':
        conv_num = num * 12
    elif From == 'Inch' and To == 'Meter':
        conv_num = num / 39.37

    elif From == 'Foot' and To == 'Inch':
        conv_num = num / 12
    elif From == 'Foot' and To == 'Meter':
        conv_num = num / 3.28
    else:
        conv_num = num

    numL = Label(App, text='Result = ' + str(round(conv_num, 2)), font=('Arial', 13, 'bold'), bg='#D2D4D5')
    numL.grid(row=5, column=0, columnspan=2, pady=10)


act_button = Button(App, text='Convert', command=convert, font=('Arial', 12))
act_button.grid(row=4, column=0, columnspan=2, pady=10)

App.mainloop()
