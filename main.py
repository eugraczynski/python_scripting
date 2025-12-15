import argparse
import util.zipHelper as zipModule


# argparse section
parser = argparse.ArgumentParser(description="Process some tasks.")
parser.add_argument(
    "-m",
    "--mode",
    action="store",
    type=str,
    help="Mode",
)
parser.add_argument("-p", "--path", action="store", type=str, help="Path to zip")
args = parser.parse_args()

args_set = set()
if args.path is not None:
    args_set.add(args.path)
if args.mode is not None:
    args_set.add(args.mode)

print(r",".join(args_set))
a, b = args_set
print(a, b)
zipper = zipModule.ZipHelper()

print(args_set)
