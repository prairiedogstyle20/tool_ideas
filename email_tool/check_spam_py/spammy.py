#! /bin/python3

#Spammy is a simple python script to get relevant information about email 
# Note: There are two operational modes
# - get all mail dir sizes
# - get email connection settings from each server
# - get 
import argparse
import os

class bcolors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[41m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

def get_users():
    users = os.listdir('/var/cpanel/users/')
    return users

def get_email_accounts():
    users = get_users()
    for each in users:
         if each != "system":
            e_domains_usr = os.listdir(f'/home/{each}/mail/')
            print (e_domains_usr)
# 
# Method prints the contents of config files for email routing
#
#
#
def get_email_routing():
    remote_domains = '/etc/remotedomains'
    local_domains = '/etc/localdomains'

    print (bcolors.CYAN + "Remote Domanins: \n" + bcolors.ENDC)
    with open(remote_domains) as f:
        if os.path.getsize(remote_domains) == 0:
            print(f"{bcolors.RED} NO Remote Domains{bcolors.ENDC} \n")
        else:
            for domain in f:
                print(f"{bcolors.GREEN}{domain}{bcolors.ENDC}")
    f.close()
    
    print (bcolors.CYAN + "Local Domains: \n" + bcolors.ENDC)
    with open(local_domains) as g:
        for domain in g:
            print(f"{bcolors.GREEN}{domain}{bcolors.ENDC}")
    g.close()

def generate_help():
     parser = argparse.ArgumentParser(prog='Spammy',description='Spammy is the spam assasin we deserve')
     parser.add_argument('-a', help='This message shows the same information')
     parser.add_argument('--check_routing', help='prints the email routing for all domains')
     parser.add_argument('--user', help='This will show all email for a email user')
     parser.add_argument('--since', help='shows email totals from time frame provided until present')
     parser.add_argument('--from', help='select emails with specific FROM values')
     args = parser.parse_args()
     return args

def main():
   args = generate_help()
   print (args)
   if args.a == "5":
       get_email_accounts()
   if args.check_routing == "1":
       get_email_routing()

if __name__ == "__main__":
    main()
