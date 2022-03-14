from flask import Flask

app = Flask(__name__)
app.secret_key = 'myprofileapp'



if __name__ == '__main__':
    from views import *

    # app_port = 5001
    # url = f'http://0.0.0.0:{app_port}'

    app.run(debug=False, host="0.0.0.0")   #, use_reloader=True)
