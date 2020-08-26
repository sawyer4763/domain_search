import whois
import sqlite3
from sqlite3 import Error
import os
import time
import sys

#connect to the database
#conn = sqlite3.connect('domain_search.db')
#c = conn.cursor()



def NXDOMAIN_Server_check():
        # Need to add a check to see if name server support NXDOMAIN
    if os.system('dig @8.8.8.8 nonexistentrandombrokendomainzyx.com | grep NXDOMAIN') == 0:
        print("Domain Server is ok")
        pass
    else:
        print("Domain server does not support NXDOMAIN")
        sys.exit()

def digcheck(domain_name):
    '''
    This function returns zero if the domain does not exist or 256 if it does 
    or is run on a server that does not support NXDOMAIN
    '''

    shell_cmd = 'dig @8.8.8.8 {} | grep NXDOMAIN'.format(domain_name)
    d_check = os.system(shell_cmd)
    time.sleep(1)
    print("Check domain{}".format(domain_name))
    return d_check

def domain_create(working_database, conn, TLD_Domain):
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
                de = 'Null'
                e = (index, d, de)
                domain_list.append(e)
                index += 1
    #Create Database
    create_sql = "CREATE TABLE {} (id integer, domain text, domain_exists text)".format(working_database)
    c = conn.cursor()
    c.execute(create_sql)
    conn.commit()
    #Create pointer field


    #Inject into database



    return(domain_list)

#

#run through the database. and write to the database if the data coming back is valid.  
def create_connection(db_file):
    """
        This will create a connection to the database for random data
        documentation as outlined at: https://www.sqlitetutorial.net/sqlite-python/insert/
        and at https://docs.python.org/3.7/library/sqlite3
    """
    db_conn = None
    try: 
        db_conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return db_conn

def get_progress(db_conn, pointer_field):
    c = db_conn.cursor()

    sql_query = 'SELECT {} FROM miscdata WHERE _rowid_=1'.format(pointer_field)
    c.execute(sql_query)
    data = c.fetchone()
    return data[0]

'''
def get_domain_exp(domain):
    #Non functional function
    dlookup = whois.whois(domain)
    dlookup_string = str(dlookup["expiration_date"])
   tfile.write("Domain: " + domain + " expires on " + dlookup_string + "\n")

    if dlookup["expiration_date"] == "null":
        null_file.write(domain+"\n")
            if dlookup["expiration_date"] <= today:
                exp_list.write(domain+"\n")
    print("working on: " + domain)
    time.sleep(random.randint(1,60))
    return()
'''
def update_progress(conn, progress_id):
    c = db_conn.cursor()
    c.execute ("UPDATE miscdata SET progress = ?", progress_id)
    conn.commit()

def next_domain(conn, db_start_point):
    c = conn.cursor()
    t_data = str(db_start_point)
    c.execute('SELECT * FROM Domains WHERE ID= ?', t_data)
    data = c.fetchone()
    return data[1]

def data_insert(db_conn, progress_id):
    """
    This function will insert into the field after a scan is completed, 
    """
    
def db_check(working_database, db_conn):
    db_cursor = db_conn.cursor()
    sql_query = "SELECT name FROM sqlite_master where type = 'table' AND name={}".format(working_database)
    dbe = db_cursor.execute(sql_query)
    return dbe

# db_connection = create_connection(domain_search.db)


# Main Pogram

#check if dig works with NXDOMAIN
#NXDOMAIN_Server_check()


#Main Variables and working bits
TLD = 'us'
db_file = '/home/ssawyer/Documents/PyTests/domain_search/domain_search.db'
pointer_field = 'pointer_field_{}'.format(TLD)
working_database = '{}_domain'.format(TLD)


#Open connection to Database
db_conn = create_connection('/home/ssawyer/Documents/PyTests/domain_search/domain_search.db')
#Check if table exists for TLD
dbe = db_check(working_database, db_conn)
if dbe == None:
    domain_create(working_database, db_conn, TLD)



#Check progress of the database in case of previous failure / timeout by reading miscdata table and progress record
db_start_point = get_progress(db_conn)
domain_to_scan = next_domain(db_conn, db_start_point)
domain_existance = digcheck(domain_to_scan)
if domain_existance == 0:
    db_pointer = db_conn.cursor()
    db_pointer.execute('UPDATE ')







'''
dig_eval = digcheck('flagtagaz.com')
if dig_eval == 0:
    # This function needs to write the result into the database into the field dig_result
    # dig result = 0 means available, dig result = 1 means not available
    pass
'''

#if __name__ == '__main__':
#    sys.exit(main(sys.argv))