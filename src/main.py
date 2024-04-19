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

if __name__ == '__main__':
    pin_generator = PinGenerator(10)
    print(pin_generator.generate())