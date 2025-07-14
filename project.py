from tkinter import *
from tkinter import ttk,messagebox
def calculate_interest():
    try:
        principal=float(principal_var.get())
        rate=float(rate_var.get())
        time=float(time_var.get())
        simple_interest=(principal*rate*time)/100
        compound_amount=principal*(1+rate/100)**time
        compound_interest=compound_amount-principal
        si_result_var.set(f"{simple_interest:,.2f}")
        ci_result_var.set(f"{compound_interest:,.2f}")
    except ValueError:
        messagebox.showerror("invalid input.","please enter numeric values for all three fields.")
root=Tk()
root.title("interest calculator")
root.geometry("400x400")
root.resizable(False,False)
PAD=8
principal_var=StringVar()
rate_var=StringVar()
time_var=StringVar()
si_result_var=StringVar(value="—")
ci_result_var=StringVar(value="—")
style=ttk.Style(root)
style.configure("label",font=("Helvetica",11))
style.configure("entry",font=("Helvetica",11))
style.configure("button",font=("Helvetica",11,"bold"))
def add_row(parent,text,variable,row):
    ttk.Label(parent,text=text).grid(column=0,row=row,sticky="e",padx=(PAD,2),pady=PAD)
    ttk.Entry(parent,textvariable=variable,width=18).grid(column=1,row=row,sticky="w",padx=(2,PAD),pady=PAD)
add_row(root,"principal:",principal_var,0)
add_row(root,"rate:",rate_var,1)
add_row(root,"time:",time_var,2)
ttk.Button(root,text="calculate",command=calculate_interest).grid(column=0,row=3,columnspan=2,pady=(PAD,PAD*2))
ttk.Label(root,text="simple Interest:").grid(column=0,row=4,sticky="e",padx=(PAD,2),pady=PAD)
ttk.Label(root,textvariable=si_result_var).grid(column=1,row=4,sticky="w",padx=(2,PAD),pady=PAD)
ttk.Label(root,text="compound Interest:").grid(column=0,row=5,sticky="e",padx=(PAD,2),pady=PAD)
ttk.Label(root,textvariable=ci_result_var).grid(column=1,row=5,sticky="w",padx=(2,PAD),pady=PAD)
root.mainloop()