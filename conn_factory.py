from conn import *
import re

HOST_MAPPING = {
        "qabl01-mgm"    :HPConnection,
        "qabl47-mgm"    :DellConnection,
        }

#locals().get("HPConnection", None)

def regexp(pref, lo, hi, postf=''):
    fmt = '%%0%dd' % 2
    return re.compile(r'\b{0:s}({1:s}){2:s}\b'.format(pref, '|'.join(fmt % i for i in range(lo, hi + 1)), postf))

def make_connection(host, usr, passwd):
    # FIXME passwd = get_password_for_host(host)
    return HOST_MAPPING[host](host, usr, passwd)

def get_all_by_hw(hw):
    pass

def get_all_by_location(location):
    pass

def get_all_by_role(role):
    pass # e.g. desktops, blades, etc.W
