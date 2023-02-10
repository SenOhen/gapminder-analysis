import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

fig = plt.figure()
graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.histplot, 'lifeExp')
#sns.histplot(data=gapminderdf, x='continent', y='lifeExp')
plt.ylim(0,90)
#plt.title("Distribution of Life Expectancy by Continent")
plt.savefig("figs/distribution_LE_by_continent.png")