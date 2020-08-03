from tkinter import *				##import the Tkinter module
import parser						##import the parser module
import math							##import the math module
root = Tk()							##creation of a Tk root widget which is an ordinary window containing the enter GUI application.
root.title('Calculator')			##Setting the title bar of the window to Calculator.

i = 0								##creation of a variable i and setting it to Zero.

##calculation of sin function and display it.

def sin():
    whole_string = display.get()			##getting the input from the user and assign it to whole_string					
    number = (whole_string)					##storing the value in the whole_string in a variable number 
    s=math.sin(math.radians(int(number)))	##calculation of Sine of the number and storing it in a varialble "s"
    clear_all()								##clearing the display of the calculator
    display.insert(0, s)					##displaying the result on the display

##calculation of cosine functon and display it.	

def cos():
    whole_string = display.get()			##getting the input from the user and assign it to whole_string	
    number = (whole_string)					##storing the value in the whole_string in a variable number
    s=math.cos(math.radians(int(number)))	##calculation of Cosine of the number and storing it in a varialble "s"
    clear_all()								##clearing the display of the calculator
    display.insert(0, s)					##displaying the result on the display					

##calculation of tangent funtion and dispaly it.

def tan():
    whole_string = display.get()			##getting the input from the user and assign it to whole_string	
    number = (whole_string)					##storing the value in the whole_string in a variable number 
    s=math.tan(math.radians(int(number)))	##calculation of Tangent of the number and storing it in a varialble "s"
    clear_all()								##clearing the display of the calculator
    display.insert(0, s)					##displaying the result on the display					

##calculation of logarithm of a number and display it. 

def log():
    whole_string = display.get()			##getting the input from the user and assign it to whole_string	
    number = (whole_string)					##storing the value in the whole_string in a variable number
    s=math.log10(int(number))				##calculation of logarithm of the number and storing it in a varialble "s"
    clear_all()								##clearing the display of the calculator
    display.insert(0, s)					##displaying the result on the display					

##caclculation of square root of a number and display it. 

def sqrt():
    whole_string = display.get()			##getting the input from the user and assign it to whole_string	
    number = (whole_string)					##storing the value in the whole_string in a variable number
    s=math.sqrt(int(number))				##calculation of SquareRoot of the number and storing it in a varialble "s"
    clear_all()								##clearing the display of the calculator
    display.insert(0, s)					##displaying the result on the display										


##caclculation of factorial of a number and display it.

def factor():
    
    whole_string = display.get()			##getting the input from the user and assign it to whole_string
    number = (whole_string)					##storing the value in the whole_string in a variable number
     
    try:
        n=math.factorial(int(number))		##calculation of factorial of the number and storing it in a varialble "n"
        clear_all()							##clearing the display of the calculator
        display.insert(0, n)				##displaying the result on the display
    except Exception:
        clear_all()							##else clear the dispaly
        display.insert(0, "Error")			##display error on the screen



def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, END)

