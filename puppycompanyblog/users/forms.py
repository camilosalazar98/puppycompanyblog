from flask_wtf import FlaskForm
from wtforms import SelectField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.flie import Filefield,FileAllowed
