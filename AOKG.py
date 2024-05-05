import random  # Import the random library for generating random numbers
import time  # Import the time library for time-related functions
from plyer import notification  # Import the notification module from plyer library for displaying notifications
import json  # Import the json library for working with JSON data
from datetime import datetime,timedelta  # Import the datetime class from the datetime module

class KindnessBackend:
    def __init__(self, file_path,config_file_path):
        self.file_path = file_path  # Set the file path for acts of kindness
        self.config_file_path = config_file_path  # Set the file path for user configurations
        

    # Method to load user configurations from the specified file
    def load_user_config(self):
        try:
            with open(self.config_file_path, 'r') as config_file:
                return json.load(config_file)  # Load user configurations from the JSON file
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file is not found

    # Method to save user configurations to the specified file
    def save_user_config(self, user_config):
        with open(self.config_file_path, "w") as config_file:
            json.dump(user_config, config_file)  # Save user configurations to the JSON file

    # Method to print a random act of kindness
    def print_random_act(self):
        user_config = self.load_user_config()
        preferred_time_str = user_config.get("preferred_time", "11:00")
        preferred_time = datetime.strptime(preferred_time_str, "%H:%M")
        while True:
         current_time = datetime.now().time()
         current_date = datetime.now().date()
         current_datetime = datetime.combine(datetime.now().date(), current_time)
         preferred_datetime = current_datetime.replace(hour=preferred_time.hour, minute=preferred_time.minute, second=0, microsecond=0)

         if preferred_datetime >= current_datetime:
            delta = preferred_datetime- current_datetime
         else:
            next_day = datetime.now() + timedelta(days=1)
            delta = datetime.combine(next_day.date(), preferred_time.time()) - current_datetime

         sec = delta.total_seconds() 
         time.sleep(sec)  # Sleep
         with open(self.file_path, 'r') as file:
            kind_acts = file.read().splitlines()  # Read acts of kindness from the file
         if kind_acts:  # Check if there are acts of kindness available
            selected_act = random.choice(kind_acts)  # Select a random act of kindness
            kind_acts.remove(selected_act)  # Remove the selected act from the list
            notification.notify("Today's Act of Kindness is:", message=selected_act,app_icon=r'C:\Users\ayush\OneDrive\Desktop\Act Of Kindness Genrator\BE-KIND.ico', timeout=10)  # Display the notification (Set the path for .ico file)
            with open(self.file_path,'w') as file:
               file.write('\n'.join(kind_acts))
         else:
            notification.notify("Congrats!!,You've completed 500 Acts of Kindness!!", timeout=10)  # Display a congratulatory notification
        

   

# Create an instance of the KindnessBackend class
backend = KindnessBackend(
        file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt',  # Specify the file path for acts of kindness
        config_file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/user_config.json'  # Specify the file path for user configurations
    )
preferred_time = "18:14" # Enter your Preferred Time for Notification
backend.save_user_config({"preferred_time": preferred_time})
backend.print_random_act()  # Print a random act of kindness