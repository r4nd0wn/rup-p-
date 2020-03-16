#! /bin/bash
mkdir /var/log/rup
touch /var/log/rup/rup.log
chmod -R 775 /var/log/rup/
cp main.py /usr/bin/rup
chmod +x /usr/bin/rup
cp parser.py /usr/bin/rupp
chmod +x /usr/bin/rupp
cp rup.service /etc/systemd/system/
touch /var/log/rup/rup.log
systemctl enable rup
echo finished

