import schedule
import random
import time
from plyer import notification
import json
 
file_path = 'C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt' # Dataset File
config_file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/user_config.json' # User Interaction File

# Loading the User_Config file for User Interaction
def load_user_config():
   try:
      with open(config_file_path,'r') as config_file: # Opening the File in Read Mode
          return json.load(config_file)
     
   except FileNotFoundError:
      return {}

# Saving the loaded Info or if file not found making a new json file
def save_user_config(user_config):
   with open(config_file_path, "w") as config_file: # Opening the file in write mode
      json.dump(user_config, config_file)
# Prompting user for its Preferred time of notification
user_config=load_user_config()
preferred_time = input("Enter your preferred time for notifications (format HH:MM, e.g., 09:30): ")
user_config['Enter The Preferred Time For Notification'] = preferred_time
save_user_config(user_config)
def print_random_act():
 user_config=load_user_config()
 preferred_time=user_config.get("Enter The Preferred Time For Notification","11:00")
    # Open the file in read mode
 with open(file_path, 'r') as file:
    # Read each line and remove the newline character
    kind_acts = file.read().splitlines()
 if kind_acts:
      # Now, 'kind_acts' is a list containing each string from the file
     selected_act = random.choice(kind_acts)
     print(selected_act)
     kind_acts.remove(selected_act)
     # Notification system
     notification.notify("Today's Act of Kindness is:",message=selected_act,timeout=10)
    

 else:
      print("Congrats!!,You've completed 500 Acts of Kindness!!")
      
# Scheduling feature
user_config=load_user_config()
preferred_time=user_config.get("Enter The Preferred Time For Notification","11:00")      
schedule.every().day.at(preferred_time).do(print_random_act)

while True:
  schedule.run_pending()
  # The interpretor checks every 30 sec if there's any execution left 
  time.sleep(10)







