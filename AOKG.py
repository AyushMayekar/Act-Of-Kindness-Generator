# import random

# file_path = 'C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt'

# # Open the file in read mode
# with open(file_path, 'r') as file:
#     # Read each line and remove the newline character
#     kind_acts = file.read().splitlines()

# # Now, 'kind_acts' is a list containing each string from the file
#         act = random.choice(kind_acts)
#         print(act)


import schedule
import random
import time

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

 else:
      print("Congrats!!,You've completed 500 Acts of Kindness!!")
      
schedule.every().day.at("10:00").do(print_random_act)

while True:
  schedule.run_pending()
  time.sleep(30)







