#! /bin/python3

#Spammy is a simple python script to get relevant information about email 
# Note: There are two operational modes
# - get all mail dir sizes
# - get email connection settings from each server
# - get 
import argparse
import json
import os
import logging

class bcolors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[41m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def get_users():
    users = os.listdir('/var/cpanel/users/')
    users.remove('system')
    return users

#  
# Method parses email_accounts.json file for each user 
# and lists the email accounts per domain.
#
def get_email_accounts():
    users = get_users()
    for user in users:
         email_file = f'/home/{user}/.cpanel/email_accounts.json'
         if os.path.getsize(email_file) != 0:
            with open(email_file) as f:
                try:
                    print(f'{bcolors.CYAN}The user {user} has:{bcolors.ENDC}')
                    e_domains_usr = json.load(f)
                    for acct  in e_domains_usr:
                        if acct != "__version":
                            e_data = e_domains_usr.get(acct)
                            if e_data.get('account_count') == 0:
                                print (f"{bcolors.RED} Domain {acct} has no email accounts{bcolors.ENDC} \n")
                            else:
                                print (f"\t{bcolors.YELLOW} Domain {acct} has: \n {bcolors.ENDC}")
                                for each in e_data.get("accounts"):
                                    print (f'\t\t{bcolors.GREEN}{each}@{acct} \n {bcolors.ENDC}')
                        else:
                            pass
                        #print(f'{bcolors.GREEN}{acct}{bcolors.ENDC}')
                    #print (json.dumps(e_domains_usr, indent=4, sort_keys=True))
                except Exception as e:
                    print (e)
         else:
            print(f'''{bcolors.CYAN}The user {user} has: \n  
            {bcolors.ENDC} {bcolors.RED} No Email Account {bcolors.ENDC}''')            
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

def general_exim_parser():
    exim_log = '/var/log/exim_main_log'

    with open(exim_log) as f:
        for each in f:
            pass
    f.close()

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
