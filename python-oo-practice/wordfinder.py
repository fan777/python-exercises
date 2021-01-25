"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:

  def __init__(self, file):
    self.file = file
    self.word_list = self.build()
    print(f'{len(self.word_list)} words read')
    
  def build(self):
    d = []
    f = open(self.file, 'r')
    for line in f:
      d.append(line.strip())
    return d

  def random(self):
    return choice(self.word_list)
  
# class WordFinder:
#     """Machine for finding random words from dictionary.
    
#     >>> wf = WordFinder("simple.txt")
#     3 words read

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True
#     """

#     def __init__(self, path):
#         """Read dictionary and reports # items read."""

#         dict_file = open(path)

#         self.words = self.parse(dict_file)

#         print(f"{len(self.words)} words read")

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words."""

#         return [w.strip() for w in dict_file]

#     def random(self):
#         """Return random word."""

#         return random.choice(self.words)