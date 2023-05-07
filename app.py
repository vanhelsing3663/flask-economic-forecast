from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from validators.registration_check import CheckRegister

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/economical_site'
app.secret_key = 'mysecretkey'
db = SQLAlchemy(app)
valid = CheckRegister()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)


@app.route('/')
def hello_world():  # put application's code here
    return 'Будущая домашняя страница '


@app.route('/register', methods=["GET", "POST"])
def registration_handler():
    """Примерная страница регистрации в будущем будет меняться"""
    if request.method == 'GET':
        return render_template("registration.html")
    else:
        login = request.form["email"]
        password = request.form["password"]
        if not valid.is_valid_email(login):
            flash("Проверьте корректность email")
        elif not valid.is_valid_password(password):
            flash("Проверьте корректность ввода пароля")
        else:
            pswd_hash = generate_password_hash(password)
            if check_password_hash(pswd_hash, password):
                new_user = Users(email=login, password=pswd_hash)
                db.session.add(new_user)
                db.session.commit()
                return render_template("home.html")
    return render_template("registration.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
