#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.234.80.45', '54.84.193.100']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        folder = archive_path.split("/")[-1]
        file_name = folder.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(folder, path, file_name))
        run('rm /tmp/{}'.format(folder))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_name))
        run('rm -rf {}{}/web_static'.format(path, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_name))
        return True
    except:
        return False
