#import AK_retrieve_creds

import keyring
from cryptography.fernet import Fernet
import email, smtplib, ssl
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

service_id = 'AKADEMIZE'
vault_key = keyring.get_password(service_id, 'Cipher_Key')
vault_suite = Fernet(vault_key.encode())

def ak_mail_user():
    return vault_suite.decrypt((keyring.get_password(service_id, 'AK_User')).encode()).decode('utf-8')

def ak_mail_pwd():
    return vault_suite.decrypt((keyring.get_password(service_id, 'AK_Pwd')).encode()).decode('utf-8')

def main():
    if 'CERTDIR' not in os.environ:
        os.environ['CERTDIR'] = "C:\\Users\\Satish\\Documents\\Python Scripts\\Akademize Certificates"
    certdir = os.environ['CERTDIR']

    samplecert='Sample-ABC123456.pdf'
    samplefile = fr'{certdir}\\{samplecert}'

    port = 465  # For SSL
    context = ssl.create_default_context()
    sender_email = ak_mail_user()
    receiver_email = "satishmurthy2015@gmail.com"
    subject = "Akademize - Certificate"
    body = "This is an email with attachment sent from Python"

    '''
    message = """\
    Subject: Test mail from Python

    This message is sent from Python."""
    '''

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(samplefile, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {samplecert}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, ak_mail_pwd())
        server.sendmail(sender_email, receiver_email, text)

main()