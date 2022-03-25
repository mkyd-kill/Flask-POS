from flask import Blueprint, flash, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

view = Blueprint('view', __name__, url_prefix='')
COMPANY = 'Happy Club'

@view.route('/')
def home():
    return redirect(url_for('view.login'))

@view.route('/usr_login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        passwrd = request.form.get('password')
        
        from .validators import passwordStrength
        password = passwordStrength(passwrd)

        from .models import Admin
        admin_usr = Admin.query.all()

        new_pwd = generate_password_hash(password, 'sha256')

        if check_password_hash(admin_usr.password, new_pwd):
            flash('Welcome Admin', category='success')
            return redirect(url_for('dashboard.main'))
        else:
            flash('Incorrect Credentials. Please contact support for assistance', category='error')
    return render_template('signup/login.html', title='Happy Club | Login', company=COMPANY)
