DIGITS = '0123456789abcdef'


def convert_to_base(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)


print('\n########## Decimal --> Base ##########')
print("{} in base {} = {}".format(25, 2, convert_to_base(25, 2)))      # => '11001'
print("{} in base {} = {}".format(25, 16, convert_to_base(25, 16)))     # => '19'


# Return value of a char
# For example, 2 is returned for '2',
# 10 is returned for 'A',
# 11 for 'B'.
def char_value(character):
    if '0' <= character <= '9':
        return ord(character) - ord('0')
    else:
        return ord(character) - ord('A') + 10


def convert_to_decimal(str, base):
    num_length = len(str)
    power = 1  # Initialize power of base
    num = 0  # Initialize result

    # Decimal = str[len-1]*1 + str[len-2]*base + str[len-3]*(base^2) + ...
    for i in range(num_length - 1, -1, -1):

        # A digit in input number must be less than number's base
        if char_value(str[i]) >= base:
            print('Invalid Number')
            return -1
        num += char_value(str[i]) * power
        power = power * base
    return num


print('\n########## Base --> Decimal ##########')
print('{} in base {} is {} in decimal'.format('11001', 2, convert_to_decimal('11001', 2)))
print('{} in base {} is {} in decimal'.format('19', 16, convert_to_decimal('19', 16)))
