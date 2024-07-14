#!/usr/bin/python3
import os
from fabric.api import env, local, put, run
env.hosts = ['ubuntu@54.162.48.101', 'ubuntu@100.26.167.222']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """A Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy"""

    if not os.path.exists(archive_path):
        return False
    put("{}".format(archive_path), "/tmp/")
    archive_path_server = "/tmp/{}".format(str(archive_path).split('/')[-1])
    filename = str(archive_path).split("/")[-1].split(".")[0]
    if run("sudo mkdir -p /data/web_static/releases/{}".format(filename)):
        pass
    if run(f"tar -xvf {archive_path_server} -C /tmp/"):
        pass
    elif not run("rm -r {}".format(archive_path_server)):
        pass
    elif not run("rm /data/web_static/current"):
        pass
    elif not run("ln -s /data/web_static/releases/{} \
                 /data/web_static/current".format(filename)):
        pass
    else:
        True
