while ! ping -c 1 -W 1 8.8.8.8; do
    echo "Waiting for 8.8.8.8 - network interface might be down..."
    sleep 1
done

IP=$(hostname -I)

echo $IP | cut -d' ' -f1 > ip_address.txt

#!/bin/sh
python ~/obtain_ip/sendip.py
