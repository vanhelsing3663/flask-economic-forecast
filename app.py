from flask import Flask

app = Flask(__name__)


@app.route('/home')
def hello_world():  # put application's code here
    return 'Hello World!'


def registration_page():
    return


if __name__ == '__main__':
    app.run(debug=True)
