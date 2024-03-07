#!/usr/bin/python3
from fabric.api import *
from time import strftime
from datetime import date


def do_pack():
    """Fabric script: generate a .tgz archive from content of web_static"""

    fileName = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/web_static_{fileName}.tgz web_static/")

        return f"versions/web_static_{fileName}.tgz"

    except Exception as e:
        return None
    