#!/usr/bin/env python
__author__ = 'evgeniy'

# import os
#import string
#import conn
import conn_factory
try:
    import paramiko
except ImportError:
    print("Paramiko python module is not found, please verify that it is installed.")
    exit(1)

#
# TODO move definitions to configuration file
# TODO Create class describing connection to host
# TODO move to configuration options supported by IMM/IPMI/ILO etc
# TODO/MAYBE create query to query capabilities from IMM/
hosts=["qabl01-mgm", "qabl47-mgm"]
usr="root"
pwd="ipasdfas"

for h in hosts:
    c = conn_factory.make_connection(h, usr, pwd)
    c.power()
