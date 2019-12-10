import os
import unittest
#from selenium import webdriver
os.environ['MOZ_HEADLESS'] = '1'


class NumberToString(object):

    def __init__(self, num):
        self.UNDER20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        self.TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        self.ILLIONS = [
            '', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
            'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion',
            'decillion', 'undecillion', 'duodecillion', 'tredecillion',
            'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion',
            'octodecillion', 'novemdecillion', 'vigintillion'
        ]
        self.num = num

    @property
    def word(self):
        numstring = ""
        return self._wordify(self.num, numstring)

    def _wordify(self, num, word):
        if word and num != 0:
            word += " "
        if num < 20:
            word += self.UNDER20[num]
            return word
        if num < 100:
            tens, rest = divmod(num, 10)
            word += self.TENS[tens]
            return self._wordify(rest, word)
        if num < 1000:
            hundreds, rest = divmod(num, 100)
            word += self.UNDER20[hundreds] + ' hundred'
            return self._wordify(rest, word)
        illnum = (len([int(x) for x in str(num)]) - 1) // 3
        illion, rest = divmod(num, 1000**illnum)
        word += self._wordify(illion, "") + " " + self.ILLIONS[illnum]
        return self._wordify(rest, word)


class Fibonacci(object):

    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n
        self.fib()

    def fib(self):
        for i, num in zip(range(self.n + 1),self._fib()):
            print("{0:3d}: {1} - {2}".format(i, num, NumberToString(num).word))

    def _fib(self):
        while True:
            self.a, self.b = self.b, self.a + self.b
            yield self.a


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        Fibonacci(316)


if __name__ == '__main__':
    unittest.main()
