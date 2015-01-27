__author__ = 'evgeniy'

# import os
import sys
import string
try:
    import paramiko
except ImportError:
    print("Paramiko python module is not found, please verify that it is installed.")
    exit(1)

#
# TODO move global definitions to configuration file
#

# TODO Create class describing connection to host
hosts=["chassis-hp.me-corp.lan", "chassis-dell1.me-corp.lan"]
user="root"
passwd="password"

for host in hosts:

