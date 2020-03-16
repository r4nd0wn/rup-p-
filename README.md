# rup\(p\)

rup is a uptime checker which requests duckduckgo and sort the HTTP response codes to track the uptime of a server.



### requirements

Rup depends on python3 and uses the following standard libarys (usually no need to install it seperately):
* [requests](https://pypi.org/project/requests/) - http requests
* [datetime](https://docs.python.org/3/library/datetime.html) - to timestamp the logs
* [time](https://docs.python.org/3/library/time.html) - helps the script to fall asleep


### Installation
make sure python3 is installed and run the following commands:
```sh
$ git clone https://github.com/r4nd0wn/rup-p-
$ cd rup-p-
$ chmod +x install.sh
$ sudo ./install.sh
```
to enable the systemd unit (recommended):
```
$ systemctl enable rup
```

### rupp
To check the uptime, use rupp:
```
$ rupp --help
```

### contribute
Feel free to fork and check my code :)

----
### License
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt)
