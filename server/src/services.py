from coding import *


ALGORITHM_REGISTRY = [
    {"key": "golomb", "name": "Golomb"},
    {"key": "eliasgamma", "name": "Elias-Gamma"},
    {"key": "fib", "name": "Fibonacci/Zeckendorf"},
]


def create_coding(algorithm: str, params: dict) -> Coding:
    """" Factory method  """
    if algorithm == "golomb":
        return GolombCoding(**params)
    elif algorithm == "eliasgamma":
        return EliasGammaCoding()
    elif algorithm == "fib":
        return FibCoding()
    else:
        raise ValueError("Invalid coder algorithm")


def encode(text: str, coder: Coding) -> "codeword":
    return coder.encode(text)


def decode(codeword: str, coder: Coding) -> "text":
    return coder.decode(codeword)
