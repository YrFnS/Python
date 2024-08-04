# Write a Python program to check whether an integer fits in 64 bits.

def in_64_bits(n):
    return n.bit_length() <= 63 and n >= -(2**63)

print(in_64_bits(2**63))
