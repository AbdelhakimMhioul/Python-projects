# Import from env file
import os
import smtplib
import ssl
from email.message import EmailMessage

# Generate application password
print(os.getenv('EMAIL_PASSWORD'))
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

EMAIL_RECEIVER = "hk.mhl1975@gmail.com"

SUBJECT = "Do not forget to drink water"
BODY = """
When you drink water, you are not only hydrating your body, you are also hydrating your brain.
"""

# Send the email
em = EmailMessage()
em['From'] = EMAIL_SENDER
em['To'] = EMAIL_RECEIVER
em['Subject'] = SUBJECT
em.set_content(BODY)

context = ssl.create_default_context()

# Send multiple emails
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())
