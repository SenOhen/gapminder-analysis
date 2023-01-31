# hw-gapminder

The assignment is comprised of the 4 questions below -- 2.5 points each.

### Data

This assignment uses a subset of the [gapminder dataset](https://www.gapminder.org/data/) 
that is available as "gapminder" in an [R package](https://cran.r-project.org/web/packages/gapminder/README.html).
The "gapminder" dataset in R is dataset available via `library(gapminder); gapminder` in R. 
Do not use the larger dataset that's available in R as "gapminder_unfiltered".
You can get a [text file](https://github.com/jennybc/gapminder#plain-text-delimited-files)
for the gapminder subset directly from the [jennybc github repo](https://github.com/jennybc/gapminder).
The easiest way to get the data into Python is from the text file: 
[gapminder.tsv](https://github.com/jennybc/gapminder/blob/main/inst/extdata/gapminder.tsv)

### Note: if seaborn hangs your mac terminal

For those of us using an older mac...

* For some reason (python not installed as a framework?), plt.show() with seaborn hangs my terminal.  
* Fix this by turning off interactive mode:
```
plt.ioff()
```
* You can also fix this by using a different backend:
```
matplotlib.use('TkAgg')
```
* List all the backends and the current backend with
```
print(plt.get_backend())
print(matplotlib.rcsetup.all_backends)
```
* Or you can add the following to `~/.zprofile` to avoid a hang with the default backend
```
# Avoids seaborn hang on my old macbook pro
export MPLBACKEND=qtagg
```

### FacetGrid

Use Seaborn's FacetGrid for this assignment...

* Seaborn overview
  * [Overview](https://seaborn.pydata.org/tutorial/function_overview.html) -- tutorial introduces “relational”, “distributional”, and “categorical” modules (plot types)
    * [seaborn.displot](https://seaborn.pydata.org/generated/seaborn.displot.html) API reference
  * Seaborn docs: [figure-level vs axes-level functions](https://seaborn.pydata.org/tutorial/function_overview.html)
* "Matplotlib offers good support for making figures with multiple axes"
  * "Seaborn builds on top of this to directly link the structure of the plot to the structure of your dataset."
  * [Mutiplot grids](https://seaborn.pydata.org/tutorial/axis_grids.html) tutorial
* FacetGrid is a seaborn class that enables "faceting"
  * "facet" (the verb) means to look simultaneously at the various dimensions ("facets", the noun) of your dataset
  * [seaborn.FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) API reference
  * Use the [FacetGrid.set()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set.html) method to set attributes on each of the subplot axes
  * [scatterplot with continuous hues & sizes](https://seaborn.pydata.org/examples/scatterplot_sizes.html) example
  * [FaceGrid.map_dataframe()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html) API reference

## Question 1 -- distribution of life expectancy by continent

Use histograms to visualize the distribution of life expectancy for each continent.
Briefly describe any features that seem significant. 
Make sure your plots are labeled and easy to read. 
Put all the plots in one figure with a title.
Look at the seaborn [FacetGrid API reference](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
for data-viz ideas.

## Question 2 -- time evolution of life expectancy by continent

For each continent, use box-and-whisker plots to visualize the time evolution of life expectancy by 
continent (i.e., for each year in the dataset from 1952 to 2007).
Comment briefly on the dominant features you see in the data.
As in Question 2, make sure your plots are labeled and easy to read, and put all the plots in one figure with a title.
Look at the seaborn [FacetGrid API reference](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
for ideas.

## Question 3 -- life expectancy vs GDP

Use scatter plots to visualize the relationship between life expectancy and GDP per capita for each continent.
Compare the use of linear and log scales for GDP. 
Comment on the relationships that seem significant and any outliers you notice.

## Question 4 -- PDF of life expectancy

* Overlay the normal (Gaussian) distribution on a normalized version of the histogram for the entire dataset.
* Include the KDE, which is discussed here: [Kernel Density Estimation](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation) -- pydata.org
* From ISLR2 p156: kernel density estimator is essentially a smoothed version of a histogram
* Consider using [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) -- scipy.org
* Comment briefly on the result (i.e., explain the dominant features in the chart with a few sentences).
  * Make sure to use the results in previous questions to justify your interpretation.
