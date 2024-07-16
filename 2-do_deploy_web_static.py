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
    # Upload the archive to the /tmp/ directory of the web server
    put(f"{archive_path}", "/tmp/")

    remote_archive_path = "/tmp/{}".format(str(archive_path).split('/')[-1])
    filename = str(archive_path).split("/")[-1].split(".")[0]
    uncompress_to = f"/data/web_static/releases/{filename}"

    run(f"sudo mkdir -p {uncompress_to}")
    run(f"sudo tar -xvf {remote_archive_path} -C {uncompress_to}")
    # run(f"sudo mv -f {uncompress_to}/web_static/* {uncompress_to}")
    run(f"sudo cp -r {uncompress_to}/web_static/* {uncompress_to}")
    run(f"sudo rm -r {uncompress_to}/web_static/*")
    run(f"sudo rm -r {uncompress_to}/web_static")
    run(f"sudo rm -r {remote_archive_path}")
    run("sudo rm /data/web_static/current")
    run(f"sudo ln -s /data/web_static/releases/{filename} \
                    /data/web_static/current")
