#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from datetime import datetime
import os.path
from fabric.api import local

def do_pack():
    time = now.strftime('%Y%m%d%H%M%S')
    path = 'version/web_static_{}.tgz'.format(time)
    if os.path.exist('versions'):
        local('mkdir versions')
    local('tar -cvzf' + path + ' web_static')
    if os.path.exist(path):
        return path
    else:
        return None
