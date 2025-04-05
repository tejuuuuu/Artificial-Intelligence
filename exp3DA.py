import numpy as np
import statistics as stats
data = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2, 2, 3, 1, 1, 2]
mean = np.mean(data)
std_dev = np.std(data)
z_scores = [float((x - mean) / std_dev) for x in data]
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print(f"Z-scores: {z_scores}")
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print(f"Q1 (25th percentile): {q1}")
print(f"Q1 (50th percentile): {q2}")
print(f"Q3 (75th percentile): {q3}")
print(f"Interquartile Range (IQR): {iqr}")
threshold = 1.5
outliers = [x for x in data if abs((x - mean) / std_dev) > threshold]
print(f"Outliers based on Z-score threshold of {threshold}: {outliers}")
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
iqr_outliers = [x for x in data if x < lower_bound or x > upper_bound]
print(f"Outliers based on IQR method: {iqr_outliers}")
 