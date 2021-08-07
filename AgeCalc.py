from tkinter import *
from datetime import datetime

win_width = 400
win_height = 350

# Center the main window
App = Tk()
App.title('Age Calculator')
x = App.winfo_screenwidth()/2 - win_width/2
y = App.winfo_screenheight()/2 - win_height/2
App.geometry("+%d+%d" % (x, y))

# Make the window's size static
App.minsize(win_width, win_height)
App.maxsize(win_width, win_height)

App['background'] = '#D2D4D5'

lable4 = Label(App, bg='#D2D4D5')         # Part4: Output - A 4x2 table
lable4.grid(row=4, column=0, columnspan=6)

# Part1: Title
msg = Label(App, text="Enter your date of birth", font=('Times', 20, 'bold'), bg='#D2D4D5')
msg.grid(row=0, column=0, columnspan=6, padx=60, pady=10)

# Part2: User input
dayL = Label(App, text='Day:', font=('Courier', 13, 'bold'), bg='#D2D4D5')      # bg='#D2D4D5'
dayE = Entry(App, width=2)
dayL.grid(row=1, column=0, padx=(25, 0))
dayE.grid(row=1, column=1, pady=10, padx=(0, 35))

monL = Label(App, text='Month:', font=('Courier', 13, 'bold'), bg='#D2D4D5')
monE = Entry(App, width=2)
monL.grid(row=1, column=2)
monE.grid(row=1, column=3, padx=(0, 35))

yearL = Label(App, text='Year:', font=('Courier', 13, 'bold'), bg='#D2D4D5')
yearE = Entry(App, width=4)
yearL.grid(row=1, column=4)
yearE.grid(row=1, column=5, padx=(0, 35))


# Calculate year, month, day, and seconds
def calculate():

    global year_now, year_birth, month_now, month_birth, day_now, day_birth, error_flag

    year_now = datetime.today().year
    year_birth = int(yearE.get())

    month_now = datetime.today().month
    month_birth = int(monE.get())

    day_now = datetime.today().day
    day_birth = int(dayE.get())

    dob = datetime(day=day_birth, month=month_birth, year=year_birth)
    if dob > datetime.now():
        error_flag = True
    else:
        error_flag = False

    if error_flag:
        error_box = Label(App, text='Can\'t calculate a time in future!', font=('Arial', 15, 'bold'),
                          width=30, borderwidth=2, relief='raised', bg='#C5C4C4', fg='red', pady=4)
        error_box.grid(row=5, column=0, columnspan=6, pady=10)
        error_flag = True
        raise ValueError("Can't calculate a time in future!")
    else:
        error_box = Label(App, width=55, relief='flat', bg='#D2D4D5', pady=10)
        error_box.grid(row=5, column=0, columnspan=6)

    time_dif = datetime.now() - dob

    return time_dif


# Part 4: Output table
def find_days():
    days_title = Label(lable4, text='Days', font=('Arial', 10), width=10, borderwidth=2,
                       relief='raised', pady=4, bg='#C5C4C4')
    days_title.grid(row=3, column=0)

    # The days are calculated by datetime library in calculate()
    day_dif = calculate().days
    days = Label(lable4, text=str(day_dif), font=('Arial', 10), width=10, borderwidth=2,
                 relief='raised', pady=4, bg='#CFCECE')
    days.grid(row=3, column=1)
    return day_dif


def find_months():

    months_title = Label(lable4, text='Months', font=('Arial', 10), width=10, borderwidth=2, relief='raised', pady=4,
                         bg='#C5C4C4')
    months_title.grid(row=2, column=0)

    # Check if it's been a full month
    # For example: Suppose you're born on June 2000
    # If it's September 2020 then you're 20 years old and some
    # But if it's January 2020, you're almost 20 years old(actually 19 years and some, not 20)
    if month_now == month_birth:
        if day_birth == day_now:
            month_dif = year_dif * 12
        elif day_birth < day_now:
            month_dif = year_dif*12 - day_now + day_birth
        else:
            month_dif = (year_dif*12 - 1) + (30 - day_birth + day_now)
    elif month_birth < month_now:
        month_dif = (year_dif*12) + (month_now - month_birth) - 1

    else:
        month_dif = (year_dif*12 - 1) + (12 - month_birth) + month_now

    months = Label(lable4, text=(str(month_dif) + ' + ' + str(find_days() % 30) + '/30'), font=('Arial', 10),
                   width=10, borderwidth=2, relief='raised', pady=4, bg='#CFCECE')
    months.grid(row=2, column=1)
    return month_dif


def find_years():

    global year_dif

    # Add this message above the output table
    title = Label(lable4, text='You\'ve lived for:', font=('Arial', 12, 'bold'), pady=4, bg='#D2D4D5')
    title.grid(row=0, column=0, columnspan=2)

    years_title = Label(lable4, text='Years', font=('Arial', 10), width=10, borderwidth=2, relief='raised', pady=4,
                        bg='#C5C4C4')
    years_title.grid(row=1, column=0)

    # Check if it was a full year or not!
    # We do exactly as in find_month()
    if year_now == year_birth:
        year_dif = 0
    else:
        if month_birth < month_now:
            year_dif = year_now - year_birth
        else:
            year_dif = year_now - year_birth - 1

    years = Label(lable4, text=(str(year_dif) + ' + ' + str(find_months() % 12) + '/12'), font=('Arial', 10),
                  width=10, borderwidth=2, relief='raised', pady=4, bg='#CFCECE')
    years.grid(row=1, column=1)


def find_seconds():
    seconds_title = Label(lable4, text='Seconds', font=('Arial', 10), width=10, borderwidth=2,
                          relief='raised', pady=4, bg='#C5C4C4')
    seconds_title.grid(row=4, column=0)

    # The seconds are calculated by datetime library in calculate()
    second_dif = int(calculate().total_seconds())
    seconds = Label(lable4, text=str(second_dif), font=('Arial', 10), width=10, borderwidth=2,
                    relief='raised', pady=4, bg='#CFCECE')
    seconds.grid(row=4, column=1)


# Call upon all above function when the button is pressed
def do():
    calculate()
    find_years()
    find_months()
    find_days()
    find_seconds()


calculate_b = Button(App, text='Calculate', font=('Arial', 11, 'bold'), command=do, width=15)
calculate_b.grid(row=2, column=0, columnspan=6, pady=5)

App.mainloop()
