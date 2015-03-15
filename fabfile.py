from fabric.api import env, task
from fabric.operations import local
from fabtools import require

env.user = 'root'
env.hosts = ['dedibox.abilian.com']

VH_PYDATA = """
server {
  server_name pydataparis.joinux.org pydata.joinux.org;

  root /var/www/pydata;
  index index.html;

  access_log /var/log/nginx/pydata-access.log;
}
"""


@task
def setup_nginx():
  require.nginx.site("pydataparis.joinux.org", VH_PYDATA)


@task
def deploy():
  require.directory("/var/www/pydata")
  local("rsync -e ssh -avz build/ root@dedibox.abilian.com:/var/www/pydata")
