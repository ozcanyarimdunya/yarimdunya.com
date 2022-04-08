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
        sites = map(str, ["x", "y", "z"])
        self.add_argument(
            "--tag",
            type=str,
            help="Tag, choose from {%(choices)s}",
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
