import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

fig = plt.figure()
graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.scatterplot,'gdpPercap', 'lifeExp')
plt.xscale("log")

plt.savefig("figs/LE_vs_GDPpercapita.png")