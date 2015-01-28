try:
    import paramiko
except ImportError:
    print("Paramiko python module is not found, please verify that it is installed.")
    exit(1)
import sys

class AbstractConnection(object):

    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def get_power_command(self, disposition):
        raise NotImplemented()

    def power(self, disposition = None):
        if disposition:
            cmd = self.get_power_command(disposition)
        else:
            cmd = self.get_power_command("status")

        self.runcmd(cmd)

    def reset(self, soft = True):
        raise NotImplemented()

    def runcmd(self, cmd):
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

        stderr, stdout, stdin = conn.exec_command(cmd)
        print (stdout.readlines())
        for line in stdout.readlines():
            if line != string.whitespace:
                print(line)
        conn.close()

class HPConnection(AbstractConnection):
    POWER_CMD = { 
                  "on":     "power on",
                  "off":    "power on",
                  "status": "power"
    }
        
    def __init__(self, host, user, passwd):
        super(HPCmd, self).__init__(host, user, passwd)

    def get_power_command(self, disposition):
        return POWER_CMD[disposition]


