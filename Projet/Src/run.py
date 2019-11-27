#!/bin/env python3

import os
import sys
import time

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("MAUVAIX NOMBRE D'ARGUMENTS. Format : 0^1 HeureDebut HeureFin")
        sys.exit(1)
    else:
        os.system("cd data;./downloadData.py "+ (" ").join(sys.argv[1:]) + \
        ";./wgrib2 donneesSP1IP2.grib2 -netcdf resultatSP1IP2.nc;pvpython vueSP1.py;;pvpython vueIP2.py;google-earth $(pwd)/fileSP1.kml;cd ..")
