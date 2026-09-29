from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message='El usuario es obligatorio'),
                                                  Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres')])
    email = StringField('Correo', validators=[DataRequired(message='El correo es obligatorio'),
                                              Email(message='Escribe un correo válido')])
    password = PasswordField('Contraseña', validators=[DataRequired(message='La contraseña es obligatoria'),
                                                       Length(min=6, message='La contraseña debe tener al menos 6 caracteres')])
    confirm_password = PasswordField('Confirmar contraseña', validators=[EqualTo('password', message='Las contraseñas no coinciden')])


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message='El usuario es obligatorio')])
    password = PasswordField('Contraseña', validators=[DataRequired(message='La contraseña es obligatoria')])


class EditProfileForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message='El usuario es obligatorio'),
                                                  Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres')])
    email = StringField('Correo', validators=[DataRequired(message='El correo es obligatorio'),
                                              Email(message='Escribe un correo válido')])
