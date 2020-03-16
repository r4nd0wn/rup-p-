# rup\(p\)

rup is an uptime checker which requests duckduckgo and sort the HTTP response codes to track the uptime of a server.
*only sorting http200 responses till now. lol.*


### requirements

Rup depends on python3 and uses the following standard libarys (usually no need to install it seperately):
* [datetime](https://docs.python.org/3/library/datetime.html) - to timestamp the logs
* [time](https://docs.python.org/3/library/time.html) - helps the script to fall asleep
* [sys](https://docs.python.org/3/library/sys.html) - to pass `rupp` arguments to the script

And also depends on:
* [requests](https://pypi.org/project/requests/) - http requests
Install it via:
```sh
$ pip install requests
```


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

### ToDo
* offer the opportunity to use different sleep duration between checking
* create cronjob for systemd haters
* check IPv4 and IPv6 abilitys seperately
* add the ability for `rupp` to check a specific time
* update rupp to ncurse 

### contribute
Feel free to fork and check my code :)

----
### License
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt)
