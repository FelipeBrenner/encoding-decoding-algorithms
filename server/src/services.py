from coding import Encoding


def encode(text: str, encoding: Encoding) -> "codeword":
    return encoding.encode(text)


def decode(codeword: str, encoding: Encoding) -> "bits":
    return encoding.decode(codeword)
