import argparse
import util.zipHelper as zipModule


# argparse section
parser = argparse.ArgumentParser(description="Process some tasks.")
parser.add_argument("-p", "--path", action="store", type=str, help="Path to zip", default=None)
parser.add_argument(
    "-m", "--mode", action="store", type=str, help="Pack, Unpack, Cleanup", default="unpack"
)
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

# args_set = []

# if args.path is not None:
#     args_set.append(args.path)
# else:
#     raise TypeError("Path argument is required")

# if args.mode is not None:
#     args_set.append(args.mode)

# if args.source is not None:
#     args_set.append(args.source)

# if args.destination is not None:
#     args_set.append(args.destination)

zipper = zipModule.ZipHelper(args.path, args.mode, args.source, args.destination)

"""
1. remake main with the arg to have at least 2 following args, mode and path to unzip (we will add more once we have more functionalities) 

2. create the dbc class, add a new unit signal with different byte size etc. You might need to do some research on dbc files but they are relative straightforward

3. As I remember you already had a XML function where we can add/edit a signal, make it a module.
"""
