from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import TelField

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired("Ingrese un nombre"), Length(min=2)])
    lname = StringField('Apellido', validators=[DataRequired("Ingrese un apellido"), Length(min=2)])
    phone = StringField('Telefono', validators=[DataRequired("Ingrese números unicamente"), Length(min=8,max=9)])
    submit = SubmitField('Agregar contacto')