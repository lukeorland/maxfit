    usage: maxfit.py [-h] [--limit LIMIT] [--scaling_divisor SCALING_DIVISOR]
                     [--verbose]
                     [file_names [file_names ...]]
    
    Prints the files that comprise the best fit within the size limit.
    
    positional arguments:
      file_names            Files that are candidates for fitting.
    
    optional arguments:
      -h, --help            show this help message and exit
      --limit LIMIT         The number of bytes limit in which to find the maximum
                            fit. The default value is 5368709120 (5 GiB).
      --scaling_divisor SCALING_DIVISOR
                            Reduce the complexity of the computation by dividing
                            the limit by scale_divisor integer value. The default
                            value is 1000000.
      --verbose, -v         Report extra info.

# Notes
* Be careful when adjusting the values of `LIMIT` and `SCALING_DIVISOR`. At
  least two Python lists are created with the number of elements equal to
  (`LIMIT` / `SCALING_DIVISOR`). If `SCALING_DIVISOR` is too small, the memory
  usage for these lists will be huge.
* Verbose output includes the number of candidate files and the left-over unused
  space.

# Example

    python ${MAXFIT_SOURCE_DIR}/maxfit.py *.m4v *.mov
