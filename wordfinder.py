"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)
        print(self.words)
        print(f"{len(self.words)}")

    def parse(self, file):
        return [w.strip() for w in file]

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    def parse(self, file):
        return [w.strip() for w in file
                if w.strip() and not w.startswith("#")]
