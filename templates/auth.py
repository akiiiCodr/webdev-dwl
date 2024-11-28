from flask import Blueprint, render_template, request, flash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('login.html')  # Adjust the template name as needed

@auth_bp.route('/home')
def home():
    return render_template('main.html')

# @auth_bp.route('/logout', methods=['GET', 'POST'])
# def logout():
#     return render_template('home.html')

@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@auth_bp.route('/contact-us')
def contact():
    return render_template('contacts.html')

@auth_bp.route('/payment')
def payment():
    return render_template('payment.html')

@auth_bp.route('/tenant')
def tenant():
    return render_template('tenant.html')

@auth_bp.route('/admin')
def admin():
    return render_template('admin.html')

@auth_bp.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')



