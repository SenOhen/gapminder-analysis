import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv"

gapminderdf = pd.read_table(url)

#print(gapminderdf.head())

sns.histplot(data=gapminderdf, x='continent', y='lifeExp')
plt.show()