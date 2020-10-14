from tkinter import *

root= Tk()
root.geometry("600x400")
root.title("Temperture convertor"
           )
labelframe_c = LabelFrame(root, text = "Celcuis to Fahrehheit" , padx=48 , pady=48)
labelframe_c.pack(fill="both")
labelframe_c .place(x = 20 , y = 10)
entry_c = Entry(labelframe_c , state = 'disable')
entry_c.pack()

labelframe_f = LabelFrame(root, text = "Fahrehheit to Celcuis " , padx=48 , pady=48)
labelframe_f.pack(fill="both")
labelframe_f .place(x = 300 , y = 10)
entry_f = Entry(labelframe_f , state = 'disable')
entry_f.pack()

def active ():
    entry_c.config(state ='normal')

button_c =Button(root, text = "Activate-Celcuis to Fahrehheit " , command= active  )
button_c .place(x = 20 , y =180 )

def active ():
    entry_f.config(state ='normal')

button_f =Button(root, text = "Activate-Fahrehheit to Celcuis" , command= active)
button_f .place(x = 300 , y =180 )



def convert():
    if entry_c:
       fahrenheit = float(entry_c.get())
       celcius = (fahrenheit-32)*5/9
       btn_result.config(text=round(celcius,2))
       btn_result.insert(0, celcius)
def convert1():
    if entry_c:
       celcius = float(entry_f.get())
       fahrenheit = (celcius*9/5)+32
       btn_result.config(text=round(fahrenheit))
       btn_result.insert(0, celcius)

btn_Caculate =Button(root, text =" convert to fahrenheit", command=convert)
btn_Caculate .pack()
btn_Caculate .place(x = 20 , y =300 )

btn_Caculate =Button(root, text ="convert to celcius", command=convert1)
btn_Caculate .pack()
btn_Caculate .place(x = 20 , y =250 )

btn_result=Entry (root, bg ="green2")
btn_result.pack()
btn_result.place(x =205 , y =290 )

def clear():
     entry_f.delete(0,END)
     entry_c.delete(0,END)
     btn_result.delete(0,END)
btn_clear =Button(root, text ="Clear" , command=clear)
btn_clear .pack()
btn_clear .place(x = 400 , y =250 )

def quit():
    root.destroy()
btn_quit =Button(root, text = "Exit Program" , command=quit)
btn_quit .pack()
btn_quit .place(x = 380 , y =290 )

root.mainloop()
