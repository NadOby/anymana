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
hosts=["chassis-hp.me-corp.lan", "chassis-dell1.me-corp.lan"]
user="root"
passwd="password"
for host in hosts:
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        conn.connect(host,username=user,password=passwd)
    except paramiko.ssh_exception.AuthenticationException as err:
        print("Caught error: {0}".format(err))
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[:])
        exit(1)

    stderr, stdout, stdin = conn.exec_command("help")
    #print (stdout.readlines())
    for line in stdout.readlines():
        if line != string.whitespace:
            print(line)
    conn.close()
