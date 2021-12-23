"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function


import numpy as np
import sys

import nsfg
import thinkstats2

def read_resp( dt_file='2002FemResp.dct',
                dut_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dt_file)
    df = dct.ReadFixedWidth(dut_file, compression='gzip', nrows=nrows)
    preg_count = count_pregnum(df)
    return preg_count

def count_pregnum(df):
    preg_count = df.pregnum.count()
    return preg_count

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = read_resp()
    assert (len(df) == 7643)

    count_of_preg = count_pregnum(df)


    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
