try:
    import paramiko
except ImportError:
    print("Paramiko python module is not found, please verify that it is installed.")
    exit(1)
import sys

class Conn():

    def __init__(self, host, user, passwd, cmd="help"):
        self.cmd = cmd
        self.host = host
        self.user = user
        self.passwd = passwd


    def runcmd(self):
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            conn.connect(self.host,username=self.user,password=self.passwd)
        except paramiko.ssh_exception.AuthenticationException as err:
            print("Caught error: {0}".format(err))
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info()[:])
            exit(1)

        stderr, stdout, stdin = conn.exec_command(self.cmd)
        print (stdout.readlines())
        for line in stdout.readlines():
            if line != string.whitespace:
                print(line)
        conn.close()

class HPCmd ():
    def __init__(self):
        pass
