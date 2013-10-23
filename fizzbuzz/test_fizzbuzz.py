from fizzbuzz import fizzbuzz
def test_with_value_0 ():
    assert(fizzbuzz(0) == "fizzbuzz")

def test_with_value_1 ():
    assert(fizzbuzz(1) == "1")

def test_with_value_3 ():
    assert(fizzbuzz(3) == "fizz")

def test_with_value_5 ():
    assert(fizzbuzz(5) == "buzz")

def test_with_value_15 ():
    assert(fizzbuzz(15) == "fizzbuzz")

def test_with_value_100 ():
    assert(fizzbuzz(100) == "buzz")

def test_with_value_99 ():
    assert(fizzbuzz(99) == "fizz")

def test_with_fractions ():
    assert(fizzbuzz(0.3) == "0.3")

def test_with_hex_values ():
    assert(fizzbuzz(0x1) == "1")
    assert(fizzbuzz(0x3) == "fizz")
    assert(fizzbuzz(0x5) == "buzz")
    assert(fizzbuzz(0xF) == "fizzbuzz")

def test_with_octal_values ():
    assert(fizzbuzz(01) == "1")
    assert(fizzbuzz(03) == "fizz")
    assert(fizzbuzz(05) == "buzz")
    assert(fizzbuzz(015) == "13")
    assert(fizzbuzz(017) == "fizzbuzz")

def test_with_binarry_value ():
    assert(fizzbuzz(0b1) == "1")
    assert(fizzbuzz(0b11) == "fizz")
    assert(fizzbuzz(0b101) == "buzz")
    assert(fizzbuzz(0b1101) == "13")
    assert(fizzbuzz(0b1111) == "fizzbuzz")

