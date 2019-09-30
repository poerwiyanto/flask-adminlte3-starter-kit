from app import app
from waitress import serve

if __name__ == '__main__':
    if app.config['ENV'] == 'development':
        app.run(host=app.config['HOST'], port=app.config['PORT'])
    elif app.config['ENV'] == 'production':
        serve(app, host=app.config['HOST'], port=app.config['PORT'])
