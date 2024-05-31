from flask import Flask
from flask_login import LoginManager
from .auth import User
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)

from . import routes, auth, llm_api, file_management
app.register_blueprint(routes.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(llm_api.bp)
app.register_blueprint(file_management.bp)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
