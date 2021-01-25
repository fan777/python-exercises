"""Word Finder: finds random words from a dictionary."""
from random import choice
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):

  def __init__(self, file):
    super().__init__(file)
    
  def build(self):
    d = []
    f = open(self.file, 'r')
    for line in f:
      if line.strip() and not line[0] == '#':
        d.append(line.strip())
    return d

# OFFICIAL

# class SpecialWordFinder(WordFinder):
#     """Specialized WordFinder that excludes blank lines/comments.
    
#     >>> swf = SpecialWordFinder("complex.txt")
#     3 words read

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True
#     """

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words, skipping blanks/comments."""

#         return [w.strip() for w in dict_file
#                 if w.strip() and not w.startswith("#")]