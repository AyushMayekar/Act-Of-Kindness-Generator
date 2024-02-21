from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/user_input')
def input():
    return render_template('user_input.html')

@app.route('/thank_you')
def thankyou():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)



