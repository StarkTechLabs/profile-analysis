import argparse
import sys

from src.app import run


def parse(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-p", "--port", type=int, default=9090)
    parser.add_help = True

    return parser.parse_args(args=argv)


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) == 0:
        argv = ['-h']
    options = parse(argv)
    run(port=options.port, debug=options.debug)
