from tkinter import *

root= Tk()
root.geometry("600x400")
root.title("Temperture convertor"
           )
labelframe_c = LabelFrame(root, text = "Celcuis to Fahrehheit" , padx=48 , pady=48)
labelframe_c.pack(fill="both")
labelframe_c .place(x = 20 , y = 10)
entry_c = Entry(labelframe_c)
entry_c.pack()

labelframe_f = LabelFrame(root, text = "Fahrehheit to Celcuis " , padx=48 , pady=48)
labelframe_f.pack(fill="both")
labelframe_f .place(x = 300 , y = 10)
entry_f = Entry(labelframe_f)
entry_f.pack()

button_c =Button(root, text = "Activate-Celcuis to Fahrehheit" )
button_c .place(x = 20 , y =180 )

button_f =Button(root, text = "Activate-Fahrehheit to Celcuis" )
button_f .place(x = 300 , y =180 )

btn_Caculate =Button(root, text ="Calculate Conversion")
btn_Caculate .pack()
btn_Caculate .place(x = 20 , y =250 )

btn_result=Entry (root, bg ="green2" ,)
btn_result.pack()
btn_result.place(x =200 , y =250 )

root.mainloop()
