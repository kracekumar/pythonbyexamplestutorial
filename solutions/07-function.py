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

def is_sonnet(poem):
    """Return the poem is sonnet or not
    """
    return len([line for line in poem.split("\n") if line]) == 14


def total_words(poem):
    """Function returns total number of words in the poem
    """
    lines = [line for line in poem.split("\n") if line]
    return sum([len([word for word in line.split(" ") if word]) for line in lines])


def word_count(poem):
    """Returns dictionary containing words as key and count as value
    """
    lines = [line for line in poem.split("\n") if line]
    word_map = {}
    for line in lines:
        for word in line.split(" "):
            if word:
                if word in word_map:
                    word_map[word] += 1
                else:
                    word_map[word] = 1
    return word_map


def unique_words(poem):
    """Return unique words in the poem as a set
    """
    lines = [line for line in poem.split("\n") if line]
    words = set([])
    for line in lines:
        for word in line.split(" "):
            if word:
                words.add(word)
    return words


def find_total_occurrences(poem, *words):
    """Find total occurences of the words in the poem.
    """
    word_counts = word_count(poem)
    print word_counts
    return {word: word_counts.get(word, 0) for word in words}


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

    # Edit the function total_words to return total words in the poem
    print "Total words: {}".format(total_words(poem))

    # Step 2
    # Find the poem is sonnet or not ?
    print "Is the poem sonnet?: {}".format(is_sonnet(poem))

    # Step 3
    # Find the word frequency in the peom using word_count
    print "Word frequency: {}".format(word_count(poem))

    # Step 4
    # Find unique words in the poem using unique_words
    print "Unique words: {}".format(unique_words(poem))

    # Step 5
    # Find total occurences of few words
    print "Specific word count; {}".format(find_total_occurrences(poem, "Krace", "Robert", "roads", "wood,"))

# __name__ holds the name of the current module
if __name__ == "__main__":
    main() # call main function
