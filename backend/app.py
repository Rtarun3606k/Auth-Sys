
from flask import Flask,Blueprint


# config imports

from config import app


# import all blueprints

from Routes.loginRoutes import loginRegister



# register all blueprints
app.register_blueprint(loginRegister,url_prefix='/auth')