#!/bin/bash
# Installer script to globally symlink the sendsecure CLI

TARGET=/usr/local/bin/sendsecure
SOURCE="$(pwd)/scripts/sendsecure"

if [ ! -f "$SOURCE" ]; then
  echo "sendsecure script not found at $SOURCE"
  exit 1
fi

sudo ln -sf "$SOURCE" "$TARGET"
echo "✅ Pwnmail CLI installed globally as 'sendsecure'"
