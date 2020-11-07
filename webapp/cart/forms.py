from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class CartForm(FlaskForm):
#такая форма нужна или нет ?


class CartItemForm(FlaskForm):
    quantity = IntegerField('Количество', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Заказать', render_kw={"class": "btn btn-primary"})
#delete = SubmitField('Delete', validators=delete())


