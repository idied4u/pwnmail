# pwnmail

A simple, private, and free encrypted email tool for real people. No surveillance. No lock-in. No paywalls.

# Requirements
python-gnupg
qrcode
rich
python-dotenv
Pillow
stepic

# Usage demo
Example:
$ sendsecure init
$ sendsecure send --to someone@example.com --subject 'Encrypted' --body 'Hello world'

# Features
- Full CLI (sendsecure)
- .env support
- Inbox watcher with ghost and self-destruct mode after a certain period of time (you can modify this)
- Fingerprint surveillance trap (get an alert if something pishy is going on in the event of MITM or tampering. First time imports are logged quietly.
- Stego attachments (hide/extract data from PNG's)
- Hardway key support (Yubikey) to check confirm when it's ready to use with decryption or signing. It will fail if no key is inserted, great for offlline use.
- generates a GPG keypair

# Disclaimer
- You are responsible for your own key safety and actions
- Meant for individuals that like to use custom tools instead of paying Corporations for "security".
- You should audit this code and edit it as you wish before using.
