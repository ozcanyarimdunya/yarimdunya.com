# ArgumentParser


## Basic argparse

```python
from argparse import Action
from argparse import ArgumentError
from argparse import ArgumentParser as BaseArgumentParser
from argparse import HelpFormatter as BaseHelpFormatter
from collections import defaultdict

__version__ = "0.1.0"


class PrintAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        parser.exit(message="Another print and then exit message like help action\n")


class ParseKVAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, defaultdict(str))
        for each in values:
            try:
                key, value = each.split("=")
                getattr(namespace, self.dest)[key] = value
            except ValueError as ex:
                message = "\nTraceback: {}".format(ex)
                message += "\nError on '{}' || It should be 'key=value'".format(each)
                raise ArgumentError(self, str(message))


class HelpFormatter(BaseHelpFormatter):
    def __init__(self, prog):
        super(HelpFormatter, self).__init__(prog=prog, max_help_position=32, width=100)


class ArgumentParser(BaseArgumentParser):
    def __init__(self):
        super(ArgumentParser, self).__init__(
            description="A sample argument parser",
            formatter_class=HelpFormatter,
        )
        sites = map(str, {"x", "y", "z"})
        self.add_argument(
            "--tags",
            type=str,
            help="Tags, choose from {%(choices)s}",
            choices=sites,
            metavar="VALUE",
            required=True,
        )
        self.add_argument(
            "--version",
            action="version",
            help="Show program's version number and exit",
            version=__version__,
        )
        self.add_argument(
            "--verbose",
            help="See more detailed logs",
            action="store_true",
            default=False,
        )
        self.add_argument(
            "-p",
            "--print",
            action=PrintAction,
            nargs=0,
            help="Show print message and exit",
            default=False,
        )
        self.add_argument(
            "-H",
            "--host-names",
            dest="hosts",
            nargs='+',
            action=ParseKVAction,
            help='Parameter accepts -H host1=localhost "host2=other hosts"',
            metavar="KEY1=VALUE1",
        )


args = ArgumentParser().parse_args()
print(args)
```

### Usage


```
$ python test.py --help

usage: test.py [-h] --tags VALUE [--version] [--verbose] [-p] [-H KEY1=VALUE1 [KEY1=VALUE1 ...]]

A sample argument parser

optional arguments:
  -h, --help                    show this help message and exit
  --tags VALUE                  Tags, choose from {y, x, z}
  --version                     Show program's version number and exit
  --verbose                     See more detailed logs
  -p, --print                   Show print message and exit
  -H KEY1=VALUE1 [KEY1=VALUE1 ...], --host-names KEY1=VALUE1 [KEY1=VALUE1 ...]
                                Parameter accepts -Y host1=localhost "host2=other hosts"
```

```
$ python test.py --tags x 

Namespace(hosts=None, print=False, tags='x', verbose=False)
```

```
$ python test.py --version

0.1.0
```

```
$ python test.py --print 

Another print and then exit message like help action
```

```
$ python test.py --tags x --host-names host1=localhost "host2=other hosts" --verbose

Namespace(hosts=defaultdict(<type 'str'>, {u'host2': u'other hosts', u'host1': u'localhost'}), print=False, tags='x', verbose=True)
```


## Advanced argparse


```python
import argparse
import sys

__version__ = "0.1.0"


class UpParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        super(UpParser, self).__init__(**kwargs)
        self.add_argument(
            "-d",
            help="Run in daemon mode",
            action="store_true",
            default=False,
        )
        self.add_argument(
            "--build",
            help="Build image",
            action="store_true",
            default=False,
        )


class DownParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        super(DownParser, self).__init__(**kwargs)
        self.add_argument(
            "--volume",
            help="Remove volume",
            action="store_true",
            default=False,
        )


class DockerParser(argparse.ArgumentParser):
    def __init__(self):
        super(DockerParser, self).__init__(description="Docker")
        self.add_argument(
            "command",
            choices=["up", "down"],
            help="subcommands"

        )
        self.add_argument(
            "-v",
            "--version",
            action="version",
            help="show program's version number and exit",
            version=__version__,
        )

    def parse_args(self, *_):
        super_ = super(DockerParser, self).parse_args(sys.argv[1:2])
        return super_.command, getattr(self, super_.command)

    @staticmethod
    def _register_commons(prs):
        prs.add_argument(
            "-V",
            "--verbose",
            dest="verbose",
            help="set logger to debug to see more detailed logs",
            action="store_true",
            default=False,
        )

    @property
    def up(self):
        up_parser = UpParser(
            prog="{} up".format(self.prog)
        )
        self._register_commons(up_parser)
        return up_parser.parse_args(sys.argv[2:])

    @property
    def down(self):
        down_parser = DownParser(
            prog="{} down".format(self.prog)
        )
        self._register_commons(down_parser)
        return down_parser.parse_args(sys.argv[2:])


name, args = DockerParser().parse_args()
print(name, args)

```

### Usage

```text
$ python docker.py --help 
usage: docker.py [-h] [-v] {up,down}

Docker

positional arguments:
  {up,down}      subcommands

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

---

```text
$  python docker.py up --help 
usage: docker.py up [-h] [-d] [--build] [-V]

optional arguments:
  -h, --help     show this help message and exit
  -d             Run in daemon mode
  --build        Build image
  -V, --verbose  set logger to debug to see more detailed logs
```

---

```text
$ python docker.py down --help 
usage: docker.py down [-h] [--volume] [-V]

optional arguments:
  -h, --help     show this help message and exit
  --volume       Remove volume
  -V, --verbose  set logger to debug to see more detailed logs
```

---

```text
$ python docker.py up -d --build --verbose 

up Namespace(d=True, build=True, verbose=True)
```
