# Supervisor

### Install supervisor

```shell
pip3 install supervisor
```

### Create config dir

```shell
mkdir /etc/supervisor && echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

### Configuration for new tasks

```shell
mkdir /etc/supervisor/conf.d
```

```text
#/etc/supervisor/supervisord.conf
;----------- * -----------
;Supervisor configurations
;----------- * -----------

[unix_http_server]
file=/tmp/supervisor.sock

[inet_http_server
port=*:9001

[supervisord]
logfile=/tmp/supervisord.log
logfile_maxbytes=50MB
logfile_backups=10
loglevel=info
pidfile=/var/run/supervisord.pid
nodaemon=false
minfds=1024
minprocs=200
user=root
childlogdir=/tmp

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock


[include]
files = conf.d/*.conf

```

```shell
mkdir /etc/supervisor/conf.d
```

### Configure and starting the supervisor server

```shell
touch /etc/systemd/system/supervisord.service
```

```shell
# add below codes to /etc/systemd/system/supervisord.service

[Unit]
Description=Supervisor daemon
Documentation=http://supervisord.org
After=network.target

[Service]
ExecStart=/usr/local/bin/supervisord -n -c /etc/supervisor/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
Alias=supervisord.service
```

```shell
systemctl enable supervisord.service
```

```shell
systemctl start supervisord.service
```

## A demo application

Assert you have a running script named `my_script.sh`

### Create supervisor config for program

```shell
touch /etc/supervisor/conf.d/my_script.conf
```

```shell
# write below conf to /etc/supervisor/conf.d/my_script.conf

[program:my_script]
command=/root/my_script.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/my_script.err.log
stdout_logfile=/var/log/my_script.out.log
```

### Inform supervisor

```shell
supervisorctl reread
```

```shell
supervisorctl update
```
