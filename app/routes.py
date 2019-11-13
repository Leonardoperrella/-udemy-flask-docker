from app.home import home


def load(app):
    app.register_blueprint(home)

'''
from flask import request
def load(app):
    @app.route('/home')
    def home():

        return 'Home Page'

    @app.route('/')
    def showname():
        name = request.args.get("name")
        return f'Name: {name}'

    @app.route('/name')
    @app.route('/name/<name>')
    def showname_param(name=None):
        if not name:
            return 'Nome não foi  preenchido!'
        return name
'''