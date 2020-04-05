#!/bin/bash

echo ">>> Installing Mailhog"

# Download binary from github
wget --quiet -O /tmp/mailhog https://github.com/mailhog/MailHog/releases/download/v1.0.0/MailHog_linux_amd64

# Move binary to /opt
sudo mv /tmp/mailhog /opt/mailhog

# Make it executable
chmod +x /opt/mailhog

# Make it start on reboot
sudo tee /etc/systemd/system/mailhog.service <<EOL
[Unit]
Description=MailHog Service
After=network.service vagrant.mount

[Service]
Type=simple
ExecStart=/usr/bin/env /opt/mailhog > /dev/null 2>&1 &

[Install]
WantedBy=multi-user.target
EOL

# Start on reboot
sudo systemctl enable mailhog

# Start background service now
sudo systemctl start mailhog

# Adapted from: https://gist.github.com/varghesejacob/c31a844042ca5ced6b72ccab3cd6055b

# 2020.04.01-DEA
