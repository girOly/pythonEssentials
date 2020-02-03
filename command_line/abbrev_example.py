import argparse

my_parser = argparse.ArgumentParser(description='Just messing around with CLI',
                                    add_help=False)
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(args.input)
