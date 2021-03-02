from fizzbuzz import fizzbuzz
import pytest

# put all the fizz buzz parameters into a decorator
# and avoid having to write assert over and over


@pytest.mark.parametrize("arg, ret", [
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16),
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret
