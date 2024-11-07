from flask import Blueprint,render_template

views_bp = Blueprint('views', __name__)

@views_bp.route('/')

def index():
    return render_template('main.html')