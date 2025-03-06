import customtkinter
import customtkinter as ctk
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracao_da_janela_inicial()
        self.background()
        self.login_screen()

    def configuracao_da_janela_inicial(self):
        self.geometry("1000x400")
        self.title("Car Rental")
        self.resizable(False, False)

    def background(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def login_screen(self):
        #Image
        self.img = PhotoImage(file="image.png")
        self.lb_img=ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=50, column=0, padx=0)

        self.title = ctk.CTkLabel(self, text="Join our family of renters", font=("Century Gothic bold",30))
        self.title.place(x=0, y=0)
        self.title.grid(row=0,column=0,pady=10,padx=10)

        #Forms
        self.frame_login = ctk.CTkFrame(self, width=400, height=300)
        self.frame_login.place(x=560, y=55)
        self.lb_title = ctk.CTkLabel(self.frame_login, text= "Enter your Username and Password", font=("Century Gothic bold",22),text_color='purple')
        self.lb_title.grid(row=0, column=0, padx=50,pady=50)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Username", font=("Century Gothic bold",15), corner_radius=15)
        self.username_login_entry.grid(row=1,column=0,pady=10,padx=10)

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Password", show='*', font=("Century Gothic bold",15),corner_radius=15)
        self.senha_login_entry.grid(row=2,column=0,pady=10,padx=10)

        self.look_password = ctk.CTkCheckBox(self.frame_login, width=300, text="Remember me", font=("Century Gothic bold",12),corner_radius=15)
        self.look_password.grid(row=3, column=0, pady=10,padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Login".upper(), font=("Century Gothic bold", 12),corner_radius=15, command=self.forms)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)


    def forms(self):
        self.frame_login.place_forget()

        #frame froms cads
        self.frame_loca = ctk.CTkFrame(self, width=400, height=100)
        self.frame_loca.place(x=630, y=55)

        self.car_model_entry = ctk.CTkEntry(self.frame_loca, width=300, placeholder_text="Enter the model", font=("Century Gothic bold",15), corner_radius=15)
        self.car_model_entry.grid(row=1,column=0,pady=10,padx=10)

        self.model_price = ctk.CTkEntry(self.frame_loca, width=300, placeholder_text="Enter the price", font=("Century Gothic bold", 15), corner_radius=15)
        self.model_price.grid(row=2, column=0, pady=10, padx=10)

        self.diary_entry = ctk.CTkEntry(self.frame_loca, width=150, placeholder_text="Number of days",font=("Century Gothic bold",15),corner_radius=15)
        self.diary_entry.grid(row=3,column=0,pady=10,padx=10)


        self.btn_car = ctk.CTkButton(self.frame_loca, width=300, text="Join the Ride".upper(), font=("Century Gothic bold", 12),corner_radius=15, command=self.open)
        self.btn_car.grid(row=4, column=0, pady=10, padx=10)

        self.text_box= ctk.CTkTextbox(self.frame_loca, width=300, height=400)
        self.text_box.grid(row=5,column=0, pady=10, padx=10)
        self.text_box.insert("0.0","Volkswagen Gol - R$ 150,00 per day\nChevrolet Onix - $ 180,00 per day\nFord Ka - $ 150,00 per day\nFiat Argo - $ 160,00 per day\nRenault Kwid - $ 140,00 per day\nToyota Corolla - $ 250,00 per day\nHonda Civic - $ 250,00 per day\nHyundai HB20 - $ 160,00 per day\nJeep Renegade - $ 200,00 per day")



    def open(self):
        text_model = self.car_model_entry.get()
        model_pricee = int(self.model_price.get())
        text_day = int(self.diary_entry.get())

        amount_pay = model_pricee*text_day

        print("You selected the car", text_model,"for",text_day,"day(s)")
        print("The amount to be paid is $", amount_pay)
        print("Enjoy your Ride!!!")


if __name__=="__main__":
    app = App()
    app.mainloop()