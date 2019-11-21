from yoda import app

@app.route('/')
@app.route('/index')
def index( ):
    return 'Olá Mundão'