from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PublicacionForm(FlaskForm):
    profesion = StringField('Profesión', validators=[DataRequired(), Length(max=100)])
    contenido = TextAreaField('Mensaje promocional', validators=[DataRequired(), Length(max=300)])
    telefono = StringField('Número telefónico', validators=[DataRequired(), Length(max=20)])
    email_contacto = StringField('Correo electrónico de contacto', validators=[DataRequired(), Email(), Length(max=150)])
    
    submit = SubmitField('Publicar')