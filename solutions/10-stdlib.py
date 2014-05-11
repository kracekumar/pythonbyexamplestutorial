#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

"""
Write a program to display the peom The Road Not Taken by Robert Frost.

Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference
"""

def main():
    # Step 1
    # Check whether 'road-not-taken.txt' file is present in current directory
    print "Road not taken file exists?: {}".format(os.path.exists("road-not-taken.txt"))

    # Step 2
    # Get list of words as command line arguments and check its presence
    poem = """
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference
"""

    for word in sys.argv[1:]:
        if word in poem:
            print "Word: {} is present".format(word)
        else:
            print "Word: {} is absent".format(word)


# __name__ holds the name of the current module
if __name__ == "__main__":
    main() # call main function
