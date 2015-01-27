class Conn():

    def __init__(self, host, user, passwd, command="help"):
        self.command = command
        self.host = host
        self.user = user
        self.passwd = passwd


    def runcmd(self):
        conn = paramiko.SSHClient()
        conn.set_missing_passwd_key_policy(paramiko.AutoAddPolicy())
        try:
            conn.connect(self.host,username=self.user,password=self.passwd)
        except paramiko.ssh_exception.AuthenticationException as err:
            print("Caught error: {0}".format(err))
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info()[:])
            exit(1)

        stderr, stdout, stdin = conn.exec_command(self.command)
        #print (stdout.readlines())
        for line in stdout.readlines():
            if line != string.whitespace:
                print(line)
        conn.close()