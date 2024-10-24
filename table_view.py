import tkinter as tk

class Table:

    def __init__ (self, master:tk.Tk,data,column_data):


        self.my_F = tk.Frame(master,width=290,height=300,bg="#000000")
        for i in range(len(column_data)):
            t = tk.Label(self.my_F, width=17, text=column_data[i], bg="#c0c0c0", bd=2)
            t.grid(row=0, column=i, padx=2, pady=2)
        for i in range(len(data)):
            for j in range(len(data[i])):
                t = tk.Label(self.my_F,width=17,text=data[i][j],bg= "#ffffff",bd=2)
                t.grid(row=i+1,column=j,padx=2,pady=2)

    def set_position(self,dx,dy):
        self.my_F.place(x=dx, y=dy)

    def remove_table(self):
        self.my_F.place_forget()