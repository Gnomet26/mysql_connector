import tkinter as tk
import tkinter.messagebox
from threading import Thread
from table_view import Table
from My_Db_connector import My_Db
import time

class My_App:
    def __init__(self):

        self.is_root = True
        self.result = ""
        self.oyna = tk.Tk()
        self.oyna.geometry("720x400")
        self.oyna.resizable(False, False)

        self.col_data = ["id","ismi","Familyasi","Tel raqam"]

        #========== set item_1 =======================
        self.l_1 = tk.Label(self.oyna,text="id")
        self.l_1.place(x = 20,y = 20)

        self.entry_1 = tk.Entry(self.oyna,width=5,bd=2)
        self.entry_1.place(x = 40,y = 20)

        # ========== set item_2 =======================
        self.l_2 = tk.Label(self.oyna, text="Ismi")
        self.l_2.place(x=100, y=20)

        self.entry_2 = tk.Entry(self.oyna, width=10, bd=2)
        self.entry_2.place(x=135, y=20)

        # ========== set item_3 =======================
        self.l_3 = tk.Label(self.oyna, text="Familyasi")
        self.l_3.place(x=240, y=20)

        self.entry_3 = tk.Entry(self.oyna, width=10, bd=2)
        self.entry_3.place(x=305, y=20)

        # ========== set item_4 =======================
        self.l_4 = tk.Label(self.oyna, text="Tel raqam")
        self.l_4.place(x=410, y=20)

        self.entry_4 = tk.Entry(self.oyna, width=13, bd=2)
        self.entry_4.place(x=475, y=20)



        #========== Buttons =====================

        self.add_btn = tk.Button(self.oyna,text="Insert",command=lambda :self.insert_data_th())
        self.add_btn.place(x = 620,y = 17)

        self.select_btn = tk.Button(self.oyna, text="Select",padx=20,command=lambda :self.select_data_th())
        self.select_btn.place(x=620, y=70)

        self.select_btn = tk.Button(self.oyna, text="Update",padx=15,command=lambda :self.update_data_th())
        self.select_btn.place(x=620, y=110)

        self.select_btn = tk.Button(self.oyna, text="Delete",padx=17,command=lambda :self.delete_data_th())
        self.select_btn.place(x=620, y=150)

        # ============== set table view ================

        self.t = Table(self.oyna, [], self.col_data)
        self.t.set_position(20, 70)
        # ==============================================


        self.oyna.update()
        self.oyna.mainloop()

    def updater(self):
        print("updater runn")
        if(self.result != ""):
            self.loading.place_forget()
            self.t = Table(self.oyna, self.result, self.col_data)
            self.t.set_position(20, 70)
            self.entry_1.delete(0,'end')
            self.entry_2.delete(0, 'end')
            self.entry_3.delete(0, 'end')
            self.entry_4.delete(0, 'end')

        else:

            time.sleep(2)
            self.updater()
        pass

    def insert_data(self):

        thh = Thread(target=lambda: self.updater())
        thh.start()

        id_1 = str(self.entry_1.get())
        id_2 = str(self.entry_2.get())
        id_3 = str(self.entry_3.get())
        id_4 = str(self.entry_4.get())

        query = f"insert into talabalar (id, ismi, familyasi, tel_raqam) values ('{id_1}', '{id_2}', '{id_3}', '{id_4}')"
        My_Db(query=query)

        select_all = "select * from talabalar"
        dd = My_Db(query=select_all)
        self.result = dd.get_result()
        self.is_root = True
        pass

    def update_data(self):

        thh = Thread(target=lambda: self.updater())
        thh.start()

        id_1 = str(self.entry_1.get())
        id_2 = str(self.entry_2.get())
        id_3 = str(self.entry_3.get())
        id_4 = str(self.entry_4.get())

        query = f"UPDATE talabalar SET id={id_1},ismi='{id_2}',familyasi='{id_3}',tel_raqam='{id_4}' WHERE id={id_1}"
        My_Db(query=query)

        select_all = "select * from talabalar"
        dd = My_Db(query=select_all)
        self.result = dd.get_result()
        self.is_root = True
        pass

    def delete_data(self):
        thh = Thread(target=lambda: self.updater())
        thh.start()

        id_1 = str(self.entry_1.get())

        query = f"delete from talabalar where id={id_1}"
        My_Db(query=query)

        select_all = "select * from talabalar"
        dd = My_Db(query=select_all)
        self.result = dd.get_result()
        self.is_root = True
        pass

    def select_data(self):

        thh = Thread(target=lambda :self.updater())
        thh.start()
        print("select func running...")
        select_all = "select * from talabalar"
        dd = My_Db(query=select_all)
        self.result = dd.get_result()
        self.is_root = True

    pass


    #================ Thread funcsion ===============

    def insert_data_th(self):
        if self.is_root:
            id_1 = str(self.entry_1.get())
            id_2 = str(self.entry_2.get())
            id_3 = str(self.entry_3.get())
            id_4 = str(self.entry_4.get())

            if(id_1 != "" and id_2 != "" and id_3 != "" and id_4 != ""):
                try:
                    int(id_1)
                    self.is_root = False
                    self.result = ""
                    self.loading = tk.Label(self.oyna, font=("Arial", 20), text="Loading...")
                    self.loading.place(x=300, y=200)
                    self.t.remove_table()
                    th = Thread(target=lambda: self.insert_data())
                    th.start()
                except:
                    tkinter.messagebox.showerror("Diqqat","ID raqam bo'lishi kerak")
            else:
                tkinter.messagebox.showinfo("Diqqat","Iltimos barcha maydonlarni to'ldiring")


    def delete_data_th(self):
        if self.is_root:
            id_1 = str(self.entry_1.get())

            if(id_1 != ""):

                try:
                    int(id_1)
                    self.is_root = False
                    self.result = ""
                    self.loading = tk.Label(self.oyna, font=("Arial", 20), text="Loading...")
                    self.loading.place(x=300, y=200)
                    self.t.remove_table()
                    th = Thread(target=lambda: self.delete_data())
                    th.start()
                except:
                    tkinter.messagebox.showerror("Diqqat","ID raqamlardan tashkil topgan bo'lishi kerak")
            else:
                tkinter.messagebox.showinfo("Diqqat","ID raqamni kiritish majburiy")
        pass

    def update_data_th(self):

        if self.is_root:
            id_1 = str(self.entry_1.get())

            if(id_1 != ""):

                try:
                    int(id_1)
                    self.is_root = False
                    self.result = ""
                    self.loading = tk.Label(self.oyna, font=("Arial", 20), text="Loading...")
                    self.loading.place(x=300, y=200)
                    self.t.remove_table()
                    th = Thread(target=lambda: self.update_data())
                    th.start()
                except:
                    tkinter.messagebox.showerror("Diqqat", "ID raqamlardan tashkil topgan bo'lishi kerak")
            else:
                tkinter.messagebox.showinfo("Diqqat", "ID raqamni kiritish majburiy")
        pass


    def select_data_th(self):
        if self.is_root:
            self.is_root = False
            self.result = ""
            self.loading = tk.Label(self.oyna, font=("Arial", 20), text="Loading...")
            self.loading.place(x=300, y=200)
            self.t.remove_table()
            th = Thread(target=lambda: self.select_data())
            th.start()
        pass


if __name__ == "__main__":
    My_App()