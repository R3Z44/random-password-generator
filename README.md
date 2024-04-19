# Password Generator

This Python code provides a simple password generator along with specific types of password generators. It utilizes the `random` and `string` libraries along with the Natural Language Toolkit (`nltk`) for generating passwords.

## Usage

To use this code, make sure you have Python installed on your system along with the required `nltk` data.

### Dependencies

- Python 3.x
- nltk

You can install `nltk` and download the necessary data by running:

```bash
pip install nltk
python -m nltk.downloader words
```

### Running the Code

To generate passwords, you can simply run the script. It will demonstrate the usage of different types of password generators.

```bash
python password_generator.py
```

## Classes

### `PasswordGenerator` (Abstract Base Class)

- Abstract base class for password generators.
- Defines an abstract method `generate()`.

### `PinGenerator`

- Generates numeric PIN codes of a specified length.

#### Parameters
- `length`: Length of the PIN code to generate.

### `RandomPasswordGenerator`

- Generates random passwords with options to include numbers and symbols.

#### Parameters
- `length`: Length of the password (default: 16).
- `include_numbers`: Boolean indicating whether to include numbers in the password (default: False).
- `include_symbols`: Boolean indicating whether to include symbols in the password (default: False).

### `MemorablePasswordGenerator`

- Generates memorable passwords using random words from a vocabulary.

#### Parameters
- `separator`: Separator character between words (default: "-").
- `num_of_words`: Number of words in the password (default: 4).
- `capitalize`: Boolean indicating whether to capitalize random words (default: True).
- `vocabulary`: List of words to choose from (default: English words from `nltk`).

## Example

```python
if __name__ == '__main__':
    # Generate PIN
    pin_generator = PinGenerator(10)
    print(pin_generator.generate())

    # Generate random password
    pass_generator = RandomPasswordGenerator(12, True, True)
    print(pass_generator.generate())

    # Generate memorable password
    mem_generator = MemorablePasswordGenerator(num_of_words=4)
    print(mem_generator.generate())
```

This script will output a randomly generated PIN, a random password with numbers and symbols, and a memorable password consisting of random words.