def get_variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    """removes the last entered operator/variable from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    """
    Evaluates the expression
    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
    """
    whole_string = display.get()							##getting the input from the user and assign it to whole_string
    try:
        formulae = parser.expr(whole_string).compile()		##Determining the syntactic structure of the user input using "parser.expr" and store it in formulae
        result = eval(formulae)								##Evaluating the expression stored in formulae and store it in result
        clear_all()											##clearing the display of the calculator
        display.insert(0, result)							##displaying the result on the dispaly
    except Exception:
        clear_all()											##else clear the display of the calculator
        display.insert(0, "Error!")							##display error on the screen
for i in range(4):
    root.columnconfigure(i,pad=3)
for j in range(3):
    root.rowconfigure(i,pad=3)


display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 6 , sticky = W+E)

##creation of button 1 and taking 1 as user input
one = Button(root, text = 1, command = lambda : get_variables(1), font=("Calibri", 12))
one.grid(row = 2, column = 0)

##creation of button 2 and taking 2 as user input
two = Button(root, text = "2", command = lambda : get_variables(2), font=("Calibri", 12))
two.grid(row = 2, column = 1)

##creation of button 3 and taking 3 as user input
three = Button(root, text = "3", command = lambda : get_variables(3), font=("Calibri", 12))
three.grid(row = 2, column = 2)

##creation of button 4 and taking 4 as user input
four = Button(root, text = "4", command = lambda : get_variables(4), font=("Calibri", 12))
four.grid(row = 3 , column = 0)

##creation of button 5 and taking 5 as user input
five = Button(root, text = "5", command = lambda : get_variables(5), font=("Calibri", 12))
five.grid(row = 3, column = 1)

##creation of button 6 and taking 6 as user input
six = Button(root, text = "6", command = lambda : get_variables(6), font=("Calibri", 12))
six.grid(row = 3, column = 2)

##creation of button 7 and taking 7 as user input
seven = Button(root, text = "7", command = lambda : get_variables(7), font=("Calibri", 12))
seven.grid(row = 4, column = 0)

##creation of button 8 and taking 8 as user input
eight = Button(root, text = "8", command = lambda : get_variables(8), font=("Calibri", 12))
eight.grid(row = 4, column = 1)

##creation of button 9 and taking 9 as user input
nine = Button(root , text = "9", command = lambda : get_variables(9), font=("Calibri", 12))
nine.grid(row = 4, column = 2)

##creation of AC button which clears the calculator screen
cls = Button(root, text = "AC", command = clear_all, font=("Calibri", 12), foreground = "red")
cls.grid(row = 5, column = 0)

##creation of button 0 and taking 0 as user input
zero = Button(root, text = "0", command = lambda : get_variables(0), font=("Calibri", 12))
zero.grid(row = 5, column = 1)

##creation of "=" button and calculate the result and show it in the display when pressed 
result = Button(root, text = "=", command = calculate, font=("Calibri", 12), foreground = "red")
result.grid(row = 5, column = 2)

##creation of "+" button and calls the operation when pressed
plus = Button(root, text = "+", command =  lambda : get_operation("+"), font=("Calibri", 12))
plus.grid(row = 2, column = 3)

##creation of "-" button and calls the operation when pressed
minus = Button(root, text = "-", command =  lambda : get_operation("-"), font=("Calibri", 12))
minus.grid(row = 3, column = 3)


##creation of "*" button and calls the opertion when pressed
multiply = Button(root,text = "*", command =  lambda : get_operation("*"), font=("Calibri", 12))
multiply.grid(row = 4, column = 3)

##creation of "/" button and calls the opertion when pressed
divide = Button(root, text = "/", command = lambda :  get_operation("/"), font=("Calibri", 12))
divide.grid(row = 5, column = 3)

##creation of "pi" button and calls the opertion when pressed
pi = Button(root, text = "pi", command = lambda: get_operation("3.14"), font =("Calibri", 12))
pi.grid(row = 2, column = 4)

##creation of "%" button and calls the opertion when pressed
modulo = Button(root, text = "%", command = lambda :  get_operation("%"), font=("Calibri", 12))
modulo.grid(row = 3, column = 4)

##creation of "(" button and calls the opertion when pressed
left_bracket = Button(root, text = "(", command = lambda: get_operation("("), font =("Calibri", 12))
left_bracket.grid(row = 4, column = 4)

##creation of "exp" button and calls the opertion when pressed
exp = Button(root, text = "exp", command = lambda: get_operation("**"), font = ("Calibri", 10))
exp.grid(row = 5, column = 4)

##creation of "<-" button and calls the opertion when pressed
undo_button = Button(root, text = "<-", command = undo, font =("Calibri", 12), foreground = "red")
undo_button.grid(row = 2, column = 5)

##creation of "x!" button and calls the opertion when pressed
fact = Button(root, text = "x!", command = factor, font=("Calibri", 12))
fact.grid(row = 3, column = 5)

##creation of ")" button and calls the opertion when pressed
right_bracket = Button(root, text = ")", command = lambda: get_operation(")"), font =("Calibri", 12))
right_bracket.grid(row = 4, column = 5)

##creation of "^2" button and calls the opertion when pressed
square = Button(root, text = "^2", command = lambda: get_operation("**2"), font = ("Calibri", 10))
square.grid(row = 5, column = 5)

##creation of "." button and calls the opertion when pressed 
dot = Button(root, text = ".", command =  lambda: get_operation("."), font=("Calibri", 12))
dot.grid(row = 6, column = 5)

##creation of "sine" button and calls the function when pressed
sine = Button(root, text = "sine", command = sin, font=("Calibri", 12))
sine.grid(row = 6, column = 4)

##creation of "cos" button and calls the function when pressed
cosine = Button(root, text = "cos", command = cos, font=("Calibri", 12))
cosine.grid(row = 6, column = 3)

##creation of "tan" button and calls the function when pressed
tan = Button(root, text = "tan", command = tan, font=("Calibri", 12))
tan.grid(row = 6, column = 2)

##creation of "log" button and calls the function when pressed
logarithm = Button(root, text = "log", command = log, font=("Calibri", 12))
logarithm.grid(row = 6, column = 1)

##creation of "sqrt" button and calls the function when pressed
sqroot= Button(root, text = "sqrt", command = sqrt, font=("Calibri", 12))
sqroot.grid(row = 6, column = 0)

root.mainloop()				##The program will stay in the event loop until we close the window.

