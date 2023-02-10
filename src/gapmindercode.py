import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv"

gapminderdf = pd.read_table(url)
continents = ['Africa', 'Europe', 'Asia', 'Americas', 'Oceania']
for item in continents:
   str = item + "df"
   globals()[str] = gapminderdf[gapminderdf['continent']==item]
   #setattr(self,name,value)

# Africadf = gapminderdf[gapminderdf['continent']=='Africa']
# Europedf = gapminderdf[gapminderdf['continent']=='Europe']
# Asiadf = gapminderdf[gapminderdf['continent']=='Asia']
# Americasdf = gapminderdf[gapminderdf['continent']=='Americas']
# Oceaniadf = gapminderdf[gapminderdf['continent']=='Oceania']
#print(gapminderdf.head())
#print(Europedf.head())