import datetime
import os
import re
import sys
import subprocess
import pyasn

yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
file_name = "netstat_data_relay_Zetservers_one_"+yesterday+".json"
ip_name = "netstat_data_relay_Zetservers_one_"+yesterday+".txt"

with open('somefile.txt', 'a') as the_file:
    the_file.write("gawk -F"'" "'" '{print $8 }' " + file_name + "| sort >"+ ip_name)

command1 = "gawk -F"'" "'" '{print $8 }' " + file_name + "| sort >" +ip_name

os.system(command1)

ip_name_formatted = "netstat_data_relay_Zetservers_one_"+yesterday+"_formatted.txt"


with open(ip_name, 'r') as f, open(ip_name_formatted, 'w') as n:
    for line in f:
        new_line = re.sub('[^a-zA-Z0-9_. ]+', ' ', line)
        n.write(new_line+'\n')


dns_records = "netstat_data_relay_Zetservers_one_"+yesterday+"_dns_records.txt"

with open(ip_name_formatted, 'r') as f, open(dns_records, 'w') as n:
    for line in f:
        #print line.strip()
        if line.strip() == "0.0.0.0":
            pass
        else:
            command2 = "dig -x " +line.strip()+" +short"
            # dns_result = os.system(command2)
            output = subprocess.check_output(command2, shell=True)
            # print output
            if output != "":
                n.write(output)
            # sys.exit()
        # n.write(new_line+'\n')

asn_records = "netstat_data_relay_Zetservers_one_"+yesterday+"_asn_records.txt"

with open(ip_name_formatted, 'r') as f, open(asn_records, 'w') as n:
    asndb = pyasn.pyasn('ipasn_20140513.dat')
    for line in f:
        #print line.strip()
        if line.strip() == "0.0.0.0":
            pass
        else:
            output = asndb.lookup(line.strip())
            # print output
            # print type(output)
            # print output[0]
            n.write(str(output[0])+'\n')
            # sys.exit()
        # n.write(new_line+'\n')
