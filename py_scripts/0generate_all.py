import random

def make_line(comment, inputs, output, cycles):
    return ";".join([comment, ','.join(inputs), output, cycles]) + "\n"

def number_to_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join(str(x) for x in digits[::-1])

def generate_all(from_base, to_base):
    for n in range(0, from_base ** 3):
        if random.random() < 0.05:
            i = number_to_base(n, from_base)
            o = number_to_base(n, to_base)
            if len(o)>3:
                break
            yield (i, o)


cycles = input("Cycles: ")
with open("baseconverter_testall.txt", "w") as f:
    for from_base in range(2, 11):
        for to_base in range(2, 11):
            for (inp, output) in generate_all(from_base, to_base):
                f.write(make_line("From base {0} to base {1}".format(from_base, to_base), [str(inp), str(from_base), str(to_base)], output, cycles))
