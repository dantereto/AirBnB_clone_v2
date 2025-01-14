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
        route = archive_path.split('/')[-1]
        folder = ('/data/web_static/releases/' + route.split('.')[0])
        put(archive_path, '/tmp/' + route)
        run('sudo mkdir -p {}'.format(folder))
        run('sudo tar -xzf /tmp/{} -C {}'.
            format(route, folder))
        run('sudo rm /tmp/{}'.format(route))
        run('sudo mv {}/web_static/* {}/'.format(folder, folder))
        run('sudo rm -rf {}/web_static'.format(folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(folder))
        return True
    except:
        return False


def deploy():
    """deploy v2"""

    pack = do_pack()
    if pack is None:
        return False
    else:
        return(do_deploy(pack))
