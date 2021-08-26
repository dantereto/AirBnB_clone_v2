#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from datetime import datetime
import os.path
from fabric.api import *
env.hosts = ['34.139.63.159', '34.139.12.106']


def do_pack():
    """do_pack"""
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(time)
    local('tar -cvzf' + path + ' web_static')
    if os.path.exists(path):
        return path
    else:
        return None


def do_deploy(archive_path):
    """ deploy """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        put(archive_path, '/tmp/')
        route = archive_path.split('/')[-1]
        folder = ('/data/web_static/releases/' + route-split('.')[0])
        run('mkdir -p archive_path')
        run('tar -cvzf /tmp/{} -C {}'.format(route, folder))
        run('rm /tmp/' + route)
        run('rm /data/web_static/current')
        run('ln -s' + folder + '/data/web_static/current')
        return True
    except:
        return False
