from app.home import home


@home.route('/home')
def index():
    return 'Home Page'