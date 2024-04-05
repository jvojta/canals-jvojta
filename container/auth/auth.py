from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

user = auth.get_user('ZLUZIeJCg7ZaH14KUgIgEj3byFZ2')
print('Successfully fetched user data: {0}'.format(user.uid))
"""
user = auth.create_user(
    email='user@example.com',
    email_verified=False,
    phone_number='+15555550100',
    password='secretPassword',
    display_name='John Doe',
    photo_url='http://www.example.com/12345678/photo.png',
    disabled=False)
print('Sucessfully created new user: {0}'.format(user.uid))
"""

auth.generate_email_verification_link('jvojta2005@gmail.com')

email = 'jvojta2005@gmail.com'
link = auth.generate_password_reset_link(email)
# Construct password reset email from a template embedding the link, and send
# using a custom SMTP server.
auth.
send_custom_email(email, link)