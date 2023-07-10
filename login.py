import tkinter as tk
from tkinter import *
from tkinter import messagebox

Name = ["Antonio"]
Username = ["A"]
Password = ["A"]
Phone = ["933933933"]
Age = ["18"]
Personal = ["123456789"]

def ola():
    def login():
        usernameInserted = entryUser.get()
        passwordInserted = entryPassword.get()

        if usernameInserted in Username:
            index = Username.index(usernameInserted)
            if passwordInserted == Password[index]:
                lblLogin.place(relx=0.52, rely=0.65, anchor=CENTER)
                lblLogin.config(text="Login Sucefully", fg="green")
                window.destroy()
                def bank():
                    window = tk.Tk()
                    window.geometry("1080x600")
                    window.resizable(0, 0)
                    window.title("New Bank")

                    frame = tk.Frame(window, width=1080, height=600, bg="black")
                    frame.pack()

                    lblBank = tk.Label(master=frame, text="New Bank", bg="black", fg="white")
                    lblBank.place(relx=0.5, rely=0.08, anchor=CENTER)
                    lblBank.config(font=("Courier", 44))

                    money = IntVar()
                    money.set(f"0€")
                    lblMoney = tk.Label(master=frame, textvariable=money, bg="black", fg="white")
                    lblMoney.place(x=955, y=10)
                    lblMoney.config(font=("Courier", 44))

                    string = StringVar()
                    string.set(f"{Name[index]} {Age[index]}")
                    lblName = tk.Label(master=frame, textvariable=string, bg="black", fg="white")
                    lblName.place(x=15, y=20)
                    lblName.config(font=("Courier", 24))

                    Nif = StringVar()
                    Nif.set(f"Nif: {Personal[index]}")
                    lblNif = tk.Label(master=frame, textvariable=Nif, bg="black", fg="white")
                    lblNif.place(x=15, y=65)
                    lblNif.config(font=("Courier", 17))

                    number = StringVar()
                    number.set(f"Phone: {Phone[index]}")
                    number = tk.Label(master=frame, textvariable=number, bg="black", fg="white")
                    number.place(x=15, y=105)
                    number.config(font=("Courier", 17))

                    lbCopyright = tk.Label(master=frame, text="@Antonio Vaz", bg="black", fg="white")
                    lbCopyright.place(x=962, y=569)
                    lbCopyright.config(font=("Courier", 10))

                    def back():
                        window.destroy()
                        ola()
                    btnReturn = tk.Button(master=frame, text="Return",command=back, bg="white", fg="black")
                    btnReturn.place(x=20, y=540)
                    btnReturn.config(font=("Courier", 18))

                    window.mainloop()
                bank()
            else:
                lblLogin.place(relx=0.52, rely=0.65, anchor=CENTER)
                lblLogin.config(text="Wrong Password", fg="red")
        else:
            lblLogin.place(relx=0.52, rely=0.65, anchor=CENTER)
            lblLogin.config(text="Username not found", fg="red")

    def r():
        btnLogin.place(x=553453420, y=300)
        lblLogin.place(relx=5, rely=0.65, anchor=CENTER)

        def l():
            lblLogin.place(relx=5, rely=0.65, anchor=CENTER)
            btnR.config(text="Register", command=r)
            lblR.config(text="Register Now")
            btnRegister.place(y=3000)
            lblR.place(x=854, y=20)

            lblName.place(x=30000)
            entry_New_Name.place(x=30000)
            lblPhoneNumber.place(x=30000)
            entry_Phone_Number.place(x=30000)
            lblAge.place(x=30000)
            entry_Age.place(x=30000)
            lblPersonal.place(x=30000)
            entry_Personal.place(x=30000)

            ###############
            # USERNAME ZONE#
            ###############
            lblUser.place(x=300, y=200)
            entryUser.place(x=450, y=205)
            lblPassword.place(x=300, y=250)
            entryPassword.place(x=450, y=255)
            btnLogin.place(x=520, y=300)

        btnR.config(text="Login", command=l)
        lblR.config(text="Login Now")
        lblR.place(x=850, y=20)

        lblName = tk.Label(master=frame, text="Name:", bg="black", fg="white")
        lblName.place(x=300, y=150)
        lblName.config(font=("Courier", 20))

        entry_New_Name = tk.Entry(master=frame, bg="white", fg="black")
        entry_New_Name.place(x=450, y=155)
        entry_New_Name.config(font=("Courier", 18))

        ###########
        lblPhoneNumber = tk.Label(master=frame, text="Phone:", bg="black", fg="white")
        lblPhoneNumber.place(x=300, y=200)
        lblPhoneNumber.config(font=("Courier", 20))

        entry_Phone_Number = tk.Entry(master=frame, bg="white", fg="black")
        entry_Phone_Number.place(x=450, y=205)
        entry_Phone_Number.config(font=("Courier", 18))
        ##############

        ################
        # START AGE ZONE#
        ################
        lblAge = tk.Label(master=frame, text="Age:", bg="black", fg="white")
        lblAge.place(x=300, y=250)
        lblAge.config(font=("Courier", 20))

        entry_Age = tk.Entry(master=frame, bg="white", fg="black")
        entry_Age.place(x=450, y=255)
        entry_Age.config(font=("Courier", 18))
        ##############
        # END AGE ZONE#
        ##############

        #####################
        # START PERSONAL ZONE#
        #####################
        lblPersonal = tk.Label(master=frame, text="Nif:", bg="black", fg="white")
        lblPersonal.place(x=300, y=300)
        lblPersonal.config(font=("Courier", 20))

        entry_Personal = tk.Entry(master=frame, bg="white", fg="black")
        entry_Personal.place(x=450, y=305)
        entry_Personal.config(font=("Courier", 18))
        ###################
        # END PERSONAL ZONE#
        ###################

        ##############
        # START EXTRAS#
        lblUser.place(x=300, y=350)
        entryUser.place(x=450, y=355)

        lblPassword.place(x=300, y=400)
        entryPassword.place(x=450, y=405)

        ############
        # END EXTRAS#
        ############

        def register():
            newName = entry_New_Name.get()
            newPhone = entry_Phone_Number.get()
            newAge = entry_Age.get()
            newPersonal = entry_Personal.get()
            newUser = entryUser.get()
            newPassword = entryPassword.get()
            if newName!="" and newPhone!="" and newAge!="" and newPersonal!="" and newUser!="" and newPassword!="":
                try:
                    tel = int(newPhone)
                    if len(newPhone)==9:
                        try:
                            idade = int(newAge)
                            if idade>17:
                                if 120>idade:
                                    try:
                                        if len(newPersonal)==9:
                                            if newPersonal[0]=="2":
                                                if newUser not in Username:
                                                    Username.append(newUser)
                                                    Password.append(newPassword)
                                                    Phone.append(newPhone)
                                                    Personal.append(newPersonal)
                                                    Name.append(newName)
                                                    Age.append(newAge)
                                                    lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                                                    lblLogin.config(text="Register Sucefully", fg="green")
                                                else:
                                                    lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                                                    lblLogin.config(text="That username is already used", fg="red")
                                            else:
                                                lblLogin.config(text="Invalid NIF", fg="red")
                                        else:
                                            lblLogin.config(text="NIF need to have 9 digits", fg="red")

                                    except ValueError:
                                        lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                                        lblLogin.config(text="NIF can´t have letters", fg="red")

                                else:
                                    lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                                    lblLogin.config(text="Invalid Age", fg="red")
                            else:
                                lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                                lblLogin.config(text="Too new to create an account", fg="red")
                        except ValueError:
                            lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                            lblLogin.config(text="Age can´t have letters", fg="red")
                    else:
                        lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                        lblLogin.config(text="Phone have 9 digits", fg="red")
                except ValueError:
                    lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                    lblLogin.config(text="Phone can´t have letters", fg="red")
            else:
                lblLogin.place(relx=0.52, rely=0.9, anchor=CENTER)
                lblLogin.config(text="Fill All Zone", fg="red")

        ######################
        # REGISTER ZONE STARTS#
        ######################
        btnRegister = tk.Button(master=frame, text="Register", command=register, bg="white", fg="black")
        btnRegister.place(relx=0.53, rely=0.8, anchor=CENTER)
        btnRegister.config(font=("Courier", 18))

        ####################
        # REGISTER ZONE END#
        ####################

    window = tk.Tk()
    window.geometry("1080x600")
    window.resizable(0, 0)
    window.title("New Bank")

    frame = tk.Frame(window, width=1080, height=600, bg="black")
    frame.pack()

    lblBank = tk.Label(master=frame, text="New Bank", bg="black", fg="white")
    lblBank.place(relx=0.5, rely=0.08, anchor=CENTER)
    lblBank.config(font=("Courier", 44))

    ###############
    # USERNAME ZONE#
    ###############
    lblUser = tk.Label(master=frame, text="Username:", bg="black", fg="white")
    lblUser.place(x=300, y=200)
    lblUser.config(font=("Courier", 20))

    entryUser = tk.Entry(master=frame, bg="white", fg="black")
    entryUser.place(x=450, y=205)
    entryUser.config(font=("Courier", 18))

    ###############
    # PASSWORD ZONE#
    ###############
    lblPassword = tk.Label(master=frame, text="Password:", bg="black", fg="white")
    lblPassword.place(x=300, y=250)
    lblPassword.config(font=("Courier", 20))

    entryPassword = tk.Entry(master=frame, bg="white", fg="black",show="*")
    entryPassword.place(x=450, y=255)
    entryPassword.config(font=("Courier", 18))

    ############
    # LOGIN ZONE#
    ############

    btnLogin = tk.Button(master=frame, text="Login", command=login, bg="white", fg="black")
    btnLogin.place(x=520, y=300)
    btnLogin.config(font=("Courier", 18))

    lblLogin = tk.Label(master=frame, text="", bg="black")
    lblLogin.config(font=("Courier", 20))

    ################
    # COPYRIGHT ZONE#
    ################

    lbCopyright = tk.Label(master=frame, text="@Antonio Vaz", bg="black", fg="white")
    lbCopyright.place(x=962, y=569)
    lbCopyright.config(font=("Courier", 10))

    ###############
    # REGISTER ZONE#
    ###############

    lblR = tk.Label(master=frame, text="Register Now", bg="black", fg="white")
    lblR.place(x=850, y=20)
    lblR.config(font=("Courier", 20))

    btnR = tk.Button(master=frame, text="Register", command=r, bg="white", fg="black")
    btnR.place(x=900, y=60)
    btnR.config(font=("Courier", 15))

    def exit():
        messagebox.showinfo('Exit Window', 'Ty for your time!')
        window.destroy()

    btnExit = tk.Button(master=frame, text="Exit", command=exit, bg="white", fg="black")
    btnExit.place(x=20, y=540)
    btnExit.config(font=("Courier", 18))

    window.mainloop()
ola()