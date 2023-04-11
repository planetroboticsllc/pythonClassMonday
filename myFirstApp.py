import customtkinter as ctk
import tkinter

def enter_clicked():
    #print("enter clicked!")
    userName = entry.get()
    addString = address.get()
    print(userName)
    print(addString)
    ageNum = int(age.get()) + 5
    strList = [userName, addString, str(ageNum)]
    infoLabel.configure(text='\n'.join(strList))

app = ctk.CTk()
app.title("My First App")
app.geometry("500x300")

label = ctk.CTkLabel(app, text="Name: ", font=ctk.CTkFont(size=20))
label.grid(row=0, column=0, padx=5, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter your name",
                     font=ctk.CTkFont(size=20),
                     width=340, height=20)
entry.grid(row=0, column=1, padx=5, pady=5)

labelAddress = ctk.CTkLabel(app, text="Address: ", font=ctk.CTkFont(size=20))
labelAddress.grid(row=1, column=0, padx=5, pady=5)

address = ctk.CTkEntry(app, placeholder_text="Enter your address",
                       font=ctk.CTkFont(size=20),
                       width=340, height=20)
address.grid(row=1, column=1, padx=5, pady=5)

ageLabel = ctk.CTkLabel(app, text="Age: ", font=ctk.CTkFont(size=20))
ageLabel.grid(row=2, column=0, padx=5, pady=5)

age = ctk.CTkEntry(app, placeholder_text="Enter age", font=ctk.CTkFont(size=20),
                   width=340, height=20)
age.grid(row=2, column=1, padx=5, pady=5)

btn = ctk.CTkButton(app, text="Enter", command=enter_clicked)
btn.grid(row=3, column=1, padx=5, pady=5)

infoLabel = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=15))
infoLabel.grid(row=3, column=2, padx=5, pady=5)

app.mainloop()
