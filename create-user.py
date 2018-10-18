#!/usr/bin/env python

import subprocess
import sys
import argparse

parser = argparse.ArgumentParser()

# xargs for input
# user info
# public ssh key
# host info

# create user on specified host
# user connecting to host should have user management rights
userinfo=[]

parser.add_argument("username", help="enter the username for remote server")
parser.add_argument("password", help="enter user password")
parser.add_argument("pubkey_path", help="enter pubkey path")
parser.add_argument("shell", help="enter shell of remote user")
parser.add_argument("host", help="enter remote hostname or ip address")
args = parser.parse_args()

if __name__=='__main__':
    # print args -- debug
    print("starting...")
    print("username = ", args.username)
    print("password = ", args.password)
    print("pubkey path = ", args.pubkey_path)
    print("shell = ", args.shell)
    print("host = ", args.host)

    # connect to ssh server and create user

