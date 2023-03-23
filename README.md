# Demographics are Destiny

_Analysis of Global Demographics_

**Motivation**: I'm deeply interested in understanding the future, and seeing what's coming.
Few areas of analysis are as predictive and close to deterministic as demographics.


## Generations

What generation are you part of? Run `python generations.py`, put in your year of birth and be told.


## Aspects of demographic analysis:

### Data Sources

https://population.un.org/wpp/


**Data:**

* Population replacement rate is `2.1`.
* Working age is defined by `wa_min = 18`, `wa_max = 65`, where current values are set by widely accepted definition.

* Population age data is a list of population counts `[male, female]` by year of birth.
* Populaiton fertility rate is a historical time series `[....,fr_i,...]` up to and including the current year.
* Relevant population summary stats include: 
	* % working age supporting under working age,
	* % working age supporting over working age.

### Data Processing

Before visualization, we need several prepped data items.


### Data Projection

* Projections consist of:
	* for any given year after the current one, a list of population counts male/female for each bucket;
	* for any given year before the current one, the number of women times the fertility rate.

### Data Visualization

Using either `plotly` or `matplotlib`.
