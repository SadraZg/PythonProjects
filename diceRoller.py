# This is a simple Python GUI Project
# It rolls the dice and shows user the random output(output being a side of a dice)
from tkinter import *

welc_wind = Tk()

# Calculations to center the windows
main_width = 240
main_height = 200
screen_width = welc_wind.winfo_screenwidth()
screen_height = welc_wind.winfo_screenheight()
x = screen_width/2 - main_width/2
y = screen_height/2 - main_height/2

welc_wind.geometry("+%d+%d" % (x, y))
welc_wind.title("Roll")
welc_wind['background'] = '#D7DBDD'

# All 6 faces of a dice
dice_faces = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}


# If user chooses to roll one dice
def one_dice():
    welc_wind.destroy()
    dice_wind = Tk()
    dice_wind.title("Roll")
    # dice_wind.geometry('240x220')
    dice_wind.geometry("+%d+%d" % (x, y))
    dice_wind['background'] = '#D7DBDD'
    # dice_wind.eval('tk::PlaceWindow . center')

    dice_faces = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}

    dice = Label(dice_wind, text='☟', font=('Times', 100), background='#D7DBDD', foreground='black')
    dice.grid(row=0, column=0, padx=50, pady=5)

    def roll():
        from random import randint
        i = randint(1, 6)
        msg = Label(dice_wind, text=dice_faces[i], font=('Times', 100), background='#D7DBDD', foreground='black')
        msg.grid(row=0, column=0, padx=25, pady=5)

    roll_b = Button(dice_wind, text='Roll', command=roll, font=('Times', 13), width=15, pady=5)
    roll_b.grid(row=1, column=0, columnspan=2, pady=15)


# If user chooses to roll two dices
def two_dice():
    welc_wind.destroy()
    dice_wind = Tk()
    dice_wind.title("Roll")
    dice_wind.geometry("+%d+%d" % (screen_width/2 - 210, y))
    dice_wind['background'] = '#D7DBDD'

    dice1 = Label(dice_wind, text='⬊', font=('Times', 100), background='#D7DBDD', foreground='black')
    dice1.grid(row=0, column=0, padx=50, pady=5)
    dice2 = Label(dice_wind, text='⬋', font=('Times', 100), background='#D7DBDD', foreground='black')
    dice2.grid(row=0, column=1, padx=50, pady=5)

    def roll():
        from random import randint
        i = randint(1, 6)
        j = randint(1, 6)
        msg1 = Label(dice_wind, text=dice_faces[i], font=('Times', 100), background='#D7DBDD', foreground='black')
        msg1.grid(row=0, column=0, padx=25, pady=5)
        msg2 = Label(dice_wind, text=dice_faces[j], font=('Times', 100), background='#D7DBDD', foreground='black')
        msg2.grid(row=0, column=1, padx=25, pady=5)

    roll_b = Button(dice_wind, text='Roll', command=roll, font=('Times', 13), width=15)
    roll_b.grid(row=1, column=0, columnspan=2, pady=15)


# The function to decide which above functions should be used according to user's choice (num_dice)
def select():
    if num_dice.get() == 1:
        one_dice()
    else:
        two_dice()


welc_msg = Label(welc_wind, text="Role the dice", font=('Times', 18), background='#D7DBDD', foreground='black')
welc_msg.grid(row=0, column=0, padx=50, pady=25)

# Two radio buttons for user to determine one or two dices to use
num_dice = IntVar()
rb1 = Radiobutton(welc_wind, text='One dice', variable=num_dice, value=1, font=('Courier', 12),
                  background='#D7DBDD', foreground='black')
rb2 = Radiobutton(welc_wind, text='Two dices', variable=num_dice, value=2, font=('Courier', 12),
                  background='#D7DBDD', foreground='black')
rb1.deselect()
rb2.deselect()
rb1.grid(row=1, column=0)
rb2.grid(row=2, column=0)

# This buttons calls the select function to determine which function is going to be called according to num_dice
dice_b = Button(welc_wind, text='Let\'s roll', command=select, width=20)
dice_b.grid(row=3, column=0, pady=20)

welc_wind.mainloop()
