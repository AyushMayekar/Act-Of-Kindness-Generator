# Act of Kindness Generator

Welcome to the Act of Kindness Generator repository! This project aims to spread positivity and kindness by providing users with daily random acts of kindness suggestions. By incorporating these acts into their daily lives, users can make a positive impact on others and foster a culture of kindness in their communities.

## Features
- **Random Acts of Kindness**: Receive daily notifications with random acts of kindness suggestions.
- **Customizable Preferred Time**: Set your preferred time for receiving notifications.
- **Persistent Storage**: Acts of kindness suggestions are stored in a text file, allowing users to add, remove, or modify suggestions as needed.
- **Notification System**: Utilizes the `plyer` library to display notifications directly on your desktop.
- **User Configuration**: Save user preferences such as preferred notification time in a JSON file.

## Tech Stack
- **Python**: Used for backend development and script execution.
- **plyer**: Library for displaying desktop notifications.
- **JSON**: Data format for storing user configurations.
- **datetime**: Module for handling date and time operations.

## Installation
1. **Setup**: Clone the repository to your local machine and install the required dependencies using 'pip install library_name' command from the command prompt.
2. **Configuration**: Customize your preferred notification time by editing the `AOKG.py` file at the end part of the code and replace the file paths in the code with your file paths(Kind_acts.txt & user_config.json).
3. **Execution**: Check for a batch file(SC.bat) with the command 'pythonw AOKG.py_file_path'(Replace the file path with your file path) in the cloned repository and place the batch file in the windows startup folder by pressing(win+R) and type command 'shell:startup'.  
4. **Check**: Check the task manager(ctrl+shift+esc) to see if the startup apps contain 'SC' named file with status enabled, if not enable it. 
5. **Enjoy**: Restart the Machine and wait for approx 2 minutes for the command prompt to pop up automatically, once the command prompt is displayed with the command 'pythonw AOKG.py_file_path', press 'Enter', close the command prompt and receive daily notifications with random acts of kindness to brighten your day!

## Screenshots

1.Example of a notification displaying a random act of kindness.
 ![1.](https://github.com/AyushMayekar/Act-Of-Kindness-Generator/blob/main/Screenshot%202024-05-05%20131511.png)
 
2.Screenshot of the `AOKG.py` file for setting preferred notification time.
![2.](https://github.com/AyushMayekar/Act-Of-Kindness-Generator/blob/main/Screenshot%202024-05-05%20132107.png) 

## Working 
Checkout the Youtube video by clicking on the image below!!

[![Watch the video](https://img.youtube.com/vi/bQkOR3RcZ9A/maxresdefault.jpg)](https://youtu.be/bQkOR3RcZ9A) 
## Contact
For more information about the Act of Kindness Generator, you can reach out to the project creator on [LinkedIn](https://www.linkedin.com/in/ayush-mayekar-b9b883284).

Thank you for spreading kindness with the Act of Kindness Generator! Together, let's make the world a better place, one act of kindness at a time. 🌟🤝🌍
