import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

fig, ax = plt.subplots(1,1)
#plt.figure(figsize=(11,6))
xdata = gapminderdf['lifeExp']
x = np.linspace(min(xdata), max(xdata), 100)
ax.plot(x,norm.pdf(x,np.mean(xdata),np.std(xdata)), c="red")
sns.histplot(data=gapminderdf, x="lifeExp", ax=ax, kde=True)
plt.savefig("figs/PDF_of_LE.png")
#plt.show()