import pandas as pd
import numpy as np

sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

np.random.seed(0) 
tot_cells= np.product(sf_permits.shape)
tot_miss=sf_permits.isnull().sum().sum()
percent_missing = (tot_miss/tot_cells)*100
sf_permits.dropna()
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

dropped_columns = sf_permits.shape[1]-sf_permits_with_na_dropped.shape[1]
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)
