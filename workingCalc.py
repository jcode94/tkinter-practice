from tkinter import *
from math import sqrt

f_num = 0
expression = [0]
old_op = []
eq_flag = False

root = Tk()
root.title('Calculator')

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    e.insert(END, number)


def button_equal():
    global expression
    global eq_flag
    expression = [str(x) for x in expression]
    print(f'I am expression just after equal was called: {expression}')

    if not eq_flag:
        expression.append(e.get())
        eq_flag = True
        e.delete(0, END)
        e.insert(0, eval(''.join(expression)))
        print(f'Not eq_flag expression state: {expression}')
        old_op.append(expression[-2])
        old_op.append(int(expression[-1]))
        expression = [e.get()]
    else:
        print(f'right before old_op assignment: {expression}')
        expression.append(str(old_op[0]))
        expression.append(str(old_op[1]))
        e.delete(0, END)
        e.insert(0, eval(''.join(expression)))
        print(f'is eq_flag expression state: {expression}')
        expression = [e.get()]


def hold_operator(operator):
    global eq_flag
    global expression
    eq_flag = 0
    if len(expression) == 1:
        expression[0] = e.get()
        expression.append(operator)
    else:
        expression.append(e.get())
        expression.append(operator)
    e.delete(0, END)


def button_sqrt():
    global f_num
    f_num = e.get()
    e.delete(0, END)
    e.insert(0, sqrt(float(f_num)))


def button_square():
    global f_num
    f_num = e.get()
    e.delete(0, END)
    e.insert(0, (float(f_num) ** 2))


def button_reciprocal():
    global f_num
    f_num = e.get()
    e.delete(0, END)
    e.insert(0, (1 / float(f_num)))


def button_bksp():
    cur = list(e.get())
    if len(cur) <= 1:
        cur = 0
    else:
        cur = cur[:-1]
    e.delete(0, END)
    e.insert(0, ''.join(cur))


def button_clearHistory():
    global f_num
    global expression
    e.delete(0, END)
    f_num = 0
    expression = [0]


def button_clearEntry():
    e.delete(0, END)


def button_percent():
    global f_num
    f_num = e.get()
    e.delete(0, END)
    e.insert(0, (float(f_num)/100))


def button_sign():
    global f_num
    f_num = e.get()
    e.delete(0, END)
    e.insert(0, (float(f_num) * -1))


def button_decimal():
    if '.' not in e.get():
        button_click('.')
    else:
        pass


# Button layout and cmd
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))

# Operations
button_sign = Button(root, text='+/-', padx=34, pady=20, command=button_sign)
button_decimal = Button(root, text='.', padx=42, pady=20, command=button_decimal)
button_equal = Button(root, text='=', padx=30, pady=20, command=button_equal)
button_add = Button(root, text='+', padx=30, pady=20, command=lambda: hold_operator('+'))
button_subtract = Button(root, text='-', padx=30, pady=20, command=lambda: hold_operator('-'))
button_multiply = Button(root, text='*', padx=30, pady=20, command=lambda: hold_operator('*'))
button_divide = Button(root, text='/', padx=30, pady=20, command=lambda: hold_operator('/'))
button_square = Button(root, text='sq', padx=35, pady=20, command=button_square)
button_reciprocal = Button(root, text='1/x', padx=34, pady=20, command=button_reciprocal)
button_sqrt = Button(root, text='sqrt', padx=33, pady=20, command=button_sqrt)
button_bksp = Button(root, text='<-', padx=26, pady=20, command=button_bksp)
button_clearHistory = Button(root, text='C', padx=33, pady=20, command=button_clearHistory)
button_clearEntry = Button(root, text='CE', padx=34, pady=20, command=button_clearEntry)
button_percent = Button(root, text='%', padx=38, pady=20, command=button_percent)


# Placement
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_0.grid(row=6, column=1)

button_add.grid(row=5, column=3)
button_equal.grid(row=6, column=3)
button_sign.grid(row=6, column=0)
button_decimal.grid(row=6, column=2)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_square.grid(row=2, column=1)
button_reciprocal.grid(row=2, column=0)
button_sqrt.grid(row=2, column=2)
button_bksp.grid(row=1, column=3)
button_clearHistory.grid(row=1, column=2)
button_clearEntry.grid(row=1, column=1)
button_percent.grid(row=1, column=0)

root.mainloop()
