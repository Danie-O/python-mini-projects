from email.message import EmailMessage
from password import PASSWORD
import ssl
import smtplib

""" STEPS:
    - go to gmail account and set up 2-factor authentication
    - generate app password (app= Python)
    - create a function to send email
"""

email_sender = 'daniellaomenogor@gmail.com'
email_password = PASSWORD

# generate temporary receiver email via temp-mail.org to test the email sender
email_receiver = ''
subject = 'A message from [Daniella]'
body = """
I just built an email sender with Python, visit my github to check it out!
Github repo link: https://github.com/Danie-O/python-mini-projects/tree/main/email-sender
"""

# define parameters for EmailMessage
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string)