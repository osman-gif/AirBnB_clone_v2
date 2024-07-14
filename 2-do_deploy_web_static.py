#!/usr/bin/python3
import os
from fabric.api import env, local, put, run


def do_deploy(archive_path):
    """A Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy"""

    env.hosts = ['54.162.48.101', '100.26.167.222']
    if not os.path.exists(archive_path):
        return False
    put("{}".format(archive_path), "/tmp/")
    archive_path_server = "/tmp/{}".format(archive_path)
    filename = str(archive_path).split("/")[-1].split(".")[0]
    if not run("tar -xzvf /data/web_static/releases/{}".format(filename)):
        return False
    elif not run("rm -r {}".format(archive_path_server)):
        return False
    elif not run("rm /data/web_static/current"):
        return False
    elif not run("ln -s /data/web_static/releases/{} \
                 /data/web_static/current".format(filename)):
        return False
    else:
        True
