from flask import Flask # module for http server
from config import Config # config of your app
from flask_sqlalchemy import SQLAlchemy # module for work with database
from flask_migrate import Migrate # module to generate migrations
from flask_login import LoginManager # module for login an security of your application
from flask_bootstrap import Bootstrap

app = Flask(__name__) # init flask http server
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager()
login.init_app(app)
login.login_view = "login"
bootstrap = Bootstrap(app)

from app import routes, models
