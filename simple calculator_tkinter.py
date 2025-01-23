import pandas as pd
import numpy as np
import math
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Advance calculator")
root.configure(bg="grey")
#root.geometry(3000*3000)
def entry():
    global e,p
    e=Text(root,width=21,bg="green",fg="yellow",font=("Arial",14),height=2)
    e.grid(row=0,column=3,columnspan=4)
    p=Text(root,width=21,bg="green",fg="yellow",font=("Arial",14),height=2) 
    p.grid(row=2,column=3,columnspan=4)

entry()

def length():
    top=Toplevel()
    
    return 

def area():
    return 

def Time():
    return

def Temp():
    return 

def constant_variables():
    return 

def speed():
    return 


def myclick(num):
    current=e.get('1.0', 'end-1c')
    e.delete(1.0,"end")
    e.insert(1.0,str(current)+str(num))
def clear():
    e.delete(1.0,"end")
    p.delete(1.0,"end")

def delt():
     current = e.get('1.0', 'end-1c')
     e.delete(1.0, "end")
     e.insert(1.0, current[:-1]) 
     p.delete(1.0,"end")
def operation(strin):
    global first_num,f_num,sign,operate
    first_num=e.get('1.0', 'end-1c')
    operate=strin
    f_num=(first_num)
    dic= {"ADD":"+","SUB":"-","MULTIPLY":"*","DIVIDE":"/","SIN":"sin","COS":"cos","TAN":"tan","COSEC":"cosec","SEC":"sec","COT":"cot","SQRT":"sqrt","SQR":"sqr","LOG":"log","LN":"ln",
           "ARCTAN":"TAN^-1","ARCSIN":"SIN^-1","ARCCOS":"COS^-1","LOG":"log","LN":"ln","INV":"^-1"
           ,"POWER":"^","EXP":"e^","FAC":"!","PERCENTAGE":"%","nCr":"C","nPr":"P" ,"SINH":"sinh","COSH":"cosh","TANH":"tanh","ARCSINH":"SINH^-1","ARCCOSH":"COSH^-1","ARCTANH":"TANH^-1"}
    sign = dic[strin]
    myclick(sign)
    
def log_with_base(base,value):
     return np.log(value) / np.log(base)
def degrees():
    global angle
    angle="DEGREE"
    return angle
    #messagebox.showinfo("Note","Degree is selected")
def radians():
    global angle
    angle="RADIAN"
    return angle
    #messagebox.showinfo("Note","Radians is selected")
    
def turn_on():
    e.config(state=NORMAL)
    p.config(state=NORMAL)
    clear()

def turn_off():
    e.config(state=DISABLED)
    p.config(state=DISABLED)
pi=np.pi
def destroy1():
    global button_Close
    buttons=[button_arcsin, button_arccos, button_arctan,button_hypsin,button_hypcos,button_hyptan,button_invhypsin,button_invhypcos,button_invhyptan,button_back,button_Close,button_rad,
    button_length,button_Speed,button_area,button_Time,button_Temp,button_constant]
    for button in buttons:
        button.destroy()
    destroy_button()

def hide_button():
    buttons =[button_arcsin, button_arccos, button_arctan,button_hypsin,button_hypcos,button_hyptan,button_invhypsin,button_invhypcos,button_invhyptan,button_back,button_Close]
    for button in buttons:
        button.destroy()
    
