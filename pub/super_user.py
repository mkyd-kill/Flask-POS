from flask import Blueprint, redirect, render_template, request, url_for
from .view import COMPANY
from .database import db_session
from dotenv import load_dotenv
import os

super_usr = Blueprint('super_user', __name__, url_prefix='')

_CREDENTIALS = 'pub/settings/.env'
load_dotenv(dotenv_path=_CREDENTIALS)

@super_usr.route('/super-admin/login', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        username = request.form.get('username')
        passwrd = request.form.get('password')

        from .validators import passwordStrength
        password = passwordStrength(passwrd)

        if username == os.getenv('SUPER_USER') and password == os.getenv('PASSWORD'):
            return redirect(url_for('super_user.add_new'))

    return render_template('signup/super.html', company=COMPANY)

@super_usr.route('/super-user/admin/add-new-user', methods=['POST', 'GET'])
def add_new():    
    if request.method == 'POST':
        pass
    return render_template('admin/super-dashboard.html')