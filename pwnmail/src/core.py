
import gnupg
import os

from dotenv import load_dotenv

load_dotenv()  # Load SMTP config from .env


# Set up GPG home
GPG_HOME = os.path.expanduser("~/.sendsecure_gpg")
os.makedirs(GPG_HOME, exist_ok=True)
gpg = gnupg.GPG(gnupghome=GPG_HOME)

def init_key(name_email: str, passphrase: str):
    """
    Generate a GPG key pair.
    """
    input_data = gpg.gen_key_input(
        name_email=name_email,
        passphrase=passphrase,
        key_type="RSA",
        key_length=2048
    )
    key = gpg.gen_key(input_data)
    return key

def export_public_key(fingerprint: str):
    """
    Export the public key for sharing.
    """
    return gpg.export_keys(fingerprint)

def import_public_key(armored_key: str):
    """
    Import a public key.
    """
    return gpg.import_keys(armored_key)

def encrypt_message(message: str, recipient_email: str):
    """
    Encrypt a message to a recipient.
    """
    encrypted_data = gpg.encrypt(message, recipients=[recipient_email])
    return str(encrypted_data)

def decrypt_message(encrypted_message: str):
    """
    Decrypt a given message.
    """
    return gpg.decrypt(encrypted_message)


import smtplib
from email.message import EmailMessage

def send_encrypted_email(smtp_server, smtp_port, smtp_user, smtp_password, to_email, subject, encrypted_body):
    """
    Send an encrypted email using SMTP.
    """
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg.set_content(encrypted_body)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
