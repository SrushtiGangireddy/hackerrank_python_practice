def print_formatted(number):
    final_binary_width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(' '.join(map(lambda x: x.rjust(final_binary_width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))
