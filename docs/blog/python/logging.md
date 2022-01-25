# Logging


## Simple logger

A simple Python logger with stream and file handler

```python
import logging
from logging.handlers import RotatingFileHandler

# setup logger with basic configuration
logging.basicConfig(  # noqa
    level=logging.INFO,
    format="[%(asctime)s]:%(levelname)s %(name)s :%(module)s/%(funcName)s,%(lineno)d: %(message)s",
    handlers=[
        RotatingFileHandler('/var/log/runlog.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('myapp')
logger.info('Hello, World!')
# [2020-06-22 15:48:15,799]:INFO myapp :test/<module>,2: Hello, World!
```

## Multi level logging

```python
import logging

debug = logging.FileHandler("/var/log/debug.log")
debug.setLevel(logging.DEBUG)

error = logging.FileHandler("/var/log/error.log")
error.setLevel(logging.ERROR)

warning = logging.FileHandler("/var/log/warning.log")
warning.setLevel(logging.WARNING)

console = logging.StreamHandler()

logging.basicConfig(  # noqa
    level=logging.INFO,
    format="[%(asctime)s]:%(levelname)s %(name)s :%(module)s/%(funcName)s,%(lineno)d: %(message)s",
    handlers=[debug, error, warning, console]
)

logger = logging.getLogger()
logger.debug("This is debug  [error+warning]")
logger.error("This is error  [error only]")
logger.warning("This is warn [error+warning]")
```
