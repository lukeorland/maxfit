#!/usr/bin/env python

from __future__ import print_function, division
import argparse
import os
import zero_one_knapsack

def file_size(file_name):
    """Returns size of the file named file_name in bytes."""
    if not os.path.exists(file_name):
        msg = "The file {} does not exist.".format(file_name)
        raise argparse.ArgumentTypeError(msg)
    return os.path.getsize(file_name)

def bytes_to_MB(bytes):
    """Keep return int value"""
    return bytes / 1000000

def main():

    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description='Process some integers.')

    # one optional flag
    # --limit limit  # number of bytes to fit
    # default: limit = 5 GB
    parser.add_argument('--limit', default=5000000000, type=int,
                        help='number of bytes limit in which to find max fit')

    # Any arguments are interpreted as files that are candidates for fitting
    # If list of files not passed, get list of all the video files in this
    # directory.
    parser.add_argument('file_names', nargs='*',
                        help='files that are candidates for fitting')

    args = parser.parse_args()
    limit = args.limit
    file_names = args.file_names
    file_sizes = [file_size(fn) for fn in file_names]

    # Print out input stats.
    print("limit = {} MB".format(bytes_to_MB(limit)))
    #sizes_strs = ["{} bytes".format(s) for s in file_sizes]
    #names_sizes = zip(file_names, sizes_strs)
    #print("file sizes = \n")
    #for name, size in names_sizes:
    #    print("\t{}\t{}".format(size, name))

    # Encode as 0-1 Knapsack problem, Solve, Decode.
    optimal_file_sizes = zero_one_knapsack.solve_same_values(file_sizes, limit)
    limit_used_up = sum(optimal_file_sizes)
    limit_not_used_up = limit - limit_used_up

    # Print out remaining bytes.

    # Print out list of optimal files.
    print(len(file_sizes))
    print(optimal_file_sizes)
    print("limit not used = {} MB".format(bytes_to_MB(limit_not_used_up)))
    for size in optimal_file_sizes:
        print(file_names[file_sizes.index(size)])


if __name__ == '__main__':
    main()
