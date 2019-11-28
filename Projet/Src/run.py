#!/bin/env python3

import os
import sys
import time

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("MAUVAIX NOMBRE D'ARGUMENTS. Format : 0^1 Heure Package")
        sys.exit(1)
    else:
        os.system("cd data;./downloadData.py "+ (" ").join(sys.argv[1:]) + \
        ";pvpython vue"+sys.argv[3]+".py;google-earth $(pwd)/file"+sys.argv[3]+".kml;cd ..")
