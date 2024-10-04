import numpy as np
import random
def main():
    m = np.random.default_rng()
    m = m.integers(1, 11, (4, 4))
    print(m)
main()