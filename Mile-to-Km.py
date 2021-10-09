from tkinter import *

def miles_to_km():
    miles=float (miles_input.get())
    km=miles*1.609
    ans_label.config(text=f"{km}")





window=Tk()
# window.minsize(width=400,height=200)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)


miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)



miles_label=Label(text="Mile",font=("Arial"))
miles_label.grid(column=2,row=0)



equal_label=Label(text="is equal to",font=("Arial"))
equal_label.grid(column=0,row=1)

ans_label=Label(text="0",font=("Arial"))
ans_label.grid(column=1,row=1)
# ans_label.config(padx=30,pady=30)

km_label=Label(text="Km",font=("Arial"))
km_label.grid(column=2,row=1)


calculate_button=Button(text="Calculate" ,command=miles_to_km)
calculate_button.grid(column=1,row=2)





window.mainloop()