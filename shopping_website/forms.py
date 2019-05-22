from wtforms import Form, PasswordField, validators, StringField, SubmitField, TextAreaField, FileField, BooleanField, SelectField
from flask_wtf.file import FileAllowed, FileRequired

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
    title = TextAreaField('Title', [validators.data_required(), validators.Length(min=1, max=20)])
    content = TextAreaField('Content', [validators.data_required(), validators.Length(min=1, max=50)])
    password = PasswordField('Password', [validators.data_required(),
                                          validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('ok')

class LocationForm(Form):
    address = StringField('Address', [validators.Length(min=1, max=20)])
    zipcode = StringField('Zipcode', [validators.Length(min=1, max=20)])
    phonenumber = StringField('Phonenumber', [validators.Length(min=10, max=13)])
    submit = SubmitField('ok')

class ProductForm(Form):
    product_name = TextAreaField('Product Name', [validators.Length(min=1, max=20)])
    product_tag = SelectField('Product Tag', choices=[('1','여성패션'), ('2','남성패션'), ('3','뷰티'), ('4','식품'), ('5','주방용품'), ('6','생활용품'), ('7','홈인테리어'), ('8','가전디지털'), ('9','자동차'), ('10','완구취미'), ('11','문구'), ('12','도서') ])
    product_intro = TextAreaField('Product Intro', [validators.Length(min=1, max=50)])
    product_pic = FileField('Product picture', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('okay')

class Delete_Form(Form):
    accept = BooleanField('I agree to delete this.', [validators.data_required()])
    submit1 = SubmitField('삭제')

class Submit_Form(Form):
    submit = SubmitField('Okay')

class Location_track_Form(Form):
    submit = SubmitField('배송조회')

