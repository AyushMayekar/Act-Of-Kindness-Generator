import schedule
import random
import time
from plyer import notification
import json
import threading



class KindnessBackend:
    def __init__(self, file_path, config_file_path):
        self.file_path = file_path
        self.config_file_path = config_file_path
        self.running=True 
        
       
        

    def load_user_config(self):
        try:
            with open(self.config_file_path, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            return {}

    def save_user_config(self, user_config):
        with open(self.config_file_path, "w") as config_file:
            json.dump(user_config, config_file)

    def print_random_act(self):
        user_config = self.load_user_config()
        preferred_time = user_config.get("Enter The Preferred Time For Notification", "11:00")

        with open(self.file_path, 'r') as file:
            kind_acts = file.read().splitlines()

        if kind_acts:
            selected_act = random.choice(kind_acts)
            kind_acts.remove(selected_act)
            notification.notify("Today's Act of Kindness is:", message=selected_act, timeout=10)
        else:
            notification.notify("Congrats!!,You've completed 500 Acts of Kindness!!", timeout=10)
          
            

    def schedule_backend(self):
        user_config = self.load_user_config()
        preferred_time = user_config.get("Enter The Preferred Time For Notification", "11:00")
        self.schedule_job=schedule.every().day.at(preferred_time).do(self.print_random_act)
        def schedule_task():
          while True:
           schedule.run_pending()
           time.sleep(5)
        threading.Thread(target=schedule_task(), daemon=True).start()    
        print("kaam karra")

    def stop(self):
        self.running=False

    def cancel_job(self):
         self.running=False
         if self.schedule_job:
            self.schedule_job.cancel_after()
        
        
        
    
 
    
# backend = KindnessBackend(
#         file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt',
#         config_file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/user_config.json'
#     )

# user_config=backend.load_user_config()
# preferred_time = '11:24'
# user_config['Enter The Preferred Time For Notification'] = preferred_time
# backend.save_user_config(user_config)
# backend.schedule_backend()
# backend.print_random_act()














