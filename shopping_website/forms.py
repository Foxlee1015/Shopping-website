from wtforms import Form, PasswordField, validators, StringField, SubmitField, TextAreaField

class LoginForm(Form):
    email = TextAreaField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.data_required()])
    submit = SubmitField('Login')

class RegistrationForm(Form):
    username = TextAreaField('Username', [validators.Length(min=4, max=20)])
    email = TextAreaField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.data_required(),
                                          validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class RequestResetForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [validators.data_required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Reset Password')

class BoardForm(Form):
    title = TextAreaField('Title', [validators.Length(min=1, max=20)])
    content = TextAreaField('Content', [validators.Length(min=10, max=50)])
    password = PasswordField('Password', [validators.data_required(),
                                          validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('ok')

class LocationForm(Form):
    address = StringField('Address', [validators.Length(min=1, max=20)])
    zipcode = StringField('Zipcode', [validators.Length(min=1, max=20)])
    phonenumber = StringField('Phonenumber', [validators.Length(min=10, max=13)])
    submit = SubmitField('ok')