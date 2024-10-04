import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nums = (8, 6, 15, 20)
sounds = {"cow":"moo","dog":"woof","pig":"oink","cat":"meow"}
prices = np.array([80, 10, 40, 2.5])


farm = list(zip(nums, sounds, prices))

rows = ["cow", "dog", "pig", "cat"]
cols = ['nums', 'sounds', 'prices']

df = pd.DataFrame(farm, index=rows, columns=cols)
print(df)

