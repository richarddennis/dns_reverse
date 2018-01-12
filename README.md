# dns_reverse
lookup dns


CHANGE VARIABLE NAME OF SERVER




```sh

apt-get install python-pip 

apt-get install python-dev   # for python2.x installs

apt-get install dnsutils

pip install pyasn --pre

pyasn_util_download.py --latest

pyasn_util_convert.py --single rib.20180110.1600.bz2 ipasn_20140513.dat

git clone https://github.com/richarddennis/dns_reverse.git

chmod +x /root/dns_reverse/dns_reverse.py

crontab -e
1 0 * * * python /root/dns_reverse/dns_reverse.py
```
