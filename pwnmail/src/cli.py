
import argparse
from core import init_key, export_public_key, import_public_key, encrypt_message, decrypt_message

def main():
    parser = argparse.ArgumentParser(description="Encrypted Email for Humans CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Init command
    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--email", required=True)
    init_parser.add_argument("--passphrase", required=True)

    # Export public key
    export_parser = subparsers.add_parser("export-key")
    export_parser.add_argument("--fingerprint", required=True)

    # Import public key
    import_parser = subparsers.add_parser("import-key")
    import_parser.add_argument("--key", required=True)

    # Encrypt message
    encrypt_parser = subparsers.add_parser("encrypt")
    encrypt_parser.add_argument("--to", required=True)
    encrypt_parser.add_argument("--message", required=True)

    # Decrypt message
    decrypt_parser = subparsers.add_parser("decrypt")
    decrypt_parser.add_argument("--message", required=True)

    args = parser.parse_args()

    if args.command == "init":
        key = init_key(args.email, args.passphrase)
        print(f"Generated key: {key}")

    elif args.command == "export-key":
        pubkey = export_public_key(args.fingerprint)
        print(pubkey)

    elif args.command == "import-key":
        result = import_public_key(args.key)
        print(f"Imported key(s): {result.fingerprints}")

    elif args.command == "encrypt":
        encrypted = encrypt_message(args.message, args.to)
        print(encrypted)

    elif args.command == "decrypt":
        decrypted = decrypt_message(args.message)
        print(decrypted)

if __name__ == "__main__":
    main()


    # Send encrypted email via SMTP
    elif args.command == "send-smtp":
        from getpass import getpass
        smtp_user = input("SMTP Username: ")
        smtp_pass = getpass("SMTP Password: ")
        smtp_server = input("SMTP Server (e.g. smtp.gmail.com): ")
        smtp_port = int(input("SMTP Port (usually 465 for SSL): "))
        to_email = input("Recipient Email: ")
        subject = input("Email Subject: ")
        message = input("Message to Encrypt and Send: ")

        encrypted = encrypt_message(message, to_email)
        send_encrypted_email(smtp_server, smtp_port, smtp_user, smtp_pass, to_email, subject, encrypted)
        print("Encrypted email sent successfully.")
