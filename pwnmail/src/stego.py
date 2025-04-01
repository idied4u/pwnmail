# Pwnmail Stego Attachments (Hide/Extract encrypted messages in PNG images)

from PIL import Image
import stepic
import sys
import os

def hide_message_in_image(input_image_path, message, output_image_path):
    img = Image.open(input_image_path)
    steg_img = stepic.encode(img, message.encode('utf-8'))
    steg_img.save(output_image_path, 'PNG')
    print(f"✅ Message hidden in {output_image_path}")

def extract_message_from_image(image_path):
    img = Image.open(image_path)
    message = stepic.decode(img)
    print("🕵️ Hidden message extracted:")
    print("="*50)
    print(message)
    print("="*50)
    return message

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  To hide:    python stego.py hide input.png 'your secret' output.png")
        print("  To extract: python stego.py extract input.png")
        sys.exit(1)

    action = sys.argv[1]
    if action == "hide" and len(sys.argv) == 5:
        _, _, input_img, secret_msg, output_img = sys.argv
        hide_message_in_image(input_img, secret_msg, output_img)
    elif action == "extract" and len(sys.argv) == 3:
        _, _, input_img = sys.argv
        extract_message_from_image(input_img)
    else:
        print("Invalid usage.")
