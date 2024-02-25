from flask import Flask, render_template,request
from AOKG import KindnessBackend

app = Flask(__name__)

backend = KindnessBackend(
        file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/kind_acts.txt',
        config_file_path='C:/Users/ayush/OneDrive/Desktop/Act Of Kindness Genrator/user_config.json'
    )


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/user_input',methods=['GET','POST'])
def input():
    if  request.method == 'POST':
        preferred_time=request.form.get('time')
        user_config=backend.load_user_config()
        user_config['Enter The Preferred Time For Notification'] = preferred_time
        backend.save_user_config(user_config)
        backend.schedule_backend()
    
        
        return render_template('/thank_you')
    return render_template('user_input.html')

@app.route('/thank_you')
def thankyou():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)



