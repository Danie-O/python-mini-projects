""" STEPS:
    - go over to gmail account and set up 2-factor authentication
    - generate app password
    - create a function to send email
"""
from email.message import EmailMessage
from password import PASSWORD

email_sender = 'daniellaomenogor@gmail.com'
email_password = PASSWORD

email_receiver = ''
subject = 'A message from [Daniella]'
body = """
I just built an email sender with Python, visit my github to check it out!
Github repo link: 
"""

# define parameters for EmailMessage
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)
