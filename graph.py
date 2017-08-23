import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Training_Dataset.csv")

m = ((df["mvar32"] + df["mvar33"] + df["mvar34"] + df["mvar35"]) * (1.0)) / (4 * 1.0)

supp = df["mvar46"]
elit = df["mvar47"]
cred = df["mvar48"]

me = df["mvar38"]

plt.plot(me, me, 'ro')
plt.show()
