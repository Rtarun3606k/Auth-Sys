
from flask import Flask,Blueprint


# config imports

from config import app


# import all blueprints

from Routes.userConsole.userRoutes import userRoutes
from Routes.userConsole.loginRoutes import loginRegister

from Routes.DevConsole.devLoginRegister import  devLoginRegister
from Routes.DevConsole.devRoutes import  devRoutes

from Routes.AdminConsole.adminLoginRegister import adminLoginRegister



# register all blueprints
app.register_blueprint(loginRegister,url_prefix='/auth')
app.register_blueprint(devLoginRegister,url_prefix='/dev')
app.register_blueprint(devRoutes,url_prefix='/devRoutes')
app.register_blueprint(adminLoginRegister,url_prefix='/admin')