from .models import User
from app.utils.validation_msgs import\
    CHECK_USERNAME_MSG, DATA_REQUIRED_MSG, EQUAL_TO_MSG, LENGTH_MAX_MSG,\
    LENGTH_MIN_MSG
from flask_babel import _
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError


def check_username(form, field):
    """Check if username is taken."""
    user = User.query\
        .filter_by(username=field.data)\
        .first()
    if user is not None:
        raise ValidationError(CHECK_USERNAME_MSG)


class LoginForm(FlaskForm):
    password = PasswordField('password')
    username = StringField('username')


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(DATA_REQUIRED_MSG)])
    password = PasswordField('password', validators=[
        DataRequired(DATA_REQUIRED_MSG),
        Length(min=6, message=LENGTH_MIN_MSG)])
    retype_password = PasswordField('password', validators=[
        EqualTo('password', message=EQUAL_TO_MSG.format(_('Kata sandi')))])
    username = StringField('username', validators=[
        DataRequired(DATA_REQUIRED_MSG),
        Length(message=LENGTH_MAX_MSG, max=50),
        check_username])
