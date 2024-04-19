import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length

    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 16, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols

    def generate(self) -> str:
        allowed_chars = string.ascii_letters + \
            (string.digits if self.include_numbers else "") + \
            (string.punctuation if self.include_symbols else "")
        return ''.join([random.choice(allowed_chars) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, separator: str = "-", num_of_words: int = 4, capitalize: bool = True, vocabulary: list = None):

        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()

        self.separator = separator
        self.num_of_words = num_of_words
        self.capitalize = capitalize

    def generate(self) -> str:
        password_words = [random.choice(self.vocabulary)
                          for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice(
                [True, False]) else word.lower() for word in password_words]
        return self.separator.join(password_words)


if __name__ == '__main__':
    pin_generator = PinGenerator(10)
    print(pin_generator.generate())

    pass_generator = RandomPasswordGenerator(12, True, True)
    print(pass_generator.generate())

    mem_generator = MemorablePasswordGenerator(num_of_words=4)
    print(mem_generator.generate())
