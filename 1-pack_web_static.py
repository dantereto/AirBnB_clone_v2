#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from datetime import datetime
import os.path
from fabric.api import local


def do_pack():
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(time)
    local('mkdir -p versions')
    local('tar -cvzf' + path + ' web_static')
    if os.path.exists(path):
        return path
    else:
        return None
