#!/usr/bin/python3
"""Compress web_static package"""
from fabric.api import *
from datetime import datetime
from time import strftime
from os import path


env.hosts = ['52.207.73.79', '3.85.177.63']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Fabric script: generate a .tgz archive from content of web_static"""
    fileName = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/web_static_{fileName}.tgz web_static/")
        return f"versions/web_static_{fileName}.tgz"

    except Exception as e:
        return None


def do_deploy(archivePath):
    """Deploy web files to the servers"""
    try:
        if not (path.exists(archivePath)):
            return False

        # Upload archive
        put(archivePath, '/tmp/')

        # Create target directory
        timesTamp = archivePath[-18:-4]
        run(f"sudo mkdir -p /data/web_static/\
releases/web_static_{timesTamp}/")

        # Uncompress archive and delete .tgz
        run(f"sudo tar -xzf /tmp/web_static_{timesTamp}.tgz -C \
/data/web_static/releases/web_static_{timesTamp}/")

        # Remove archive
        run(f"sudo rm /tmp/web_static_{timesTamp}.tgz")

        # Move contents to host web_static
        run(f"sudo mv /data/web_static/releases/web_static_{timesTamp}\
/web_static/* /data/web_static/releases/web_static_{timesTamp}/")

        # Remove external web_static directory
        run(f"sudo rm -rf /data/web_static/releases/\
web_static_{timesTamp}/web_static")

        # Delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Re-establish the symbolic link
        run(f"sudo ln -s /data/web_static/releases/\
web_static_{timesTamp}/ /data/web_static/current")
    except Exception:
        return False

    # Return true on success
    return True
