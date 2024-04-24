from django.core.mail import EmailMessage
import random
import string

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
    
    @staticmethod
    def generate_random_password():
        # Generate a random password using uppercase letters, lowercase letters, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=12))  # Generate a 12-character password
        return password
