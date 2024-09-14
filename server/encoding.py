from typing import Protocol


class Encoding(Protocol):

    def encode(symbol):
        raise NotImplementedError

    def decode(codeword):
        raise NotImplementedError



# - Elias-Gamma Encoding
# Prefix = max(2**N) lower than decimal symbol
# Stopbit = 1
# Suffix = rest as binary, same len as prefix filled with 0
class EliasGammaEncoding:

    def __init__(self):
        self.stopbit = '1'

    def encode(self, symbol) -> str:
        d = ord(symbol)

        for i, j in zip(range(d), range(d)[1:]):
            if 2**j > d:
                N = i
                rest = d - 2**i

                prefix = '0' * N
                suffix = format(rest, 'b')
                _fill = '0' * (len(prefix) - len(suffix))
                suffix = _fill + suffix
                return prefix + self.stopbit + suffix

        raise ValueError(f"Could not encode symbol: {symbol}")

    def decode(self, codeword) -> int:
        bi = codeword.index(self.stopbit)
        final = len(codeword)
        prefix = codeword[:bi]
        suffix = codeword[bi+1:final]
        return chr( 2**len(prefix) + int(suffix, 2) )
