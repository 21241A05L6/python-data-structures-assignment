import math_utils
from math_utils import square

import string_utils

import shop_package.discount as disc
from shop_package.billing import calculate_total


print(math_utils.add(5, 3))
print(math_utils.subtract(10, 4))
print(square(6))


text = "hello python world"

print(string_utils.capitalize_words(text))
print(string_utils.reverse_string(text))
print(string_utils.word_count(text))


print(disc.apply_discount(1000, 10))
print(disc.flat_discount(500))


print(calculate_total([100, 200, 300]))