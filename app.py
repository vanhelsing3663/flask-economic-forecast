from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from validators.registration_check import CheckUserPassword, CheckUserEmail
from config import DATABASE, SECRET_KEY

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123090704Qq@localhost/alex_sql'
app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.secret_key = SECRET_KEY

validator_password = CheckUserPassword()
validator_email = CheckUserEmail()
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/account')
def account():
    return render_template("account.html")

@app.route('/register', methods=["GET", "POST"])
def registration_handler():
    """Примерная страница регистрации в будущем будет меняться"""
    if request.method == 'GET':
        return render_template("registration.html")
    else:
        login = request.form["email"]
        password = request.form["password"]
        if not validator_email.is_valid_lenght(login):
            flash("Убедитесь , что вы ввели допустимую длину")
        elif not validator_email.email_should_not_exceed_voltage(login):
            flash("Убедитесь , что вы ввели допустимую длину не превышающую 256 символов")
        elif not validator_email.count_dog_symbol(login):
            flash("Убедитесь , что в вашем email присутствует символ @")
        elif not validator_password.is_valid_lenght(password):
            flash("Убедитесь , что вы ввели пароль более 8 символов")
        elif not validator_password.checking_that_the_password_contains_at_least_one_digit(password):
            flash("Убедитесь , что в вашем пароле присутствует хотя бы одна цифра")
        elif not validator_password.has_uppercase(password):
            flash("Убедитесь , что в вашем пароле есть хотя бы одна заглавная буква")
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
