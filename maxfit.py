#!/usr/bin/env python

from __future__ import print_function, division
import argparse
import math
import os
import zero_one_knapsack

scale = 1e6

def file_size(file_name):
    """Returns size of the file named file_name in bytes."""
    if not os.path.exists(file_name):
        msg = "The file {} does not exist.".format(file_name)
        raise argparse.ArgumentTypeError(msg)
    return os.path.getsize(file_name)

def bytes_to_MB(bytes):
    """Returns float value"""
    return bytes / 1e6

def bytes_scaled(bytes, scale_divisor):
    """Returns float value"""
    return bytes / scale_divisor

def truncate(size, scale_divisor):
    return int(math.ceil(bytes_scaled(size, scale_divisor)))

def indices_best_fit_files(file_sizes, limit, scaling_divisor):
    file_sizes_scaled = [truncate(size, scale) for size in file_sizes]
    profits_scaled = file_sizes_scaled[:]
    limit_scaled = truncate(limit, scale)
    '''
    knap_result = knapsack.getItemsUsed(file_sizes_scaled, \
            knapsack.zeroOneKnapsack(file_sizes_scaled, profits_scaled,
                                     limit_scaled))
    return [idx for idx, val in enumerate(knap_result) if val == 1]
    '''
    return zero_one_knapsack.solve_dynamic_prog(file_sizes_scaled,
                                                profits_scaled, limit_scaled)

def report(msg, verbose):
    if verbose:
        print(msg)

def main():

    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description='Prints the files that ' +
                                     'comprise the best fit within the size ' +
                                     'limit.')

    # Optional flags
    # --limit limit  # number of MB to fit
    # default: limit = 5 GB
    parser.add_argument('--limit', default=5E9, type=int,
                        help='number of bytes limit in which to find max fit')

    parser.add_argument('--scaling_divisor', default=1e6, type=int,
                        help='reduce the complexity of the computation by ' +
                        'dividing the limit by scale_divisor integer value.')

    # Any arguments are interpreted as files that are candidates for fitting
    # If list of files not passed, get list of all the video files in this
    # directory.
    parser.add_argument('file_names', nargs='*',
                        help='files that are candidates for fitting')

    parser.add_argument('--verbose', '-v', action='count',
                        help='report extra info')

    args = parser.parse_args()
    limit = args.limit
    scaling_divisor = args.scaling_divisor
    verbose = args.verbose
    file_names = args.file_names

    # Print out input stats.
    report("\nlimit = {} bytes = {} MB".format(limit, bytes_to_MB(limit)),
           verbose)

    file_sizes = [file_size(fn) for fn in file_names]
    report("number of candidate files: {}".format(len(file_sizes)), verbose)

    # Encode as 0-1 Knapsack problem, Solve, Decode.
    #optimal_file_sizes = zero_one_knapsack.solve_same_values(file_sizes, limit)
    optimal_file_idxs = indices_best_fit_files(file_sizes, limit,
                                               scaling_divisor)

    # Print out remaining bytes.
    limit_used_up = 0
    optimal_files = []
    for idx in optimal_file_idxs:
        optimal_files.append(file_names[idx])
        limit_used_up += file_sizes[idx]

    limit_not_used_up = limit - limit_used_up

    # Print out list of optimal files.
    report("limit not used = {} MB".format(bytes_to_MB(limit_not_used_up)), verbose)
    report("\nfiles that fit best:\n", verbose)

    for file_name in optimal_files:
        print(file_name)


if __name__ == '__main__':
    main()

