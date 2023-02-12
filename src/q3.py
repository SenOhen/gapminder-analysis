import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from gapmindercode import gapminderdf, Africadf, Asiadf, Europedf, Americasdf, Oceaniadf

# Visualizing life expectancy vs GDP per capita (linear scale)
fig = plt.figure()
graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.scatterplot,'gdpPercap', 'lifeExp')
graph.fig.subplots_adjust(top=0.85)
graph.fig.suptitle("Life Expectancy vs GDP by Continent (Linear Scale)")
graph.set(ylim=(0,90))
plt.savefig("figs/LE_vs_GDPpercapita_linear_scale.png")

# Visualizing life expectancy vs GDP per capita (log scale)
fig = plt.figure()
graph = sns.FacetGrid(gapminderdf, col='continent')
graph.map(sns.scatterplot,'gdpPercap', 'lifeExp')
plt.xscale("log")
graph.fig.subplots_adjust(top=0.85)
graph.fig.suptitle("Life Expectancy vs GDP by Continent (Log Scale)")
graph.set(ylim=(0,90))
plt.savefig("figs/LE_vs_GDPpercapita_log_scale.png")