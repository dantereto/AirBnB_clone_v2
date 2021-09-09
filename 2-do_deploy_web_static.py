#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from datetime import datetime
import os.path
from fabric.api import *
env.user = "ubuntu"
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
    """distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        dire = "data/web_static/releases"
        file_name = archive_path.split('/')[-1]
        wext = file_name.split('.')[0]
        put(archive_path, "/tmp/{}".format(file_name))
        run("sudo mkdir -p mkdir -p /{}/{}".format(dire, wext))
        run("sudo tar -xzf /tmp/{} -C /{}/{}/".format(file_name, dire, wext))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv /{}/{}/web_static/* /{}/{}/".format(dire, wext, dire, wext))
        run("sudo rm -rf /{}/{}/web_static".format(dire, wext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /{}/{}/ /data/web_static/current".format(dire, wext))
        return True

    except Exception:
        return False
