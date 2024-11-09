from flask_mail import Message, Mail
from flask import current_app

mail = Mail()

def send_email(subject, recipients, body):
    msg = Message(
        subject=subject,
        recipients=recipients,
        body=body,
        sender=current_app.config['MAIL_USERNAME']
    )
    mail.send(msg)

def send_password_reset_email(user, token):
    reset_url = f"{current_app.config['FRONTEND_URL']}/reset-password/{token}"
    subject = "Password Reset Request"
    body = f"Hello {user.username},\n\nClick the link below to reset your password:\n{reset_url}\n\nIf you did not request this, please ignore this email."
    send_email(subject, [user.email], body)