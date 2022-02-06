# About this folder

After lauchinhg the [**Portuguese Legislative Elections's Media Monitor**](https://jorgemiguelgomes.github.io/LEG2022_MediaMonitor/) I've downloaded a larger dataset. 
Instead of treating the data again using Google Sheets - the process used to write the first report - I decided to use Python scripts to treat the data, and produce the graphics that can be used in the report.

# The Dashboard

The idea to produce a dashboard was born from the fact that we are producing a dashboard for VOST Portugal, and this looked like the perfect use case to test DASH's capabilities. 

# The APPS folder

The following python scripts can be found in the **apps** folder
1. filter.py - filters the rawdatasets by the media outlet chosen and produces a graph for each candidate as well as the resulting .csv file
2. aggregator.py - takes all datasets from **filter.py** and aggregates them into a unique dataset, adding a column with candidate name
3. percentstacked.py - calculates percentages from the total values, based on the dataset produced with **aggregator.py**
4. dashboard.py - a simple DASH app  dashboard with a dropdown that uses the dataset produced with **percentstacked.py**
5. tabs.py - a DASH app that includes three tabs using the dataset produced with **percentstacked.py** as well as the dataset from **aggregator.py**

* * *

<img width="1787" alt="tabs.py" src="https://user-images.githubusercontent.com/34355337/152694189-fc8d6177-398f-4279-9168-76afb2fc9128.png">
