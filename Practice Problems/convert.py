def convert(base_10_number, new_base):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base_10_number < new_base:
        return convert_string[base_10_number]
    else:
        return convert(base_10_number // new_base, new_base) + convert_string[base_10_number % new_base]


print(convert(100, 10))
print(convert(100, 2))
print(convert(100, 36))

# print(unconvert("100", 10))
# print(unconvert("1100100", 2))
# print(unconvert("2S", 36))