"""Fabfile for PyData Paris."""

from fabric.api import env, task
from fabric.operations import local
from fabtools import require

env.user = 'root'
env.hosts = ['dedibox.abilian.com']

VH_PYDATA = """
server {
  server_name pydata.fr www.pydata.fr;

  access_log /var/log/nginx/pydata2016-access.log;

  rewrite ^/ http://pydata.org/paris2016/ permanent;
}

server {
  server_name pydataparis.joinux.org pydata.joinux.org;

  access_log /var/log/nginx/pydata2016-access.log;

  rewrite ^/$ http://pydata.org/paris2016/ permanent;
  rewrite ^/(.*) http://2015.pydata.fr/$1 permanent;
}

server {
  server_name 2015.pydata.fr;

  root /var/www/pydata2015;
  index index.html;

  access_log /var/log/nginx/pydata2015-access.log;
}
"""


@task
def setup_nginx():
  require.nginx.site("pydata.fr", VH_PYDATA)


@task
def deploy():
  require.directory("/var/www/pydata")
  local("rsync -e ssh -avz build/ root@dedibox.abilian.com:/var/www/pydata2015")
