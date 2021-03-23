#import AK_retrieve_creds

import keyring
from cryptography.fernet import Fernet
import yagmail
import os

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

    sender_email = ak_mail_user()
    receiver_email = "satishmurthy2015@gmail.com"
    mail_subject = "Akademize - Certificate"
    body = [
    "Hello. Please find attached the certificate for the course you completed with AKADEMIZE.\n"
    "Hope you have found the course useful.\n"
    "Please send us your feedback as what we can do to improve the course.\n"
    "Please reach out to us for any queries on the course or any other training needs you may have.\n"
    "Good luck.\n"
    "- Team AKADEMIZE"
]

    yag = yagmail.SMTP(sender_email, ak_mail_pwd())
    yag.send(
        to = receiver_email,
        subject=mail_subject,
        contents=body,
        bcc=sender_email,
        attachments=samplefile
    )

main()