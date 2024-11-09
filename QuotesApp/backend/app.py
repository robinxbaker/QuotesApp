from flask import Flask
from config import Config
from models import db
from routes.auth import auth
from routes.quotes import quotes
from routes.users import users
from routes.ratings import ratings
from routes.admin import admin
from flask_cors import CORS
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mail = Mail()
mail.init_app(app)

db.init_app(app)

# Register Blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(quotes, url_prefix='/api/quotes')
app.register_blueprint(users, url_prefix='/api/users')
app.register_blueprint(ratings, url_prefix='/api/ratings')
app.register_blueprint(admin, url_prefix='/api/admin')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)