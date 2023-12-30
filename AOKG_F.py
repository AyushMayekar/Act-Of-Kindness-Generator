import customtkinter as ctk
from PIL import Image

class Kindness_App:
    def __init__(self,root):
        self.root = root
        self.page1_frame = ctk.CTkFrame(master=root) # Creates a frame for page 1 of the GUI
        # self.pil_image=Image.open("C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/KindAction.png")
        # self.resized_image=self.pil_image.resize((700,500), Image.LANCZOS)
        self.logo_image=ctk.CTkImage(Image.open("C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/KindAction.png"),size=(600,600))
        self.logo_label=ctk.CTkLabel(master=self.page1_frame,image=self.logo_image,text='')
        self.logo_label.pack(padx=20,pady=20)
        self.Button_1=ctk.CTkButton(master=self.page1_frame,text="NEXT",height=30,command=self.go_to_Page2,font=("ariel",15))
        self.Button_1.pack(padx=10,pady=10)
        self.page1_frame.pack()
        self.page2_frame = ctk.CTkFrame(master=root) # Creates a frame for page 2 of the GUI
        self.page3_frame = ctk.CTkFrame(master=root) # Creates a frame for page 3 of the GUI
        self.page4_frame = ctk.CTkFrame(master=root) # Creates a frame for page 4 of the GUI
        self.root.title("KindnessApp") # Gives the Title for thr frame
        self.root.geometry("800x700") # Sets the Geometry(widthxheight) of the frame
        # Method to traverse from page1 to page2
    def go_to_Page2(self):  
        self.page1_frame.pack_forget()
        self.wel_mes=ctk.CTkLabel(master=self.page2_frame,text="Welcome to KindnessApp!\n\n🌟 Get ready to embark on a journey of spreading joy and positivity! KindnessApp is here to make your day brighter by encouraging random acts of kindness. 🌈\n\nHow it works:\n1. Set your preferred notification time on the next page.\n2. Enable the toggle to receive daily reminders.\n3. Embrace the day's suggested act of kindness and make someone smile.\n\nRemember, even the smallest acts can make a big difference. Good luck on your kindness journey! 🌻💙",height=600,width=500,corner_radius=40,fg_color="green",font=("arial",20))
        self.wel_mes.pack(padx=10,pady=10)
        self.Button_2_1=ctk.CTkButton(master=self.page2_frame,text="NEXT",height=30,font=("ariel",15),command=self.go_to_Page3)
        self.Button_2_1.pack(padx=10,pady=10,side="right")
        self.Button_2_2=ctk.CTkButton(master=self.page2_frame,text="PREVIOUS",height=30,font=("ariel",15),command=self.go_to_page1)
        self.Button_2_2.pack(padx=10,pady=10,side="left")
        self.page2_frame.pack()
   # Method to go to page1 from page2
    def go_to_page1(self):
     for widget in self.page2_frame.winfo_children():
        widget.destroy()
     self.page2_frame.pack_forget()
     self.page1_frame.pack()
  # Method to go to page3 from page2
    def go_to_Page3(self):
     self.page2_frame.pack_forget()
     self.page3_frame.pack() 


ctk.set_default_color_theme("green")
root=ctk.CTk() # Displays the frame
APP=Kindness_App(root) # Creating an object of the class      
root.mainloop()  # Runs an endless loop to keep our app running


    
           





