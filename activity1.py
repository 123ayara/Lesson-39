from tkinter import*
root=Tk()
root.title("Numper Pad")
root.geometry("250x300")
Frame(master=root, height=200, width=360, bg="#d0efff")
nums=[[9,8,7],[6,5,4],[3,2,1],["#", 0,"*"]]
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame=Frame(master=root,relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j)
        label=Label(master=frame, text=nums[i][j], bg="#69f38d")
        label.pack(padx=3, pady=3)
root.mainloop()