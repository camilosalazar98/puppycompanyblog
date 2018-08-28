from flask_wtf import FlaskForm
from wtforms import SelectField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.flie import Filefield,FileAllowed


from flask_login import current_user
from puppycompanyblog.models import User


class LoginForm(FlaskForm):
    email = StringFeild('Email', validators =[DataRequired(),Email()])
    password = Password('Password',validators = [DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email  = StringFeild('Email', validators =[DataRequired(),Email()])
    username = StringFeild('UserName', validators =[DataRequired(),Email()])
    pasword = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm'),message = 'Password must match!'])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')



    def check_email(self,field):
        if User.query.filter_by(email = field.data).first()
            raise ValidationError('Your email has been registered already!')


    def check_username(self,field):
        if User.query.filter_by(email = field.data).first()
            raise ValidationError('Your username has been registered already!')

class UpdateUserFrom(FlaskForm):
    email = StringFeild('Email',validators = [DataRequired(),Email()])
    username = StringFeild('UserName',validators = [DataRequired(),Email()])
    picture = Filefield('Update Profile Picture',validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first()
            raise ValidationError('Your email has been registered already!')


    def check_username(self,field):
        if User.query.filter_by(email = field.data).first()
            raise ValidationError('Your username has been registered already!')
