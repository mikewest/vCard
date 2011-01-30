#!/usr/bin/env python
# encoding: utf-8

#
# Import the `with` statement from The Future (!) to ensure compatability
# with Python 2.5.
#
from __future__ import with_statement

#
# We need `base64` for the heavy lifting, `os` to join paths, `sys` to
# exit, and `re` to do search and replace.
#
import base64
import os
import re
import sys

# Open up `./src/index.html` for reading, and `./build/index.html` for
# writing.  Sequentially read lines from the former, process them if
# they contain references to PNG files, and dump the resulting lines
# into the latter.
def main():
    with open( "./src/index.html", "r" ) as infile:
        with open( "./build/index.html", "w" ) as outfile:
            for line in infile:
                outfile.write( processPNGs( line ) )

# Given a line that contains a PNG, open the referenced PNG file,
# encode it, and replace the PNG filename with the encoded string.
# Return the result after substitution.
def processPNGs( line ):
    def replacer( matchobj ):
        png = matchobj.group(0)
        with open( os.path.join( "src", png ), "r" ) as infile:
            data = infile.read()
        return "data:image/png;base64,%s" % base64.b64encode(data)

    return re.sub( "([a-zA-Z]*.png)", replacer, line )


#
# As is typical for Python scripts, we test to see if this file is
# being executed or included.  If it's being executed
# (`if __name__ == "__main__"`), then run the `main` function.  If
# not, do nothing at all.
#
if __name__ == "__main__":
    sys.exit(main())
