import schedule
import random
import time
from plyer import notification
 
file_path = 'C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt'


def print_random_act():
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
schedule.every().day.at("11:15").do(print_random_act)

while True:
  schedule.run_pending()
  # The interpretor checks every 30 sec if there's any execution left 
  time.sleep(30)







