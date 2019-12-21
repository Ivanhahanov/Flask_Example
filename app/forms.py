from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, FileField, PasswordField, SubmitField  # maybe useful


class ExampleForm(FlaskForm):
    int_row = IntegerField('Поле с числами')
    str_row = StringField('Строковое поле')
    submit = SubmitField('Добавить')
