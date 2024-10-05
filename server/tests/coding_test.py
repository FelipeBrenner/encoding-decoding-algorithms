import pytest
from coding import *


# EliasGammaCoding tests
@pytest.fixture
def elias_gamma():
    return EliasGammaCoding()

def test_encode_single_character_elias_gamma(elias_gamma):
    assert elias_gamma.encode('T') == '0000001010100'  # Binary representation of 'T' (84)
    assert elias_gamma.encode('e') == '0000001100101'  # Binary representation of 'e' (101)
    assert elias_gamma.encode('s') == '0000001110011'  # Binary representation of 's' (115)
    assert elias_gamma.encode('t') == '0000001110100'  # Binary representation of 't' (116)
    assert elias_gamma.encode(' ') == '00000100000'  # Binary representation of ' ' (32)
    assert elias_gamma.encode('!') == '00000100001'  # Binary representation of '!' (33)

def test_decode_single_character_elias_gamma(elias_gamma):
    assert elias_gamma.decode('0000001010100') == 'T'
    assert elias_gamma.decode('0000001100101') == 'e'
    assert elias_gamma.decode('0000001110011') == 's'
    assert elias_gamma.decode('0000001110100') == 't'
    assert elias_gamma.decode('00000100000') == ' '
    assert elias_gamma.decode('00000100001') == '!'

def test_encode_decode_round_trip_elias_gamma(elias_gamma):
    for char in ['T', 'e', 's', 't', ' ', '!']:
        encoded = elias_gamma.encode(char)
        decoded = elias_gamma.decode(encoded)
        assert decoded == char, f"Failed round-trip for {char}"

def test_encode_text_elias_gamma(elias_gamma):
    assert elias_gamma.encode('Test !') == '00000010101000000001100101000000111001100000011101000000010000000000100001'

def test_decode_codeword_elias_gamma(elias_gamma):
    assert elias_gamma.decode('00000010101000000001100101000000111001100000011101000000010000000000100001') == 'Test !'


# GolombCoding tests
@pytest.fixture
def golomb():
    return GolombCoding(8)

def test_encode_single_character_golomb(golomb):
    assert golomb.encode('T') == '00000000001100'  # Binary representation of 'T' (84)
    assert golomb.encode('e') == '0000000000001101'  # Binary representation of 'e' (101)
    assert golomb.encode('s') == '000000000000001011'  # Binary representation of 's' (115)
    assert golomb.encode('t') == '000000000000001100'  # Binary representation of 't' (116)
    assert golomb.encode(' ') == '00001000'  # Binary representation of ' ' (32)
    assert golomb.encode('!') == '00001001'  # Binary representation of '!' (33)

def test_decode_single_character_golomb(golomb):
    assert golomb.decode('00000000001100') == 'T'
    assert golomb.decode('0000000000001101') == 'e'
    assert golomb.decode('000000000000001011') == 's'
    assert golomb.decode('000000000000001100') == 't'
    assert golomb.decode('00001000') == ' '
    assert golomb.decode('00001001') == '!'

def test_encode_decode_round_trip_golomb(golomb):
    for char in ['T', 'e', 's', 't', ' ', '!']:
        encoded = golomb.encode(char)
        decoded = golomb.decode(encoded)
        assert decoded == char, f"Failed round-trip for {char}"

def test_encode_text_golomb(golomb):
    assert golomb.encode('Test !') == '0000000000110000000000000011010000000000000010110000000000000011000000100000001001'

def test_decode_codeword_golomb(golomb):
    assert golomb.decode('0000000000110000000000000011010000000000000010110000000000000011000000100000001001') == 'Test !'



# FibCoding tests
@pytest.fixture
def fib():
    return FibCoding()

def test_encode_single_character_fib(fib):
    assert fib.encode('T') == '0000101011'  # Binary representation of 'T' (84)
    assert fib.encode('e') == '10101000011'  # Binary representation of 'e' (101)
    assert fib.encode('s') == '00010010011'  # Binary representation of 's' (115)
    assert fib.encode('t') == '10010010011'  # Binary representation of 't' (116)
    assert fib.encode(' ') == '00101011'  # Binary representation of ' ' (32)
    assert fib.encode('!') == '10101011'  # Binary representation of '!' (33)

def test_decode_single_character_fib(fib):
    assert fib.decode('0000101011') == 'T'
    assert fib.decode('10101000011') == 'e'
    assert fib.decode('00010010011') == 's'
    assert fib.decode('10010010011') == 't'
    assert fib.decode('00101011') == ' '
    assert fib.decode('10101011') == '!'

def test_encode_decode_round_trip_fib(fib):
    for char in ['T', 'e', 's', 't', ' ', '!']:
        encoded = fib.encode(char)
        decoded = fib.decode(encoded)
        assert decoded == char, f"Failed round-trip for {char}"

def test_encode_text_fib(fib):
    assert fib.encode('Test !') == '00001010111010100001100010010011100100100110010101110101011'

def test_decode_codeword_fib(fib):
    assert fib.decode('00001010111010100001100010010011100100100110010101110101011') == 'Test !'
