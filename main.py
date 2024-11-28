from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')  # Or whatever template you wish to use

@app.route('/userscreen')
def userscreen():
    return render_template('userscreen.html')  # Replace with your actual template or logic


if __name__ == '__main__':
    app.run(debug=True)

