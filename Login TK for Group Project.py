import tkinter as tk
from tkinter import messagebox

#creating window object
form = tk.Tk()
form.title("Restration Form")

 

def openwindow():
    def signin():
        openfile = open("details.txt", "r")
        totallines = openfile.readlines()
        firstname = new_ftext.get()
        email = new_etext.get()
        
        for i in totallines:
            eachline = i.split("|")
            thefirstname = eachline[0].strip("\n")
            thelastname = eachline[1].strip("\n")
            theemail = eachline[2].strip("\n")
            checker = False
            if firstname == thefirstname and email == theemail:
                checker = True
                break

        if checker == True:
            messagebox.showinfo("Information", "Login Success! Please close this window.")
        else:
            messagebox.showerror("Failed", "Login Failed")



    window = tk.Toplevel()
    window.title("Login Form")
    newframe = tk.Frame(window)
    newframe.grid(padx=10, pady=10)
    new_label = tk.Label(newframe, text = "Sign In")
    new_label.grid(row=0, column= 0, columnspan= 2, pady=5, sticky="we")

    new_flabel = tk.Label(newframe, text = "First name:")
    new_flabel.grid(row = 1, column= 0,pady=5, sticky="w")
    new_elabel = tk.Label(newframe, text = "Email:")
    new_elabel.grid(row = 2, column= 0,pady=5, sticky="w")
    new_ftext = tk.Entry(newframe)
    new_ftext.grid(row = 1, column= 1,pady=5)
    new_etext = tk.Entry(newframe)
    new_etext.grid(row = 2, column= 1,pady=5)
    lbutton = tk.Button(newframe, text = "Sign In", command = signin)
    lbutton.grid(row = 3, column= 0, columnspan= 2,pady=5)


def register():
    detail_file = open("details.txt", "w")
    detail_file.close()
    new_detail_file = open("details.txt", "a")

    fname = ftext.get()
    lname = ltext.get()
    email = etext.get()
  

    if len(fname) > 1:
        if len(lname) > 1:
            if len(email) > 1:
                if "@" in email and "." in email:
                    new_detail_file.write(fname + "|" + lname + "|" + email + "\n")
                    new_detail_file.close()
                    messagebox.showinfo("Congratulations","Registration Successful!!")
                else:
                    messagebox.showerror("Error","Please enter a valid email")       
            else:
                messagebox.showerror("Error","Please do not leave email field blank")
        else:
            messagebox.showerror("Error","Please do not leave last name field blank")
    else:
        messagebox.showerror("Error","Please do not leave first name field blank")





frame = tk.Frame(form)
frame.grid(padx=10, pady=10)
tlabel = tk.Label(frame, text = "Registration Form")
tlabel.grid(row=0, column= 0, columnspan= 2, pady=5, sticky="we")
flabel = tk.Label(frame, text = "Enter first name:")
flabel.grid(row = 1, column= 0,pady=5, sticky="w")
llabel = tk.Label(frame, text = "Enter Last name:")
llabel.grid(row = 2, column= 0,pady=5, sticky="w")
elabel = tk.Label(frame, text = "Enter email:")
elabel.grid(row = 3, column= 0,pady=5, sticky="w")
ftext = tk.Entry(frame)
ftext.grid(row = 1, column= 1,pady=5)
ltext = tk.Entry(frame)
ltext.grid(row = 2, column= 1,pady=5)
etext = tk.Entry(frame)
etext.grid(row = 3, column= 1,pady=5)
rbutton = tk.Button(frame, text = "Register", command=register)
rbutton.grid(row = 4, column= 0, columnspan= 2,pady=5)

sbutton = tk.Button(frame, text = "Already registered? click this button to sign in", command=openwindow)
sbutton.grid(row = 5, column= 0, columnspan= 2,pady=5)
form.mainloop()




    
    
    
    


    
