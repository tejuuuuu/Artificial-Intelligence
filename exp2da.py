import pandas as pd
import numpy as np
import os
downloads_path = os.path.expanduser("~/Downloads/s.csv")
df = pd.read_csv(downloads_path)
df.describe()
subset_label = df.loc[:, ['sciences.grade', 'math.grade']]  
subset_positional = df.iloc[0:10, 0:2] 
aggregation = df.agg({'sciences.grade': ['sum', 'mean'],'math.grade': ['min', 'max'] })
grouped = df.groupby('english.grade').agg({'sciences.grade': 'sum', 'math.grade': 'mean' })
print(subset_label)
print(subset_positional)
print(aggregation)
print(grouped)