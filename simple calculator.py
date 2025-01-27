import numpy as np
import math
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Advance calculator")
root.configure(bg="grey")
global e,p
e=Text(root,width=23,bg="green",fg="yellow",font=("Arial",14),height=3)
e.grid(row=0,column=3,columnspan=4)
p=Text(root,width=23,bg="green",fg="yellow",font=("Arial",14),height=3) 
p.grid(row=2,column=3,columnspan=4)
num1=" "
p.insert(1.0,num1)
def popup():
    messagebox.showinfo("Instructions","Calculator Instructions\n Advanced Functions\nClick More to access advanced mathematical functions \n\n Available functions include:\n Trigonometric: Sin, Cos, Tan\n Inverse trigonometric: sin^-1, cos^-1, tan^-1\n Hyperbolic: sinh, cosh, tanh\n Inverse hyperbolic: sinh^-1, cosh^-1, tanh^-1\n Logarithmic: log (base 10), ln (natural log)\n Exponential: e^x, x^y (power)\n Other: sqrt (square root), sqr (square), inv (inverse), x! (factorial)\n\n Angle Mode\n Use ""Rad"" for calculations in radians\n Use ""Deg"" for calculations in degrees\n \nParentheses\n Use ""("" and "")"" for grouping expressions\n\n Error Handling\n If you see an error message, press ""clear"" and re-enter your calculation\n\n Additional Controls\n ""clear"": Erases all input and results\n ""DEL"": Deletes the last entered character\n\n ""exit"": Closes the calculator application\n\n Tips\n For complex calculations, consider breaking them down into smaller steps\n Always check your input before pressing ""="" to avoid errors\n If you are unsure about a function,try a simple test calculation first")
def myclick(num):
    current=e.get('1.0', 'end-1c')
    e.delete(1.0,"end")
    e.insert(1.0,str(current)+str(num))
def clear():
    e.delete(1.0,"end")
    p.delete(1.0,"end")
    num1=" "
    p.insert(1.0,num1)
def delt():
     current = e.get('1.0', 'end-1c')
     e.delete(1.0, "end")
     e.insert(1.0, current[:-1]) 
     p.delete(1.0,"end")
def operation(strin):
    global sign,operate
    operate=strin
    dic= {"ADD":"+","SUB":"-","MULTIPLY":"*","DIVIDE":"/","SIN":"sin(","COS":"cos(","TAN":"tan(","SQRT":"sqrt(","SQR":"sqr(",",":",",
           "ARCTAN":"TAN^-1(","ARCSIN":"SIN^-1(","ARCCOS":"COS^-1(","LOG":"log(","LN":"ln(","INV":"inv(","(":"(",")":")"
           ,"POWER":"pow(","EXP":"e^(","FAC":"fac(" ,"SINH":"sinh(","COSH":"cosh(","TANH":"tanh(","ARCSINH":"SINH^-1(","ARCCOSH":"COSH^-1(","ARCTANH":"TANH^-1("}
    sign = dic[strin]
    myclick(sign)
 
def degrees():
    global angle
    angle="DEGREE"
    return angle

def radians():
    global angle
    angle="RADIAN"
    return angle
    
pi=np.pi
def destroy_all_buttons():
    global button_Close
    buttons=[button_arcsin, button_arccos, button_arctan,button_hypsin,button_hypcos,button_hyptan,button_invhypsin,button_invhypcos,button_invhyptan,button_back,button_Close,button_rad,button_openparenthesis,button_closeparenthesis,button_instruction
    ]
    for button in buttons:
        button.destroy()
    destroy_button()

def destroy_inverse_buttons():
    buttons =[button_arcsin, button_arccos, button_arctan,button_hypsin,button_hypcos,button_hyptan,button_invhypsin,button_invhypcos,button_invhyptan,button_back,button_Close]
    for button in buttons:
        button.destroy()
    
