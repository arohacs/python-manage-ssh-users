#!/usr/bin/env python

import subprocess
import sys
import argparse
from pprint import pprint
from fabric import Connection

parser = argparse.ArgumentParser()

# create user on specified host
# user connecting to host should have user management rights
userinfo=[]

parser.add_argument("username", help="enter the username for remote server")
parser.add_argument("password", help="enter user password")
parser.add_argument("pubkey_path", help="enter pubkey path")
parser.add_argument("shell", help="enter shell of remote user")
parser.add_argument("host", help="enter remote hostname or ip address")
args = parser.parse_args()

def create_user(username, password, shell):
    pass

def set_ssh_key(username, password, pubkey):
    pass

if __name__=='__main__':
    # print args -- debug
    print("starting...")
    print("username = ", args.username)
    print("password = ", args.password)
    print("pubkey path = ", args.pubkey_path)
    print("shell = ", args.shell)
    print("host = ", args.host)
    #hosts.append(args.host)
    # connect to ssh server and create user

    admin_user = 'jack'
    admin_password = 'cuc4il1n'
    #env.forward_agent = True
    #env.user = 'user'
    key_filename = ("/home/%s/.ssh/%s" % (args.username, args.pubkey_path))

    print (key_filename)
