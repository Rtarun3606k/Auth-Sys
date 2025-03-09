
from flask import Flask,Blueprint


# config imports

from config import app


# import all blueprints

from Routes.loginRoutes import loginRegister

from Routes.DevConsole.devLoginRegister import  devLoginRegister



# register all blueprints
app.register_blueprint(loginRegister,url_prefix='/auth')
app.register_blueprint(devLoginRegister,url_prefix='/dev')