from conn import *

HOST_MAPPING = {
        "qabl01-mgm"    :HPConnection,
        "qabl47-mgm"    :DellConnection,

        #...

        }

#locals().get("HPConnection", None)

def make_connection(host, usr):
    pwd = get_password_for_host(host)
    return HOST_MAPPING[host](host, usr, pwd)

def get_all_by_hw(hw):
    pass

def get_all_by_location(location):
    pass

def get_all_by_role(role):
    pass # e.g. desktops, blades, etc.

