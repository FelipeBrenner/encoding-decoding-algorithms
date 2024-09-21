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

    def decode(self, codeword) -> str:
        bi = codeword.index(self.stopbit)
        final = len(codeword)
        prefix = codeword[:bi]
        suffix = codeword[bi+1:final]
        return chr( 2**len(prefix) + int(suffix, 2) )

class GolombEncoding:

    def __init__(self):
        self.k = 8
        self.stopbit = '1'

    def encode(self, symbol) -> str:
        d = ord(symbol)
        return '0' * (d // self.k) + self.stopbit + format(d % self.k, 'b')  # prefix + stopbit + suffix

    def decode(self, codeword) -> str:
        bi = codeword.index(self.stopbit)
        final = len(codeword)
        prefix = codeword[:bi]
        suffix = codeword[bi+1:final]
        return chr( len(prefix) * self.k + int(suffix, 2) )
    
class FibEncoding:

    def __init__(self):
        self.stopbit = '1'

    def encode(self, symbol) -> str:
        d = ord(symbol)

        seq = self._gen_fib_d(d)
        bits = ['0'] * len(seq)

        _total = 0
        for i, v in enumerate(seq[-1::-1]):
            if _total + v <= d:
                _total += v
                bits[-1-i] = '1'
                if _total == d:
                    break
        return ''.join(bits) + self.stopbit

    def decode(self, codeword) -> int:
        seq = self._gen_fib_n(len(codeword))
        d = 0
        bits = list(codeword)
        for i, v in enumerate(seq):
            if bits[i] == '1':
                d += v
        return chr(d)
    
    def _gen_fib_d(self, d) -> list[int]:
        seq = []
        last: int = 1
        next: int = 1
        while next < d:
            seq.append(next)
            last, next = next, last + next
        return seq

    def _gen_fib_n(self, n) -> list[int]:
        seq = []
        last: int = 1
        next: int = 1
        for _ in range(1, n):
            seq.append(next)
            last, next = next, last + next
        return seq