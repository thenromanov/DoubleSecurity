from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class LoginForm(FlaskForm):
    astronautId = StringField('id астронавта', validators=[DataRequired()])
    astronautToken = StringField('Пароль астронавта', validators=[DataRequired()])
    capitanId = StringField('id капитана', validators=[DataRequired()])
    capitanToken = StringField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
