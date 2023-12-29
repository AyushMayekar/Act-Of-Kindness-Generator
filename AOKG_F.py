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
        self.logo_label.pack(padx=20,pady=20,expand=True)
        self.Button_1=ctk.CTkButton(master=self.page1_frame,text="NEXT",height=620)
        self.Button_1.pack(padx=10,pady=10)
        self.page1_frame.pack()
        self.page2_frame = ctk.CTkFrame(master=root) # Creates a frame for page 2 of the GUI
        self.page3_frame = ctk.CTkFrame(master=root) # Creates a frame for page 3 of the GUI
        self.page4_frame = ctk.CTkFrame(master=root) # Creates a frame for page 4 of the GUI
        self.root.title("KindnessApp") # Gives the Title for thr frame
        self.root.geometry("800x700") # Sets the Geometry(widthxheight) of the frame
ctk.set_default_color_theme("blue")
root=ctk.CTk() # Displays the frame
APP=Kindness_App(root) # Creating an object of the class      
root.mainloop()  # Runs an endless loop to keep our app running


    
           





