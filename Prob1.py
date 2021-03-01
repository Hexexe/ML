import numpy as np
import re

def generate(p1):
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    return len(re.findall("(?=11111)", "".join(map(str, seq))))

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