def openinv():
    #op1=Toplevel()
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
    button_back=Button(root,text="back",command=hide_button,padx=7.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_Close=Button(root,text="Close",command=destroy1,padx=10,pady=12.5,fg="orange",bg="black",borderwidth=6)

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
def open():
    #top=Toplevel()
    global button_sin,button_cos,button_tan,button_sqrt,button_sqr,button_X,button_log,button_inv,button_ln,button_invf,button_exp,button_factorial,button_close
    global button_rad,button_degree,button_length,button_Speed,button_area,button_Time,button_Temp,button_constant
    button_sin=Button(root,text="Sin",command=lambda:operation("SIN"),padx=14,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_cos=Button(root,text="Cos",command=lambda:operation("COS"),padx=13,pady=12.5,fg="orange",bg="black",borderwidth=6) 
    button_tan=Button(root,text="Tan",command=lambda:operation("TAN"),padx=13,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_sqrt=Button(root,text="sqrt",command=lambda:operation("SQRT"),padx=12.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_sqr=Button(root,text="sqr",command=lambda:operation("SQR"),padx=13.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_X=Button(root,text="^",command=lambda:operation("POWER"),padx=19.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_log=Button(root,text="log",command=lambda:operation("LOG"),padx=13.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_ln=Button(root,text="ln",command=lambda:operation("LN"),padx=19,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_inv=Button(root,text="inv",command=lambda:operation("INV"),padx=15,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_invf=Button(root,text="invf",command=openinv,padx=12,pady=12,fg="orange",bg="black",borderwidth=6)
    button_exp=Button(root,text="e^",command=lambda:operation("EXP"),padx=16,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_factorial=Button(root,text="x!",command=lambda:operation("FAC"),padx=20,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_close=Button(root,text="close",command=destroy_button,padx=10,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_rad=Button(root,text="Rad",command=radians,padx=13,pady=12.5,fg="orange",bg="black",borderwidth=6)
    button_degree=Button(root,text="Deg",command=degrees,padx=11.5,pady=12.5,fg="orange",bg="black",borderwidth=6)

    button_length=Button(root,text="Length",command=length,padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
    button_Speed=Button(root,text="0",command=speed,padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
    button_Time=Button(root,text="0",command=Time,padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
    button_Temp=Button(root,text="0",command=Temp,padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
    button_constant=Button(root,text="0",command=constant_variables,padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
    button_area=Button(root,text="0",command=area,padx=20,pady=12.5,fg="white",bg="black",borderwidth=6)
    
    button_length.grid(row=0,column=0)
    button_Speed.grid(row=0,column=1)
    button_Time.grid(row=0,column=2)
    button_Temp.grid(row=1,column=0)
    button_constant.grid(row=2,column=0)
    button_area.grid(row=3,column=0)
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
    button_rad,button_degree,button_length,button_length,button_Speed,button_area,button_Time,button_Temp,button_constant]
    for button in buttons:
        button.destroy()
    
def equal():
    try:
         global p,s,operate
         second_num=e.get('1.0', 'end-1c')
         global s_num
         s_num=(second_num.replace(sign,""))
         s=(s_num.replace(first_num,""))

         expression= e.get('1.0', 'end-1c')
         result=eval(expression)
         p.insert(1.0,result)
    except:
         second_num=e.get('1.0', 'end-1c')
         s_num=(second_num.replace(sign,""))
         s=(s_num.replace(first_num,""))
         if operate=="PERCENTAGE":
            p.insert(1.0,float(f_num)/100)
         if operate=="SIN":
            angle="DEGREE"
            if angle=="DEGREE":
                k=math.sin(math.radians(float(s)))
                p.insert(1.0,k)
            elif angle=="RADIAN":
                  k=math.sin((float(s)))
                  p.insert(1.0,k)
         if operate=="COS":
            angle="DEGREE"
            if angle=="DEGREE":
               k=math.cos(math.radians(float(s)))
               p.insert(1.0,k)
            elif angle=="RADIAN":
               k=math.cos((float(s)))
               p.insert(1.0,k)
         if operate == "TAN":
            angle="DEGREE"
            if angle=="DEGREE":
               k=math.tan(math.radians(float(s)))
               p.insert(1.0,k)
            elif angle=="RADIAN":
                 k=math.tan((float(s)))
                 p.insert(1.0,k)
         if operate=="ARCTAN":
            k=np.arcsin(float(s))
            p.insert(1.0,k)
         if operate=="ARCCOS":
            k=np.arccos(float(s))
            p.insert(1.0,k)
         if operate=="ARCSIN":
            k=np.arcsin(float(s))
            p.insert(1.0,k)
         if operate=="SQRT":
            p.insert(1.0,np.sqrt(float(s)))
         if operate=="SQR":
            p.insert(1.0,np.square(float(s)))
         if operate=="LOG":
            p.insert(1.0,np.log10(float(s)))
         if operate=="LN":
            p.insert(1.0,np.log(float(s)))
         if operate=="INV":
            num=float(f_num)**-1
            p.insert(1.0,num)
         if operate=="POWER":
            p.insert(1.0,pow(int(f_num),int(s)))
         if operate=="FAC":
            p.insert(1.0,math.factorial(int(f_num)))
         if operate=="EXP":
            p.insert(1.0,np.exp(float(f_num)))
         if operate=="SINH":
            p.insert(1.0,np.sinh(float(s)))
         if operate=="COSH":
            p.insert(1.0,np.cosh(float(s)))
         if operate=="TANH":
            p.insert(1.0,np.tanh(float(s)))
         if operate=="ARCSINH":
            p.insert(1.0,np.arcsinh(float(s)))
         if operate=="ARCCOSH":
            p.insert(1.0,np.arccosh(float(s)))
         if operate=="ARCTANH":
            p.insert(1.0,np.arctanh(float(s)))

    
    

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
button_more=Button(root,text="More",command=open,padx=8.5,pady=12.5,fg="orange",bg="black",borderwidth=6)
button_equal=Button(root,text="=",command=equal,padx=17,pady=12.5,fg="white",bg="orange",borderwidth=6)
button=Button(root,text=".",command=lambda:myclick("."),padx=22,pady=12.5,fg="white",bg="black",borderwidth=6)
button_del=Button(root,text="DEL",command=delt,padx=12.5,pady=12.5,fg="orange",bg="black",borderwidth=6)

button_PERCENT=Button(root,text="%",command=lambda:operation("PERCENTAGE"),padx=18,pady=12.5,fg="orange",bg="black",borderwidth=6)
#buttom_instruction=Button(root,text="instructions",command=popup,padx=20,pady=12.5,fg="Red",bg="black",borderwidth=6)

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
button_PERCENT.grid(row=3,column=5)
button_more.grid(row=7,column=3)
button_equal.grid(row=7,column=6)
root.mainloop()
