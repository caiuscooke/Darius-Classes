# its bringing in functions and other objects that aren't available by default

import random
print()  # available by default
# randint() # not available by default

# random library/module

random.randint()  # now we've imported it

random_integer = random.randint(0, 100)
random_decimals = random.randint(1, 100)
random_decimal = random_decimals / 100
random_float = random_integer + random_decimal
