import os
import time
import sys
import string
import random

def domain_create(TLD_Domain):
    import string
    slist = list(string.ascii_lowercase)
    # add all numbers 0 through 9 to the list
    for number in range(10):
        text_num = str(number)
        slist.append(text_num)
    if TLD_Domain == '':
        TLD_Domain = 'us'
    domain_list = []
    index = 1
    for a in slist:
        for b in slist:
            for c in slist:
                d = a + b + c + "." + TLD_Domain
                #de = 'Null'
                #e = (d)
                domain_list.append(d)
                index += 1
    return(domain_list)

def digcheck(domain_name, TLD):
    '''
    #    This function returns zero if the domain does not exist or 256 if it does 
    #    or is run on a server that does not support NXDOMAIN
    '''
    fname = '{}_tld.txt'.format(TLD)
    shell_cmd = 'dig @8.8.8.8 {} | grep NXDOMAIN'.format(domain_name)
    d_check = os.system(shell_cmd)
    print("Check domain: {}".format(domain_name))
    if d_check == 0:
        output = '{} is available'.format(domain_name)
    else:
        output = '{} is taken'.format(domain_name)
    write_shell_cmd = 'echo {} >> {}'.format(output, fname)
    os.system(write_shell_cmd)
    pause = random.randint(1,60)
    print(pause)
    time.sleep(pause)
    return d_check

TLD_Domain = 'us'
domain_list = domain_create(TLD_Domain)
#print(domain_list, TLD_Domain)
for domain in domain_list:
    digcheck(domain, TLD_Domain)