# While ping google.com doesnt work, sleep for 1 second
# ping -c 1 = ping once
# ping -W 1 = timeout 1s
while ! ping -c 1 -W 1 8.8.8.8; do
    echo "Waiting for 8.8.8.8 - network interface might be down..."
    sleep 1
done

# Obtain ip address and assign to IP variable
IP=$(hostname -I)

# Split the IP variable by spaces, and write the first section to text file
echo $IP | cut -d' ' -f1 > ip_address.txt

# Run python script to send the ip address via telebot

#!/bin/sh
python ~/obtain_ip/sendip.py
