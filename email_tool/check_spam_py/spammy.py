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
import re

class bcolors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[41m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def get_users():
    check_user = re.compile('\W')
    users = os.listdir('/var/cpanel/users/')
    users.remove('system')
    valid_users = []
    for user in users:
        if check_user.search(user) == None:
            valid_users.append(user)            
    return valid_users
#
# Method takes list of users and returns list of email accounts
# by parsing the Json in email_accounts.json 
# Returns a dictionary of domain
#
def parse_cp_email(jsonFile):
    acct_map = {}
    domain_usr = json.load(jsonFile)
    for acct in domain_usr:
        if acct != "__version":
            type(domain_usr.get(acct).get('accounts').keys())
            acct_map[acct] = domain_usr.get(acct).get('accounts').keys()
        else:
            continue
    return acct_map        

def report_all_email(data):
    for user in data.keys():
        print(f'{bcolors.CYAN}The user {user} has: \n {bcolors.ENDC}')
        if data.get(user) == None:
            print(f'{bcolors.RED} No Email Account {bcolors.ENDC}')            
        else:
            for domain in data.get(user).keys():
                tmpData = data.get(user).get(domain)
                if tmpData == {}:
                    print(f'{bcolors.RED} {domain} has No Email Accounts')
                else:
                    print(f'{bcolors.YELLOW} \t {domain} has: \n {bcolors.ENDC}')
                    for each in tmpData:
                        print(f'{bcolors.GREEN} \t\t{each}@{domain} \n {bcolors.ENDC}')

# 
# Method parses email_accounts.json file for each user 
# and lists the email accounts per domain.
#
def get_email_accounts():
    data = {}
    users = get_users()
    for user in users:
         email_file = f'/home/{user}/.cpanel/email_accounts.json'
         if os.path.getsize(email_file) != 0:
            with open(email_file) as f:
                user_data = parse_cp_email(f)
                data[user] = user_data                
         else:
            data[user] = None
    report_all_email(data)
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
     parser.add_argument('-a','--all_email',action='store_true',
     help='This message shows the same information')
     parser.add_argument('-r','--email_routing', action='store_true', 
     help='prints the email routing for all domains')
     #parser.add_argument('--user', help='This will show all email for a email user')
     #parser.add_argument('--since', help='shows email totals from time frame provided until present')
     #parser.add_argument('--from', help='select emails with specific FROM values')
     args = parser.parse_args()
     return args

def main():
   args = generate_help()
   print (args)
   if args.all_email == True:
       get_email_accounts()
   if args.email_routing == True:
       get_email_routing()

if __name__ == "__main__":
    main()
