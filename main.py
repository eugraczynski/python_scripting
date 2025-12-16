import argparse
import util.zipHelper as zipModule


# argparse section
parser = argparse.ArgumentParser(description="Process some tasks.")
parser.add_argument(
    "-m", "--mode", action="store", type=str, help="Pack, Unpack, Cleanup"
)
parser.add_argument("-p", "--path", action="store", type=str, help="Path to zip")
parser.add_argument(
    "-s",
    "--source",
    action="store",
    type=str,
    default="Data_to_extract/Tasks.zip",
    help="Path to source file",
)
parser.add_argument(
    "-d",
    "--destination",
    action="store",
    type=str,
    default="packed_config.zip",
    help="Path to save zip",
)
args = parser.parse_args()

# args_set = set()
# if args.path is not None:
#     args_set.add(args.path)
# if args.mode is not None:
#     args_set.add(args.mode)

# print(r",".join(args_set))
# a, b = args_set
# print(a, b)
# print(args_set)



zipper = zipModule.ZipHelper(args.path, args.mode, args.source, args.destination)
