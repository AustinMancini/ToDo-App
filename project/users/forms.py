from flask_wtf import FlaskForm
from wtforms import StingField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError