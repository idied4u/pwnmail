# Pwnmail Ghost Inbox Watcher with Self-Destruct Mode

import time
import os
import email
from email import policy
from email.parser import BytesParser
from core import decrypt_message
import tempfile

MAILBOX_DIR = os.path.expanduser("~/Maildir/new")  # Adjust if needed
SELF_DESTRUCT_DELAY = 10  # Seconds to keep the message before wiping

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ghost_display(message: str):
    try:
        print(f"🕵️ Showing decrypted message (auto-wipes in {SELF_DESTRUCT_DELAY}s)...")
        print("="*60)
        print(message)
        print("="*60)
        time.sleep(SELF_DESTRUCT_DELAY)
        clear_terminal()
        print("🧨 Message self-destructed.")
    except Exception as e:
        print(f"Error during ghost display: {e}")

def watch_mailbox():
    print("📬 Ghost Inbox is watching for new encrypted messages...")
    seen = set()

    while True:
        try:
            files = os.listdir(MAILBOX_DIR)
            for file in files:
                filepath = os.path.join(MAILBOX_DIR, file)
                if filepath not in seen and filepath.endswith(".eml"):
                    with open(filepath, "rb") as f:
                        msg = BytesParser(policy=policy.default).parse(f)
                        body = msg.get_body(preferencelist=('plain')).get_content()
                        if "-----BEGIN PGP MESSAGE-----" in body:
                            print(f"🔓 Encrypted message detected: {file}")
                            decrypted = decrypt_message(body)
                            if decrypted.ok:
                                ghost_display(str(decrypted))
                                os.remove(filepath)  # Delete original message
                                seen.add(filepath)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    watch_mailbox()
