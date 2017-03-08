


from flask import Flask

app = Flask(__name__)



from views import *

if __name__ == '__main__':
    app.run()


    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://richard:1220@localhost/todoapp'
