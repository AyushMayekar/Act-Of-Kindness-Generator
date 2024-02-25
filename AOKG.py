import schedule  # Import the schedule library for task scheduling
import random  # Import the random library for generating random numbers
import time  # Import the time library for time-related functions
from plyer import notification  # Import the notification module from plyer library for displaying notifications
import json  # Import the json library for working with JSON data
from datetime import datetime  # Import the datetime class from the datetime module

class KindnessBackend:
    def __init__(self, file_path, config_file_path):
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
        user_config = self.load_user_config()  # Load user configurations
        preferred_time = user_config.get("Enter The Preferred Time For Notification", "11:00")  # Get preferred notification time

        with open(self.file_path, 'r') as file:
            kind_acts = file.read().splitlines()  # Read acts of kindness from the file

        if kind_acts:  # Check if there are acts of kindness available
            selected_act = random.choice(kind_acts)  # Select a random act of kindness
            kind_acts.remove(selected_act)  # Remove the selected act from the list
            notification.notify("Today's Act of Kindness is:", message=selected_act, timeout=10)  # Display the notification
        else:
            notification.notify("Congrats!!,You've completed 500 Acts of Kindness!!", timeout=10)  # Display a congratulatory notification

    # Method to schedule the backend for displaying notifications
    def schedule_backend(self):
        user_config = self.load_user_config()  # Load user configurations
        preferred_time = user_config.get("Enter The Preferred Time For Notification", "11:00")  # Get preferred notification time
        self.schedule_job = schedule.every().day.at(preferred_time).do(self.print_random_act)  # Schedule the print_random_act method
        while True:
           schedule.run_pending()  # Run pending scheduled tasks
           time.sleep(5)  # Sleep for 5 seconds

    # Method to get the preferred notification time from the user
    def get_preferred_time(self):
        while True:
            self.preferred_time = input('\n\n\tPlease Enter Your Preferred Time for Notifications (HH:MM Format): ')  # Prompt user for input
            try:
                datetime.strptime(self.preferred_time, '%H:%M')  # Validate the input format
                break  # Break the loop if the format is correct
            except ValueError:
                print ('Incorrect format, please use HH:MM')  # Display error message for incorrect format
        return self.preferred_time  # Return the preferred time

# Create an instance of the KindnessBackend class
backend = KindnessBackend(
        file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt',  # Specify the file path for acts of kindness
        config_file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/user_config.json'  # Specify the file path for user configurations
    )
# Display welcome message
print("\n\t\tWelcome to KindnessApp!🌟\n\tGet ready to embark on a journey of spreading joy and positivity!\n\tKindnessApp is here to make your day brighter by encouraging random acts of kindness.🌈\n\n\tHow it works:\n\t1. Set your preferred notification time below.\n\t2. Press Enter and get started.\n\t3. Embrace the day's suggested act of kindness and make someone smile.\n\tRemember, even the smallest acts can make a big difference. Good luck on your kindness journey! 🌻💙")
user_config = backend.load_user_config()  # Load user configurations
preferred_time = backend.get_preferred_time()  # Get preferred notification time from the user
# Display thank you message
print("\n\n\t\tThank you for choosing KindnessApp! 🌟\n\n\tYour commitment to spreading joy and positivity makes the world a better place.\n\t Keep embracing kindness, and let's continue making a positive impact together. 😊💙\n\n")
# Display exit message
print("\n\t\t PLEASE CLOSE THE TERMINAL TO EXIT\n\n")
user_config['Enter The Preferred Time For Notification'] = preferred_time  # Update user configurations with preferred notification time
backend.save_user_config(user_config)  # Save updated user configurations
backend.schedule_backend()  # Schedule backend for displaying notifications
backend.print_random_act()  # Print a random act of kindness












