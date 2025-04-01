# Pwnmail Hardware Key Detection (Yubikey / GPG Smartcard)

import subprocess

def check_smartcard():
    try:
        result = subprocess.run(["gpg", "--card-status"], capture_output=True, text=True)
        if "Reader ...........: " in result.stdout:
            print("✅ Smartcard detected and ready.")
            return True
        else:
            print("❌ No smartcard found.")
            return False
    except Exception as e:
        print(f"Error checking smartcard: {e}")
        return False

# Example usage
if __name__ == "__main__":
    check_smartcard()
