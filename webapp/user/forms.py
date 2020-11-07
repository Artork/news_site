from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from webapp.user.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    roles = SelectField('Выбирите вашу роль', choices=[('buy', 'Покупатель'), ('sel', 'Продавец')])
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField()
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    #def validate_username(self, username):
     #   users_count = User.query.filter_by(username=username.data).count()
    #    if users_count > 0:
    #        raise ValidationError('Пользователь с таким именем уже зарегистрирован')       user_count = User.query.filter_by()
    #def validate_email(self, email):
     #   email_count = User.query.filter_by(email=email.data).count()
    #    if users_count > 0:
    #        raise ValidationError('Данный email уже занят')
        