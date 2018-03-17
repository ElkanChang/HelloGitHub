#!/usr/bin/env python3

import sys

def copy_file(src,dst):
    with open(src,"r") as src_file:
        with open(dst,"w") as dst_file:
            for line in src_file:
                dst_file.write(line)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print("Parameter Error")
        print(sys.argv[0],"src_file dest_file")
        sys.exit(-1)
    sys.exit(0)

