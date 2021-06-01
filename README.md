# Python Programming in the Geosciences

This is a two-part (morning and afternoon) interactive workshop
on using the Python programming language in the geosciences
to perform data analysis and visualization.
The workshop is a part of the [RECCS][reccs] program at CU Boulder.

This workshop will not teach the details of Python--others have done this (see "Resources" below),
and it takes more time than we have.
The goal of this workshop is to show how working geoscientists
use some of the plentiful scientific libraries available in Python.


## Instructors

* [Mark Piper](https://instaar.colorado.edu/people/mark-piper/)
* Jeffrey Schmidt


## Requirements

* Computer
* Web browser
* Internet access
* Coffee (optional, but recommended)


## Agenda

The workshop is divided into morning and afternoon sessions.

### Morning

The morning session runs from 9 am until noon,
with a break around the midpoint.
It covers more basic concepts,
but people with experience using Python
can join and help those with less experience.

*Topics:*

* Introductions
* Why Python?
* Logging in to the CSDMS JupyterHub
* Using Jupyter Notebook
* Python fundamentals
* Importing Python libraries
* Reading data from a csv file with *pandas*
* Plotting data with *matplotlib*
* Saving work to a PDF file
* Exercises and discussion

:arrow_forward: [Run the workshop material on the CSDMS JupyterHub][nbgitpuller-link]

### Afternoon

The afternoon session runs from 1 pm until 4 pm,
with a break around the midpoint.
It covers more advanced topics.

*Topics:*

* Introductions
* Loops, conditionals, `try` statement, functions
* Reading data from a NetCDF file with *scipy*
* Analyzing and visualizing data with *Basemap* and *matplotlib*
* Saving work to a PDF file
* Exercises and discussion

:arrow_forward: [Run the workshop material on the CSDMS JupyterHub][nbgitpuller-link]


## Resources

Python:
* [Software Carpentry][swc], especially the [Programming with Python][swc-python] lesson
* [Data Carpentry][dc]
* The official [Python tutorial][python-tutorial] is somewhat advanced, but has a lot of information
* The [TutorialsPoint Python tutorial][tp-tutorial] is also well done, and perhaps easier to follow
* When I have a Python question, usually someone on [Stack Overflow][stack-overflow] has an answer

CU Boulder:
* [Community Surface Dynamics Modeling System (CSDMS)][csdms]
* [Cooperative Institute for Research in Environmental Sciences (CIRES)][cires]
* [EarthLab][earthlab]
* [Earth Surface Processes Institute (ESPIn)][espin] summer school


## Acknowledgments

CSDMS is supported by the National Science Foundation
under Award No. [1831623][csdms-award],
*Community Facility Support: The Community Surface Dynamics Modeling System (CSDMS)*.

Portions of the Python language fundamentals section were derived
from material that is copyright Software Carpentry
and remixed under their [license][swc-license].

NEON (National Ecological Observatory Network). 2D wind speed and direction
(DP1.00001.001). https://data.neonscience.org (accessed May 26, 2021)

20th Century Reanalysis V2 data provided by the NOAA/OAR/ESRL PSL, Boulder, Colorado, USA,
from their website at https://psl.noaa.gov/data/gridded/data.20thC_ReanV2.html.

<!-- Links -->

[cires]: https://cires.colorado.edu/
[csdms]: http://csdms.colorado.edu
[csdms-award]: https://nsf.gov/awardsearch/showAward?AWD_ID=1831623
[dc]: https://datacarpentry.org/
[earthlab]: https://earthlab.colorado.edu/
[espin]: https://github.com/csdms/espin
[nbgitpuller-link]: https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Freccs-2021&urlpath=tree%2Freccs-2021%2Fnotebooks%2F0_overview.ipynb&branch=main
[python-tutorial]: https://docs.python.org/3/tutorial/
[reccs]: https://cires.colorado.edu/outreach/reccs
[swc]: https://software-carpentry.org/
[swc-license]: https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/LICENSE.md
[swc-python]: https://swcarpentry.github.io/python-novice-inflammation/
[stack-overflow]: https://stackoverflow.com/
[tp-tutorial]: https://www.tutorialspoint.com/python/index.htm
