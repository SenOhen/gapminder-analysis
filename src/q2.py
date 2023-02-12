import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

# Visualizing time evolution of life expectancy by continent
graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.boxplot, "year", "lifeExp")

#Making space for figure title, and setting axis parameters
graph.fig.subplots_adjust(top=0.85)
graph.fig.suptitle("Time Evolution of Life Expectancy by Continent")
graph.set(ylim=(0,90))

plt.savefig("figs/time_evolution_LE_by_continent.png")