import argparse

import os
import sys


# Creates the Parser
my_parser = argparse.ArgumentParser(description='List the content of a Folder')

# Add the arguments

my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()