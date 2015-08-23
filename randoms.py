import random
import string


class Randoms(object):
    '''
    A class with all the random letter and number generating that 
    you could want.

    :length: the lenth of characters to return.
    '''
    def __init__(self, length=None, *args, **kwargs):
        self.length = length or 10

    def _get_length(self, length):
        if not length:
            return self.length
        else:
            return length

    def _generate(self, string, length=None):
        '''
        :string: is the character-string to randomly pick from.
        '''
        return ''.join([random.choice(string) for x in range(self._get_length(length))])

    def letters(self, length=None):
        return self._generate(string.ascii_letters, length)

    def lowercase(self, length=None):
        return self._generate(string.ascii_lowercase, length)

    def uppercase(self, length=None):
        return self._generate(string.ascii_uppercase, length)

    def digits(self, length=None):
        return self._generate(string.digits, length)

    def integer(self, length=None):
        return int(self._generate(string.digits, length))

    def float(self, length=None):
        return float(self._generate(string.digits, length))        