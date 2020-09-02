from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import TelField

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, message=("Nombre muy corto"))])
    lname = StringField('Apellido', validators=[DataRequired(), Length(min=2,message=("Apellido muy corto"))])
    phone = StringField('Telefono', validators=[DataRequired(), Length(min=8,max=9,message=("Telefono no valido"))])
    submit = SubmitField('Agregar contacto')


class LoginForm(FlaskForm):
    user = StringField('User name', validators=[DataRequired(), Length(min=2, message=("Usuario invalido"))])
    password = PasswordField('Password Please', validators=[DataRequired(), Length(min=8, message=("Contraseña muy corta"))])
    submit = SubmitField('Sing up')
