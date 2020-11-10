from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

from counties import counties

class RegistrationForm(FlaskForm):

    company = StringField('Company *', 
                        validators=[DataRequired(),Length(min=2, max=30)])
    email = StringField('Email *', 
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password *", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password *", validators=[DataRequired(), EqualTo('password')])
    address1 = StringField('Address *', 
                        validators=[DataRequired(),Length(min=2, max=30)])
    address2 = StringField("Address line 2", validators=[Optional(), Length(min=2, max=30)])                        
    county = SelectField('County *', 
                        choices=counties,
                        validators=[DataRequired(),Length(min=2, max=30)])

    # could check for valid eircode or even use the eircode to query for addess?
    # maybe even check from eircode then ask user is this the address and let them adjust accordingly
    eircode= StringField('Eircode *', 
                        validators=[DataRequired(),Length(min=2, max=30)])


    submit = SubmitField("Register Now!")


class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    
    remember = BooleanField("Remember me") # cookie stuff ngl dont really know anything about this 
    submit = SubmitField("Login!")  