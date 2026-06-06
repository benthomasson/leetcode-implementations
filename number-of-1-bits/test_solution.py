from solution import hamming_weight


def test_example_1():
    assert hamming_weight(0b00000000000000000000000000001011) == 3


def test_example_2():
    assert hamming_weight(0b00000000000000000000000010000000) == 1


def test_example_3():
    assert hamming_weight(0b11111111111111111111111111111101) == 31


def test_zero():
    assert hamming_weight(0) == 0


def test_one():
    assert hamming_weight(1) == 1


def test_all_ones():
    assert hamming_weight(0xFFFFFFFF) == 32


def test_power_of_two():
    assert hamming_weight(1 << 16) == 1


def test_alternating_bits():
    assert hamming_weight(0xAAAAAAAA) == 16
