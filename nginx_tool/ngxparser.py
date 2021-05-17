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

    def __init__(self, acc_log, err_log, mode):
        pass

# input:
# output:
# description: This formats the arguments and provides simple way to produce
#              help menu output
#
def gen_help():
    parser = argparse.ArgumentParser(prog='Ngxparser', description ='Ngxparser helps analyze what Nginx is doing')

    parser.add_argument('-ip',action='store_true',
    help='Print requests made base on IP address')

    parser.add_argument('-h', action='store_true',
    help='Print results based on hourly rates')
    
    parser.add_argument('--since', action='store_true',
    help='Print results based on timedate object in format to match Nginx config')

def main():
    args = generate_help()
    print (args)
    switch (args) {
        case
    }
if __name__ == "__main__":
    main()
    
