"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Random word finder in file"""

    def __init__(self,path):
        """Reads the file, makes list of read words,
        counts number of words read from it
         >>> wf = WordFinder("simple.txt")
        read 3 words from the file 'simple.txt'

        >>> wf.random() in ["cat", "dog", "porcupine", "mouse", "elephant"]
        True

        >>> wf.random() in ["cat", "dog", "porcupine", "mouse", "elephant"]
        True

        >>> wf.random() in ["cat", "dog", "porcupine", "mouse", "elephant"]
        True
        """
        file_handle = open(path)
        self.words = []
        for line in file_handle:
            self.words.append(line.strip())
        print (f"read {len(self.words)} words from the file '{path}'")
    
    def random(self):
        """Returns random word from list"""
        return random.choice(self.words)
    
    def __repr__(self):
        """Representation"""

        return f"<WordFinder randomly returns words from text file>"


class SpecialWordFinder(WordFinder):
    """WordFinder that excludes empty lines and commented lines"""

    def __init__(self, path):
        
        file_handle = open(path)
        self.words = []
        for line in file_handle:
            if line.strip() and not line.startswith("#"):
                self.words.append(line.strip())
        print (f"read {len(self.words)} words from the file '{path}'")

    def __repr__(self):
        """Representation"""

        return f"<SpecialWordFinder randomly returns words from text file\n excluding empty and commented lines>"