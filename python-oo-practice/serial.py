"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
      self.start = start
      self.counter = -1
    
    def __repr__(self):
      '''Show representation.'''
      return f'<SerialGenerator start={self.start} next={self.start + self.counter + 1}'

    def generate(self):
      '''Add incrementer to start number and return'''
      self.counter += 1
      return self.start + self.counter
    
    def reset(self):
      '''Reset incrementer'''
      self.counter = -1
    
    
      