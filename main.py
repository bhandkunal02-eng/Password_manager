from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
 
    password_list = []


    password_letters=(random.choice(letters) for _ in range(nr_letters))
    password_symbol=(random.choice(symbols) for _ in range(nr_symbols))
    password_numbers=(random.choice(numbers) for _ in range(nr_numbers))


    password_list = list(password_letters) + list(password_symbol) + list(password_numbers)


    random.shuffle(password_list)
    password="".join(password_list)

    password_input.insert(0,password)

    

    print(f"Your password is: {password}")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    Email=Email_user_name_Entery.get()
    password=password_input.get()
    new_data={
        website:{
            "email":Email,
            "password":password,
        }
    }
    
    if len(website)==0 or len(password)==0 :
        messagebox.showerror(title="error",message="ERROR BRO ERROR!!")
   
    else:
        try:
            with open ("data.json","r") as f:
            # reading old data
                data=json.load(f)
                # Updating old data with new data
                data.update(new_data)
            
        except FileNotFoundError:
            with open ("data.json","w") as f:
                json.dump(new_data,f,indent=4)

        else:
             with open("data.json","w") as f:
            # Saving updated data
                json.dump(data,f,indent=4)         




        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
            
       
        
#---------------------------Search PAssword---------------------------------#
def find_password():
    website=website_input.get()
    try:
        with open("data.json","r") as f :
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="No data file found !")

    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email} \n password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"NO details of {website} website")


       

    

    

    



# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(width=200, height=200)
# nothing_label=Label(text="  ",fg="white")
# nothing_label.grid(column=0,row=0)
logo_img = PhotoImage(file="E:\Pyhon Basic to Advance ,Udemy\python_DAY-29_password_manager\password-manager-start\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=1)

website_label=Label(text="Website :")
website_label.grid(column=0,row=2)
website_input=Entry(width=60)
website_input.focus()
website_input.grid(column=1,row=2,columnspan=2)
Email_user_name_label=Label(text="Email/UserName :")
Email_user_name_label.grid(column=0,row=3)
Email_user_name_Entery=Entry(width=80)
Email_user_name_Entery.insert(0,"bhand.kunal02@gmail.com")
Email_user_name_Entery.grid(column=1,row=3,columnspan=4)
Password_label=Label(text="Password :")
Password_label.grid(column=0,row=4)
pass_generate_button=Button(text="Generate_Password",command=generate_password)
pass_generate_button.grid(column=3,row=4)
password_input=Entry(width=60)



password_input.grid(column=1,row=4,columnspan=2)
add_pass_button=Button(text="Add Details",width=70,command=save)
add_pass_button.grid(column=1,row=5,columnspan=3)

# Search button:

search_button=Button(text="Search",width=15,command=find_password)
search_button.grid(column=3,row=2,columnspan=2)






window.mainloop()