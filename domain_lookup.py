import string
import whois
import time
import datetime
import random
from dns import resolver
import os

# list of letters [a-z]
a_list = list(string.ascii_lowercase)

# Get today's date to compare to expiration dates
today = datetime.datetime.now()

#The top level domain to evaluate
TLD =".us"
# Create a file to capture all output
tfile = open("domain" + TLD+".txt","w+") 
# create a file to capture all null (available domains)
null_file = open("null_output"+TLD+".txt","w+")
#create a file to capture all expired domains
#exp_list = open("expired_output"+TLD+".txt","w+")

#list of numbers zero through nine to search for domains 111 through 999
n_list = [0,1,2,3,4,5,6,7,8,9]

res = resolver.Resolver()
res.nameservers = ['8.8.8.8', '192.168.1.1']
for a in a_list:
    for b in a_list:
        for c in a_list:
            domain = a + b + c + TLD
#   DNS lookup method
#            try:
#                dip = res.resolve(domain)
#                for ip in dip:
#                    tfile(domain + ":" + ip.address + "\n")
#            except Exception:
#                tfile(domain + ":" + "No_IP\n")
# Whois section
            dlookup = whois.whois(domain)
            dlookup_string = str(dlookup["expiration_date"])
            tfile.write("Domain: " + domain + " expires on " + dlookup_string + "\n")
            if dlookup["expiration_date"] == "null":
                null_file.write(domain+"\n")
#            if dlookup["expiration_date"] <= today:
#                exp_list.write(domain+"\n")
            print("working on: " + domain)
            time.sleep(random.randint(1,60))

#for a in n_list:
#    for b in n_list:
#        for c in n_list:
#            domain = a + b + c + TLD
#            dlookup = whois.whois(domain)
#            dlookup_string = str(dlookup["expiration_date"])
#            tfile.write("Domain: " + domain + " expires on " + dlookup_string + "\n")
#            if dlookup["expiration_date"] == "null":
#                null_file.write(domain+" \n")
#                print("domain " + domain + "is not registered")
#            if dlookup["expiration_date"] <= today:
#                exp_list.write(domain+ "\n")
#                print("domain " + domain + "is expired")
#            print("working on: " + domain + " which expires on: " + dlookup_string)
#            time.sleep(random.randint(1,60))

tfile.close()
null_file.close()
#exp_list.close()
