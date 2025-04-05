import pandas as pd
import numpy as np
import os
downloads_path = os.path.expanduser("~/Downloads/robo.csv")
df = pd.read_csv(downloads_path)
average_conversations = df['Interaction_Count'].mean()
print(f"Average daily conversations: {average_conversations}")
max_energy_consumption = df['Energy_Consumption (kWh)'].max()
min_energy_consumption = df['Energy_Consumption (kWh)'].min()
print(f"Maximum energy consumption: {max_energy_consumption}")
print(f"Minimum energy consumption: {min_energy_consumption}")
total_steps = df['Steps_Walked'].sum()
print(f"Total steps walked: {total_steps}")

