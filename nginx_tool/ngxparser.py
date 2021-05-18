#! /opt/imh-python/bin/python3.7
# -*- coding: utf-8 -*-

# Ngxparser is a tool for generating reports based
# on nginx access logs and error logs.
# This program is written for RHEL 7/centos 7

import sys
import re
import os
import argparse
import logging

# description: This is a simple classes that defines all the basic colors
#              for bash terminal text highlighting. There is also the
#              special character (ENDC) that ends the usage of the current color
#              and returns to the default settings. This contains the basic color
#              options and can be added to easily.
#
#
class Bcolors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[41m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

# input:
# output:
# description:
#
#
class Ngxparser:

    def __init__(self, mode, acc_log='/var/log/nginx/access.log', err_log='/var/log/nginx/error_log'):
        self.acc_log=acc_log
        self.err_log=err_log

    def get_ip_count(self):
        pass
    
    # input: single line from nginx access log
    # output: list of field values 
    # description: This method seperates the log file line into distinct values
    # that are used in analysis reports later
    def split_field_values(self, data):

        valid_http_methods = ["GET","HEAD","POST","PUT","PATCH","DELETE","CONNECT","OPTIONS","TRACE"]

        temp_field_values = data.split('\"')
        ip_time_values = field_values[0].split()
        request_value = field_values[1]
        
        for each in valid_http_methods:
            if each in field_value[1]:


        print (f"IP = {ip_time_values[0]}")
        print (f"Request = {field_values[1]}",'\n')
        return 
        print (f"date = {field_values[3]}")
        print (f"request = {field_values[6]}")
        print (f"response_code = {field_values[8]}")
        print (f"domain = {field_values[27]}")
        return field_values

    def parse_acc_file(self):
        try:
            with open(self.acc_log) as f:
                for line in f:
                    #print (line)
                    self.split_field_values(line)
        except IOError:
            print (f'There is no file named {self.acc_log}')


# input:
# output:
# description: This formats the arguments and provides simple way to produce
#              help menu output
#
def gen_help():
    parser = argparse.ArgumentParser(prog='Ngxparser', description ='Ngxparser helps analyze what Nginx is doing')
    
    parser.add_argument('-ip',action='store_true',
    help='Print requests made base on IP address')

    parser.add_argument('--hour', action='store_true',
    help='Print results based on hourly rates')
    
    parser.add_argument('--since', action='store_true',
    help='Print results based on timedate object in format to match Nginx config')

    parser.add_argument('--access-log', action='store_true',
    help='overide the default location for Nginx access log')

    parser.add_argument('--error-log', action='store_true',
    help='overide the default location for the Nginx error log')

    parser.add_argument('-o','--output', action='store_true',
    help='set a file for output of results instead of std out')
    
    args = parser.parse_args()
    return args

def main():
    args = gen_help()
    print (args)
    testing = Ngxparser(0)
    testing.parse_acc_file()

if __name__ == "__main__":
    main()    
