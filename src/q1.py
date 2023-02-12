import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

# Visualizing life expectancy distibution by continent
graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.histplot, 'lifeExp')

# Making space for figure title, and setting axis parameters
graph.fig.subplots_adjust(top=0.8)
graph.fig.suptitle("Distribution of Life Expectancy by Continent")
graph.set(ylim=(0,90))

plt.savefig("figs/distribution_LE_by_continent.png")