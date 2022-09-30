#!/usr/bin/python3
# A fabfile deletes out-of-date archives

from fabric.api import *

env.hosts = ['3.237.47.144', '18.206.92.91']
#username
env.user = "ubuntu"
#keyfile
env.key_filename = '~/.ssh/id_rsa


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0 or number == 1:
        num = 2
    elif number >= 2:
        num = number + 1

    with lcd("./versions"):
        local(
        'ls -t web_static_* | tail -n +{} | \
xargs rm -f -- && cd -'.format(num))
    with lcd("/data/web_static/releases"):
        run('ls -t web_static_* | tail -n +{} | \
xargs rm -f -- && cd -'.format(num))