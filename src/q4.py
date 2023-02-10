import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

#ax = plt.subplots()
plt.figure(figsize=(11,6))
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
ax = plt.plot(x,norm.pdf(x))
sns.histplot(data=gapminderdf, x="lifeExp")
sns.displot(data=gapminderdf, x="lifeExp", kind="kde")
plt.show()