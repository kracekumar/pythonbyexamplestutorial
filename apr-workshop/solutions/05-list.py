#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

# Below is function definition
def main():
    # Step 1
    # Find total number of lines in the poem
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
    lines = poem.split("\n")
    print "Total number of lines: {}".format(len(lines))

    # Step 2
    # Print total characters in first and last line
    print "Total chaarcters in first line:{}".format(len(lines[0]))

    #Step 3
    # Find no of times word "I" is used in the poem
    print "I came in the poem {} times".format(poem.count("I"))

    # Step 4:
    # Replace the last line with
    # And that has made all the difference.
    last_line = "And that has made all the difference."
    lines[-2] = last_line
    print lines

# __name__ holds the name of the current module
if __name__ == "__main__":
    main() # call main function
