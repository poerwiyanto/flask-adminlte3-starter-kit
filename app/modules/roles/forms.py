from app.utils.validation_msgs import DATA_REQUIRED_MSG
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(DATA_REQUIRED_MSG)])
