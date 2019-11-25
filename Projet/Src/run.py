#!/bin/env python3

import os
import sys
import time

if __name__ == "__main__":
    if (len(sys.argv) != 5):
        print("MAUVAIX NOMBRE D'ARGUMENTS. Format : 0^1 HeureDebut HeureFin Mode")
        sys.exit(1)
    else:
        os.system("cd data;./downloadData.py "+ (" ").join(sys.argv[1:]) + \
        ";./wgrib2 donneesGroupees.grib2 -netcdf resultat.nc;pvpython vue.py;cd ..; eog out.png")
