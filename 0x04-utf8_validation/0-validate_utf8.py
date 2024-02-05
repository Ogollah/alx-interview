#!/usr/bin/python3
'''UTF- validation module
'''


def validUTF8(data):
    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    n = len(data)
    i = 0

    while i < n:
        current_byte = data[i]

        if (not isinstance(current_byte, int)
                or current_byte < 0 or current_byte > 0x10ffff):
            return False
        elif current_byte <= 0x7f:
            i += 1
        elif current_byte & 0b11111000 == 0b11110000:
            span = 4
        elif current_byte & 0b11110000 == 0b11100000:
            span = 3
        elif current_byte & 0b11100000 == 0b11000000:
            span = 2
        else:
            return False

        if n - i >= span:
            next_bytes = data[i + 1: i + span]
            if not all(is_continuation_byte(byte) for byte in next_bytes):
                return False
            i += span
        else:
            return False

    return True
