import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.boxplot, "year", "lifeExp")
plt.ylim(0,90)
plt.savefig("figs/time_evolution_LE_by_continent.png")