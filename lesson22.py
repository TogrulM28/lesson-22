import tkinter as tk
import json

class Username:
    def __init__(self,name,password):
        self.name = name
        self.password = password

def log_in():
    user = username_entry.get()
    pwd = password_entry.get()
    
    user1 = Username(user,pwd)

    try:
        with open(f"lesson 22/{user}.json","r") as f:
            login_result.config(text="Logged in successfully!!!",fg='green')
    except FileNotFoundError:
        with open(f"lesson 22/{user}.json","w") as f:
            user2 = json.dumps(user1.__dict__)
            f.write(user2)
        login_result.config(text='Account created!',fg='black')

login = tk.Tk()
login.title("Login")
login.geometry('550x750')

login_lbl = tk.Label(text="Login",font=("sanserif",25,'bold'))
login_lbl.pack(pady=20)

username_lbl = tk.Label(text="username:", font=('cambria',20))
username_lbl.pack(pady=10)

username_entry = tk.Entry(textvariable=tk.StringVar,font=('helvetica',15))
username_entry.pack()

password_lbl = tk.Label(text="password:", font=('cambria',20))
password_lbl.pack(pady=10)

password_entry = tk.Entry(textvariable=tk.StringVar,font=('helvetica',15),show="•")
password_entry.pack()

login_btn = tk.Button(text='login',font=('helvetica',15,'bold'),bg='#24c130',fg='white',command=log_in)
login_btn.pack(pady=5)

login_result = tk.Label(text="",font=("helvetica",15))
login_result.pack(pady=10)

login.mainloop()