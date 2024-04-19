import random
import string
from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length
    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for _ in range (self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int =16, include_numbers: bool =False, include_symbols: bool =False):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
    
    def generate(self) -> str:
        allowed_chars = string.ascii_letters + (string.digits if self.include_numbers else "") + (string.punctuation if self.include_symbols else "")
        return ''.join([random.choice(allowed_chars) for _ in range (self.length)])

if __name__ == '__main__':
    pin_generator = PinGenerator(10)
    print(pin_generator.generate())
    
    pass_generator = RandomPasswordGenerator(12, True, True)
    print(pass_generator.generate())