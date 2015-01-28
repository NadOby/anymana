#!/usr/bin/env python
__author__ = 'evgeniy'

# import os
#import string
import conn
try:
    import paramiko
except ImportError:
    print("Paramiko python module is not found, please verify that it is installed.")
    exit(1)

#
# TODO move definitions to configuration file
# TODO Create class describing connection to host

hosts=["mews2206", "mews111", "mews046"]
usr="root"
pwd="passwd"

for h in hosts:
    c = conn.HPConnection(h, usr, pwd)
    c.power()
    c.power("status")