def open_inverse_buttons():
    global button_arcsin, button_arccos, button_arctan,button_hypsin,button_hypcos,button_hyptan,button_invhypsin,button_invhypcos,button_invhyptan,button_back,button_Close,button_rad
    button_arcsin=Button(root,text="sin^-1",command=lambda:operation("ARCSIN"),padx=1.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_arccos=Button(root,text="cos^-1",command=lambda:operation("ARCCOS"),padx=2.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_arctan=Button(root,text="tan^-1",command=lambda:operation("ARCTAN"),padx=2.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_hypsin=Button(root,text="sinh",command=lambda:operation("SINH"),padx=10,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_hypcos=Button(root,text="cosh",command=lambda:operation("COSH"),padx=10.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_hyptan=Button(root,text="tanh",command=lambda:operation("TANH"),padx=10.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_invhypsin=Button(root,text="sinh^-1",command=lambda:operation("ARCSINH"),padx=0.1,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_invhypcos=Button(root,text="cosh^-1",command=lambda:operation("ARCCOSH"),padx=0.1,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_invhyptan=Button(root,text="tanh^-1",command=lambda:operation("ARCTANH"),padx=0.1,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_back=Button(root,text="back",command=destroy_inverse_buttons,padx=7.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_Close=Button(root,text="Close",command=destroy_all_buttons,padx=10,pady=12.5,fg="orange",bg="black",borderwidth=6)

    button_arcsin.grid(row=5,column=0)
    button_arccos.grid(row=5,column=1)
    button_arctan.grid(row=5,column=2)
    button_hypsin.grid(row=6,column=0)
    button_hypcos.grid(row=6,column=1)
    button_hyptan.grid(row=6,column=2)
    button_invhypsin.grid(row=7,column=0)
    button_invhypcos.grid(row=7,column=1)
    button_invhyptan.grid(row=7,column=2)
    button_back.grid(row=4,column=0)
    button_Close.grid(row=3,column=0)

def open_extra_buttons():
    global button_sin,button_cos,button_tan,button_sqrt,button_sqr,button_X,button_log,button_inv,button_ln,button_invf,button_exp,button_factorial,button_close,button_openparenthesis,button_closeparenthesis,button_quit,button_instruction
    global button_rad,button_degree,button_length,button_Speed,button_area,button_Time,button_Temp,button_constant
    button_sin=Button(root,text="Sin",command=lambda:operation("SIN"),padx=14,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_cos=Button(root,text="Cos",command=lambda:operation("COS"),padx=13,pady=12.5,fg="orange",bg="black",borderwidth=6) 
    button_tan=Button(root,text="Tan",command=lambda:operation("TAN"),padx=14,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_sqrt=Button(root,text="sqrt",command=lambda:operation("SQRT"),padx=12.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_sqr=Button(root,text="sqr",command=lambda:operation("SQR"),padx=13.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_X=Button(root,text="pow",command=lambda:operation("POWER"),padx=12.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_log=Button(root,text="log",command=lambda:operation("LOG"),padx=13.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_ln=Button(root,text="ln",command=lambda:operation("LN"),padx=19,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_inv=Button(root,text="inv",command=lambda:operation("INV"),padx=17,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_invf=Button(root,text="invf",command=open_inverse_buttons,padx=12,pady=12,fg="orange",bg="black",borderwidth=6)
    button_exp=Button(root,text="e^",command=lambda:operation("EXP"),padx=16,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_factorial=Button(root,text="x!",command=lambda:operation("FAC"),padx=20,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_close=Button(root,text="close",command=destroy_button,padx=10,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_rad=Button(root,text="Rad",command=radians,padx=13,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_degree=Button(root,text="Deg",command=degrees,padx=11.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_openparenthesis=Button(root,text="(",command =lambda:operation("("),padx=21,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_closeparenthesis=Button(root,text=")",command =lambda:operation(")"),padx=21,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_openparenthesis.grid(row=2,column=1)
    button_closeparenthesis.grid(row=2,column=2)
    button_instruction=Button(root,text="Guide",command=popup,padx=5,pady=12.5,fg="Yellow",bg="black",borderwidth=6)
    button_instruction.grid(row=2,column=0)
    button_degree.grid(row=3,column=2)
    
    button_sin.grid(row=5,column=0)
    button_cos.grid(row=5,column=1)
    button_tan.grid(row=5,column=2)

    button_sqrt.grid(row=4,column=2)
    button_invf.grid(row=4,column=0)
    button_factorial.grid(row=4,column=1)
    button_ln.grid(row=6,column=0)
    button_log.grid(row=6,column=1)
    button_inv.grid(row=6,column=2)
    
    button_exp.grid(row=7,column=0)
    button_sqr.grid(row=7,column=1)
    button_X.grid(row=7,column=2)
    button_close.grid(row=3,column=0)
    button_rad.grid(row=3,column=1)

def destroy_button():
    buttons=[ button_sin,button_cos,button_tan,button_sqrt,button_sqr,button_X,button_log,button_inv,button_ln,button_invf,button_exp,button_factorial,button_close,
    button_rad,button_degree,button_openparenthesis,button_instruction,button_closeparenthesis]
    for button in buttons:
        button.destroy()

def inv(num1):
    num=(num1)**-1
    return num   
def equal():
    global e,p
    p.delete(1.0,END)
    global angle
    try:
         expression= e.get('1.0', 'end-1c')
         result=eval(expression)
         p.insert(1.0,result)
    except ValueError as e:
        e.delete(0, END)
        p.insert(0, f"Error: {str(e)}")
    except ZeroDivisionError:
        e.delete(0, END)
        p.insert(0, "Error: Division by zero")
    except:
         expression = expression.replace('sin(', 'math.sin(')
         expression = expression.replace('cos(', 'math.cos(')
         expression = expression.replace('tan(', 'math.tan(')
         expression = expression.replace('sinh(', 'np.sinh(')
         expression = expression.replace('cosh(', 'np.cosh(')
         expression = expression.replace('tanh(', 'np.tanh(')
         expression = expression.replace('SIN^-1(', 'np.arcsin(')
         expression = expression.replace('COS^-1(', 'np.arccos(')
         expression = expression.replace('TAN^-1(', 'np.arctan(')
         expression = expression.replace('SINH^-1(', 'np.arcsinh(')
         expression = expression.replace('COSH^-1(', 'np.arcsinh(')
         expression = expression.replace('TANH^-1(', 'np.arcsinh(')
         expression = expression.replace('log(', 'np.log10(')
         expression = expression.replace('ln(', 'np.log(')
         expression = expression.replace('e^(', 'np.exp(')
         expression = expression.replace('fac(', 'math.factorial(')
         expression = expression.replace('sqr(', 'np.square(')
         expression = expression.replace('sqrt(', 'np.sqrt(')
         
         angle="RADIAN"
         if angle == "DEGREE":
            expression = expression.replace('math.sin(', 'math.sin(math.radians(')
            expression = expression.replace('math.cos(', 'math.cos(math.radians(')
            expression = expression.replace('math.tan(', 'math.tan(math.radians(')
         result = eval(expression)
         p.delete(1.0, "end")
         p.insert(1.0, result)


         
button_1=Button(root,text="1",command=lambda: myclick(1),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_2=Button(root,text="2",command=lambda: myclick(2),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_3=Button(root,text="3",command=lambda: myclick(3),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)

button_4=Button(root,text="4",command=lambda: myclick(4),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_5=Button(root,text="5",command=lambda: myclick(5),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_6=Button(root,text="6",command=lambda: myclick(6),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)

button_7=Button(root,text="7",command=lambda: myclick(7),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_8=Button(root,text="8",command=lambda: myclick(8),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_9=Button(root,text="9",command=lambda: myclick(9),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)

button_0=Button(root,text="0",command=lambda: myclick(0),padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
button_clear=Button(root,text="clear",command= clear,padx=10,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_x=Button(root,text="x",command=lambda:  operation("MULTIPLY"),padx=19,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_div=Button(root,text="/",command=lambda: operation("DIVIDE"),padx=20,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_add=Button(root,text="+",command=lambda:operation("ADD"),padx=18,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_sub=Button(root,text="-",command=lambda:operation("SUB"),padx=20,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_more=Button(root,text="More",command=open_extra_buttons,padx=8.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_equal=Button(root,text="=",command=equal,padx=17,pady=12.5,fg="white",bg="orange",borderwidth=6)
button=Button(root,text=".",command=lambda:myclick("."),padx=22,pady=12.5,fg="white",bg="black",borderwidth=6)
button_del=Button(root,text="DEL",command=delt,padx=12.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_quit=Button(root,text="exit",command=root.quit,padx=13,pady=12,fg="orange",bg="black",borderwidth=6)
button_quit.grid(row=3,column=5)


button_1.grid(row=6,column=3)
button_2.grid(row=6,column=4)
button_3.grid(row=6,column=5)

button_4.grid(row=5,column=3)
button_5.grid(row=5,column=4)
button_6.grid(row=5,column=5)

button_7.grid(row=4,column=3)
button_8.grid(row=4,column=4)
button_9.grid(row=4,column=5)

button_0.grid(row=7,column=4)
button_clear.grid(row=3,column=4)
button_del.grid(row=3,column=3)
button.grid(row=7,column=5)

button_x.grid(row=6,column=6)
button_div.grid(row=3,column=6)
button_add.grid(row=5,column=6)
button_sub.grid(row=4,column=6)

button_more.grid(row=7,column=3)
button_equal.grid(row=7,column=6)
root.mainloop()
