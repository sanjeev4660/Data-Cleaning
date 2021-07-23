import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("../input/earthquake-database/database.csv")

np.random.seed(0)
earthquakes['Date'].dtype
date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()
indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
earthquakes.loc[indices]
 earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")

q2.check()
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

 q3.check()
 sns.distplot(day_of_month_earthquakes.dropna(), kde=False, bins=31)
