from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, UserMixin

bp = Blueprint('auth', __name__)

class User(UserMixin):
    users = {
        1: {"id": 1, "username": "admin", "password": "password"}
    }

    def __init__(self, id):
        self.id = id
        self.authenticated = True

    @staticmethod
    def get(user_id):
        if user_id in User.users:
            return User(user_id)
        return None

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simplified authentication for demo purposes
        for user_id, user_info in User.users.items():
            if user_info["username"] == username and user_info["password"] == password:
                user = User(user_id)
                login_user(user)
                return redirect(url_for('routes.dashboard'))
    return render_template('sign_in.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))
