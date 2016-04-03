import string
import sys

try:
    import paramiko
except ImportError:
    print("Paramiko python module is not found, please verify that it is installed.")
    exit(1)


class AbstractConnection(object):
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def get_power_command(self, disposition):
        raise NotImplemented()

    def power(self, disposition=None):
        if disposition:
            cmd = self.get_power_command(disposition)
        else:
            cmd = self.get_power_command("status")

        self.runcmd(cmd)

    def reset(self, soft=True):
        raise NotImplemented()

    def runcmd(self, cmd):
        print(cmd)
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            conn.connect(self.host, username=self.user, password=self.passwd, timeout=10)
        except paramiko.ssh_exception.AuthenticationException as err:
            print("Caught error: {0}".format(err))
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info()[:])
            exit(1)

        stderr, stdout, stdin = conn.exec_command(cmd)
        print(stdout.read())
        for line in stdout.readlines():
            if line != string.whitespace:
                print(line)
        conn.close()


class HPConnection(AbstractConnection):
    POWER_CMD = {
        "on":       "power on",
        "off":      "power off",
        "status":   "power",
        "reset":    "power reset",
        "reboot":   "power warm"
    }

    def __init__(self, host, user, passwd):
        super(HPConnection, self).__init__(host, user, passwd)

    def get_power_command(self, disposition):
        return HPConnection.POWER_CMD[disposition]

    def reset(self, soft=True):
        if soft:
            return self.runcmd("reboot")
        else:
            return self.power("reset")


class DellConnection(AbstractConnection):
    POWER_CMD = {
        "on":       "racadm serveraction poweron",
        "off":      "racadm serveraction powerdown",
        "status":   "racadm serveraction powercatatus",
        "reset":    "racadm serveraction hardreset ",
        "reboot":   "racadm serveraction powercycle"
    }

    def __init__(self, host, user, passwd):
        super(DellConnection, self).__init__(host, user, passwd)

    def get_power_command(self, disposition):
        return DellConnection.POWER_CMD[disposition]

    def reset(self, soft=True):
        if soft:
            return self.runcmd("reboot")
        else:
            return self.power("reset")


class IBMConnection(AbstractConnection):
    POWER_CMD = {
        "on":       "power -on",
        "off":      "power -off",
        "status":   "power -state",
        "reset":    "power -cycle",
        "reboot":   "power -cycle"
    }

    def __init__(self, host, user, passwd):
        super(IBMConnection, self).__init__(host, user, passwd)

    def get_power_command(self, disposition):
        return IBMConnection.POWER_CMD[disposition]

    def reset(self, soft=True):
        if soft:
            return self.runcmd("reboot")
        else:
            return self.power("reset")
