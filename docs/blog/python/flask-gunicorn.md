# Gunicorn in Flask app

A deployment script for flask with gunicorn

## Folder structure

```
.
├── app.py
├── deploy.sh
├── gunicorn.pid
├── gunicorn.py
├── requirements.txt
├── static
│   ├── download.pdf
│   └── index.js
├── templates
│   ├── about.html
│   ├── base.html
│   ├── history.html
│   ├── index.html
│   ├── sss.html
│   └── test.html
└── wsgi.py

2 directories, 14 files
```

## gunicorn.py

```python
bind = '0.0.0.0:5001'
backlog = 2048

workers = 2
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

max_requests = 1000

daemon = True
pidfile = 'gunicorn.pid'
raw_env = [
    "SECRET_KEY=_5#y2L'F4Q8z\n\xec]",
    "FLASK_ENV=production"
]


def pre_fork(server, worker):
    server.log.info("Check some connection")

```

## wsgi.py

```python
from app import app

if __name__ == '__main__':
    app.run(debug=False)

```

## deploy.sh
```shell
#!/bin/bash

if [ -f 'gunicorn.pid' ]; then
  while IFS= read -r process; do
    kill -9 "$process"
  done < gunicorn.pid
fi


gunicorn -c gunicorn.py wsgi:app

```
