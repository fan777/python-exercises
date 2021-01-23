def print_upper_words(words):
  """ print each word uppercase """
  for word in words:
    print(word.upper())

def print_upper_words_with_e(words):
  """ print each word uppercase if start with e """
  for word in words:
    if word[0].upper() == 'E': # can use word.startswith('e')
      print(word.upper())

def print_upper_words_start(words, must_start_with):
  """print words that start with letter"""
  for word in words:
    for letter in must_start_with:
      if word[0].upper() == letter.upper():
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words_with_e(["hello", "elephant", "hey", "goodbye", "yo", "yes"])
print_upper_words_start(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])