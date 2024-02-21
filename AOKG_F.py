import customtkinter as ctk
from PIL import Image
from AOKG import KindnessBackend
import threading
import time


class Kindness_App:
    def __init__(self,root):
        self.root = root
        self.page1_frame = ctk.CTkFrame(master=root) # Creates a frame for page 1 of the GUI
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
        self.stop_event=threading.Event()


        # Method to traverse from page1 to page2
    def go_to_Page2(self):
        for widget in self.page3_frame.winfo_children():
         widget.destroy()  
        self.page3_frame.pack_forget()
        self.page1_frame.pack_forget()
        
        self.wel_mes=ctk.CTkLabel(master=self.page2_frame,
                                  text="Welcome to KindnessApp!\n\n🌟 Get ready to embark on a journey of spreading joy and positivity! KindnessApp is here to make your day brighter by encouraging random acts of kindness. 🌈\n\nHow it works:\n1. Set your preferred notification time on the next page.\n2. Enable the toggle to receive daily reminders.\n3. Embrace the day's suggested act of kindness and make someone smile.\n\nRemember, even the smallest acts can make a big difference. Good luck on your kindness journey! 🌻💙",
                                  height=600,
                                  width=500,corner_radius=40,
                                  fg_color='Midnight Blue',
                                  font=("arial",20))
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
     for widget in self.page4_frame.winfo_children():
         widget.destroy()
         self.page4_frame.pack_forget()
     for widget in self.page2_frame.winfo_children():
         widget.destroy()  
     self.page2_frame.pack_forget()
     self.User_prompt=ctk.CTkLabel(master=self.page3_frame,text='Enter your preferred time for notifications (format HH:MM, e.g., 09:30,21:00,15:40):',
                                   height=100,width=500,corner_radius=30,fg_color='Midnight Blue', font=("arial",20))
     self.User_prompt.pack(padx=20,pady=20)
     self.User_input=ctk.CTkTextbox(master=self.page3_frame,height=20,width=90,corner_radius=10,font=('arial',15),fg_color='white',text_color='black')
     self.User_input.pack(padx=10,pady=10)
     self.submit_toggle=ctk.CTkSwitch(master=self.page3_frame,switch_height=20,height=30,width=60,text='',command=self.backend_integration)
     self.submit_toggle.pack(padx=10,pady=10)
     self.Button_3_1=ctk.CTkButton(master=self.page3_frame,text="NEXT",height=30,font=("ariel",15),command=self.go_to_page4)
     self.Button_3_1.pack(padx=10,pady=10,side="right")
     self.Button_3_2=ctk.CTkButton(master=self.page3_frame,text="PREVIOUS",height=30,font=("ariel",15),command=self.go_to_Page2)
     self.Button_3_2.pack(padx=10,pady=10,side="left")
     self.page3_frame.pack() 
    
    def go_to_page4(self):
       for widget in self.page3_frame.winfo_children():
         widget.destroy()  
       self.page3_frame.pack_forget()
       self.wel_mes=ctk.CTkLabel(master=self.page4_frame,
                                  text="Thank you for choosing KindnessApp! 🌟 \nYour commitment to spreading joy and positivity makes the world a better place.\n Keep embracing kindness, and let's continue making a positive impact together. 😊💙",
                                  height=650,
                                  width=500,corner_radius=20,
                                  fg_color='Midnight Blue',
                                  font=("arial",20))
       self.wel_mes.pack(padx=10,pady=10)
       self.Button_4_1=ctk.CTkButton(master=self.page4_frame,text="NEXT",height=30,font=("ariel",15),command=self.stop_gui)
       self.Button_4_1.pack(padx=10,pady=10,side="right")
       self.Button_4_2=ctk.CTkButton(master=self.page4_frame,text="PREVIOUS",height=30,font=("ariel",15),command=self.go_to_Page3)
       self.Button_4_2.pack(padx=10,pady=10,side="left")
       self.page4_frame.pack()


    # Method to integrate Backend
    def backend_integration(self):
       self.current_value=self.submit_toggle.get()
       if self.current_value==1:
          self.preferred_time=self.User_input.get('0.0','end')
         
          self.backend = KindnessBackend(
          file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt',
          config_file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/user_config.json'
          )
          self.user_config=self.backend.load_user_config()
          self.user_config['Enter The Preferred Time For Notification'] =self.preferred_time
          self.backend.save_user_config(self.user_config)
          self.backend_thread=threading.Thread(target=self.delaying_backend)
          self.backend_thread.start()
       else:
          pass
        #   self.stop_backend()
          
          

    # def stop_backend(self):
    #    if self.backend_thread and self.backend_thread.is_alive():
    #     self.backend.stop()
    #     self.backend_thread.join()

    def stop_gui(self):
       self.root.destroy()      

    def delaying_backend(self):
      try:
       while not self.stop_event.is_set():
           print("runnning thread")
           self.backend.schedule_backend()
           time.sleep(10)
      except Exception as e:
       print("Exception Occured in Thread : ",e)
      finally:
          print("thread stopped") 
        
       
       
                
          
  
            
    

ctk.set_default_color_theme("green")
root=ctk.CTk() # Displays the frame
APP=Kindness_App(root) # Creating an object of the class    
root.mainloop()  # Runs an endless loop to keep our app running


    
           





