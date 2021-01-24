def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # reverse_phrase = list(phrase)[::-1]
    # return ''.join(reverse_phrase)
    return phrase[::-1]

print('should return god: ', reverse_string('dog'))