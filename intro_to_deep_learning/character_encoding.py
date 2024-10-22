import pandas as pd
import numpy as np

import charset_normalizer

np.random.seed(0)

before = "This is the Dollar symbol: $"

type(before)

after = before.encode("utf-8", errors="replace")

type(after)

after

print(after.decode("utf-8"))

# Try to decode our bytes with the ASCII encoding
print(after.decode("ascii"))
