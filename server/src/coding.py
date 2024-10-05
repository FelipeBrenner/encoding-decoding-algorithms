from typing import Protocol
import math


class Coding(Protocol):

    def encode(symbol):
        raise NotImplementedError

    def decode(codeword):
        raise NotImplementedError


class EliasGammaCoding:
    # - Elias-Gamma Encoding
    # Prefix = max(2**N) lower than decimal symbol
    # Stopbit = 1
    # Suffix = rest as binary, same len as prefix filled with 0

    def __init__(self):
        self.stopbit = '1'

    def encode(self, text: str) -> "codeword":
        encoded_text = []
        for symbol in text:
            encoded_text.append(self._encode(symbol))
        return ''.join(encoded_text)

    def decode(self, codeword: "bits") -> str:
        decoded_text = []
        p = 0
        while p < len(codeword):
            # Find the stop bit
            sbidx = codeword.index(self.stopbit, p)
            prefix_len = sbidx - p

            # Get the prefix and suffix
            prefix = codeword[p:sbidx]
            sufstart = sbidx + 1
            final = sufstart + prefix_len
            suffix = codeword[sufstart:final]

            # Decode the character and add to result
            decoded_char = chr(2**len(prefix) + int(suffix, 2))
            decoded_text.append(decoded_char)

            # Move pointer to the next symbol in the encoded text
            p = final

        return ''.join(decoded_text)

    def _encode(self, symbol: str) -> str:
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

    def _decode(self, bits: str) -> str:
        bi = bits.index(self.stopbit)
        final = len(bits)
        prefix = bits[:bi]
        suffix = bits[bi+1:final]
        return chr( 2**len(prefix) + int(suffix, 2) )


class GolombCoding:
    # Prefix = quotient number of zeros
    # Stopbit = 1
    # Suffix = rest as binary

    def __init__(self, k=None):
        if k is None or not k:
            raise ValueError("Parameter 'k' required for Golomb coding")
        if (math.ceil(math.log2(k)) == math.floor(math.log2(k))) is False:
            raise ValueError("Parameter 'k' must be a power of 2")
        self.k = k
        self.stopbit = '1'

    @property
    def suffix_size(self):
        return int( math.log2(self.k) )

    def encode(self, text: str) -> "codeword":
        encoded_text = []
        for symbol in text:
            encoded_text.append(self._encode(symbol))
        return ''.join(encoded_text)

    def decode(self, codeword: "bits") -> str:
        decoded_text = []
        p = 0
        while p < len(codeword):
            # Find the stop bit
            sbidx = codeword.index(self.stopbit, p)

            # Get the prefix and suffix
            prefix = codeword[p:sbidx]
            sufstart = sbidx + 1
            final = sufstart + self.suffix_size
            suffix = codeword[sufstart:final]

            # Decode the character and add to result
            decoded_char = chr( len(prefix) * self.k + int(suffix, 2) )
            decoded_text.append(decoded_char)

            # Move pointer to the next symbol in the encoded text
            p = final
        return ''.join(decoded_text)

    def _encode(self, symbol: str) -> "bits":
        d = ord(symbol)
        return '0' * (d // self.k) + self.stopbit + format(d % self.k, f'0{self.suffix_size}b')  # prefix + stopbit + suffix (format as binary, with leading zeros)

    def _decode(self, bits: str) -> str:
        bi = bits.index(self.stopbit)
        final = len(bits)
        prefix = bits[:bi]
        suffix = bits[bi+1:final]
        return chr( len(prefix) * self.k + int(suffix, 2) )


class FibCoding:

    def __init__(self):
        self.stopbit = '1'

    def encode(self, text: str) -> "codeword":
        encoded_text = []
        for symbol in text:
            encoded_text.append(self._encode(symbol))
        return ''.join(encoded_text)

    def decode(self, codeword: "bits") -> int:
        decoded_text = []
        p = 0
        while p < len(codeword):
            bits: str = self._find_next_bits(codeword[p:])

            # Decode the character and add to result
            decoded_char = self._decode(bits)
            decoded_text.append(decoded_char)

            # Move pointer to the next symbol in the encoded text
            p += len(bits)
        return ''.join(decoded_text)

    def _find_next_bits(self, codeword) -> "bits":
        bits = ""
        for b1, b2 in zip(codeword, codeword[1:]):
            if b1 == '1' and b2 == '1':
                bits += b1
                bits += b2
                return bits
            bits += b1
        return bits

    def _encode(self, symbol: str) -> "bits":
        d = ord(symbol)

        seq = self._gen_fib_until(d)
        bits = ['0'] * len(seq)

        _total = 0
        for i, v in enumerate(seq[-1::-1]):
            if _total + v <= d:
                _total += v
                bits[-1-i] = '1'
                if _total == d:
                    break
        return ''.join(bits) + self.stopbit

    def _decode(self, bits: str) -> str:
        seq = self._gen_fib_len(len(bits))
        d = 0
        bits = list(bits)
        for i, v in enumerate(seq):
            if bits[i] == '1':
                d += v
        return chr(d)

    def _gen_fib_until(self, d) -> list[int]:
        """ generates fibonacci sequence until it reached a decimal 'd' """
        seq = []
        last: int = 1
        next: int = 1
        while next < d:
            seq.append(next)
            last, next = next, last + next
        return seq

    def _gen_fib_len(self, n) -> list[int]:
        """ generates fibonacci sequence of length 'n' """
        seq = []
        last: int = 1
        next: int = 1
        for _ in range(1, n):
            seq.append(next)
            last, next = next, last + next
        return seq
