from fabric.api import run, cd


def update():
    with cd('/root/deploy/'):
        run('git pull')
        run('docker-compose stop')
        run('docker-compose rm')
        run('docker-compose up -d')
