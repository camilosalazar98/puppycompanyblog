# puppycompanyblog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)


app.config['SECRET_KEY'] = #make my form work
########################
#####Data Base setup####
########################
basedir = os.path.adspath(os.path.dirname(__file__))
app.config['SQlALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLALchemy(app)
Migrate(app,db)

#########################


#########################
#Login configs
login_manager = LoginManager()#create a object of login LoginManager

login_manager.init_app(app)#pass in the app
login_manager.login_veiw = 'users.login'



from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages
from puppycompanyblog.users.views import users
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
