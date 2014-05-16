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
    # Find total number of blank lines in the poem
    lines = poem.split("\n")
    count = 0
    for line in lines:
        if line == '':
            count +=1
    print count
    
    # Step 2
    # use sum function
    # Find total number of words in the poem
    cleaned_lines = [line for line in lines if line]
    print sum([len(line.split(" ")) for line in cleaned_lines])

    # Step 3
    # Display first 5 lines in the poem
    print cleaned_lines[:5]

    # Step 4:
    # Display lines till first line break
    pos = 1
    while lines[pos] != '':
        print lines[pos]
        pos += 1

# __name__ holds the name of the current module
if __name__ == "__main__":
    main() # call main function
