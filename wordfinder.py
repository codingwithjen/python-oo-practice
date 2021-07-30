"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    """Return a random word from a list of words.

    >>> wf = WordFinder("simple.txt")
    3 words are read

    >>> wf.random() in ["Cat", "Dog", "Porcupine"]
    True

    >>> wf.random() in ["Cat", "Dog", "Porcupine"]
    True

    >>> wf.random() in ["Cat", "Dog", "Porcupine"]
    True
    """

    def __init__(self, path):
        """Reads path to a file on a disk that contains words and reads that file"""

        dict_file = open("simple.txt", "r")

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")
    
    def parse (self, dict_file):
        """Parse dictfile into list of words"""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Return it without the blank lines or comments

    >>swf = SpecialWordFinder("complex.txt")
    3 words read 

    >>> swf.random() in ["Pear", "Carrot", "Kale"]
    True

    >>> swf.random() in ["Pear", "Carrot", "Kale"]
    True

    >>> swf.random() in ["Pear", "Carrot", "Kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file to list of words and skipping blank lines and/or comments"""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

