#!/usr/bin/python3
from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """Fabric script that generates a .tgz archive from the contents
    of the web_static folder  function do_pack"""

    if not os.path.exists('./versions'):
        local('mkdir versions')

    date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = 'versions/web_static_{}.tgz'.format(date)
    result = local('tar -cvzf {} web_static'.format(archive))

    if result.failed:
        return None
    else:
        return archive
