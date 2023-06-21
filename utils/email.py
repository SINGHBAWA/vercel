from flask_mail import Mail, Message
import os
from flask import render_template

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USERNAME": "amansinghbawa@gmail.com",
    "MAIL_PASSWORD": "<>"
}


class EmailService:
    def __init__(self, app):
        self.app = app
        app.config.update(mail_settings)
        self.mail = Mail(app)

    def send_mail(self, recipient, name, message):
        msg = Message(subject=f"Query from {recipient}",
                      sender=self.app.config.get("MAIL_USERNAME"),
                      recipients=[self.app.config.get("MAIL_USERNAME"), ],  # replace with your email for testing
                      body=message)
        self.mail.send(msg)

        msg = Message(subject="Baba iron and cement store - Query submitted",
                      sender=self.app.config.get("MAIL_USERNAME"),
                      recipients=[recipient, ]  # replace with your email for testing
                      # body=f"Hi,\nYour query is submitted we will contact you soon\n\nDetails:\n{message}\n\nThank you,\nBaba Iron and cement store\n"
                    )
        msg.html = render_template("mail/contact_us_customer.html", **{"name": name,"message": message})
        self.mail.send(msg)
