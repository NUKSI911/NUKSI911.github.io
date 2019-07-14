from flask_wtf import FlaskForm 
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from first_tutorial.models import User 
#  posts=[
# # 		{
# # 	'author': 'Simbi',
# # 	'title': 'Blog Post 1',
# # 	'content':'First post content',
# # 	'date_posted':'April 21,2018'
# 	},
# 		{
# 	'author': 'Rasheed',
# 	'title':'Blog Post 2',
# 	'content':'Second post content',
# 	'date_posted':'April 21,2019'
# 		}
# ]


class RegistrationForm(FlaskForm):
		"""Username form Creation"""
		username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
		email = StringField('Email',validators=[DataRequired(),Email()])
		password=PasswordField('Password',validators=[DataRequired()])
		confirm_password= PasswordField('Confirm Password ',validators=[DataRequired(),EqualTo('password')])
		submit=SubmitField('Sign Up')


		def validate_username(self,username):

			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('This username is taken.Please choose a different name')

		def validate_email(self,email):

			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('This Email is taken.Please choose a different name')

class LoginForm(FlaskForm):
		"""Login  form Creation"""
		email = StringField('Email',validators=[DataRequired(),Email()])
		password=PasswordField('Password',validators=[DataRequired()])
		remember =BooleanField('Remember Me')
		submit=SubmitField('Login')


class UpdateAccountForm(FlaskForm):
		"""Username form Creation"""
		username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
		email = StringField('Email',validators=[DataRequired(),Email()])
		picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
		submit=SubmitField('Update')


		def validate_username(self,username):
			if username.data != current_user.username:
				user=User.query.filter_by(username=username.data).first()
				if user:
					raise ValidationError('This username is taken.Please choose a different name')

		def validate_email(self,email):
			if email.data != current_user.email:
				user=User.query.filter_by(email=email.data).first()
				if user:
					raise ValidationError('This Email is taken.Please choose a different name')


class RequestResetForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	submit = SubmitField('Request Pasword Reset')

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with this email.Please register first')


class ResetPasswordForm(FlaskForm):
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password= PasswordField('Confirm Password ',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Reset Password')