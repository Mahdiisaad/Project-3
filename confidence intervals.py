import pandas as pa
import numpy as np
import seaborn as sns
import sys
import matplotlib.pyplot as plt
from scipy import stats

df = pa.read_csv(r'C:\Users\User\Desktop\Python\data2.csv')
# print(df.head())
dat = df.CWDistance.mean()
std = df.CWDistance.std()
n = len(df)
t = 2.064
"""we use it when n < 30"""
t2 = 1.96
""" we use it when n >= 30"""
calc_for_interval1 = dat - t * (std / np.sqrt(n))
calc_for_interval2 = dat + t * (std / np.sqrt(n))
print(calc_for_interval1, calc_for_interval2)


dt = pa.read_csv(r'C:\Users\User\Desktop\Python\data.csv')
dt["gender"] = dt.RIAGENDR.replace({1: "Male", 2: "Female"})

dt["smokin"] = dt.SMQ020.replace({1: "Yes", 2: "No", 7: np.nan, 9: np.nan})

dx = dt[["smokin", "gender"]].dropna()

print(pa.crosstab(dx.smokin, dx.gender))
"""this is to make the data showen as array"""


dx["smokin"] = dx.smokin.replace({"Yes": 1, "No": 0})

dz = dx.groupby("gender").agg({"smokin": [np.mean, np.size, np.std]})
dz.columns = ["Proportion", "Total n", "std"]
print(dz)
"""we did the replacement again, because we want to know the Mean by numbers in order to calculate P value"""

p1 = 0.304845
p2 = 0.513258
n1 = 2972
n2 = 2753
std1 = 0.460419
std2 = 0.499915
standard_error_for_both_Pop = np.sqrt(
    (p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
print(standard_error_for_both_Pop)
""" these steps only to calculate the SE, for both genders compined"""

p_value1 = p1 - p2 + 1.96 * standard_error_for_both_Pop
p_value2 = p1 - p2 - 1.96 * standard_error_for_both_Pop

print(p_value1, p_value2)
""" this means we are 95% confidence that difference in two "POPULATION PROPORTION" are -0.18 and -0.23"""

standard_error_for_both_Means = np.sqrt(
    (std1**2 / n1) + (std2**2 / n2))
print(standard_error_for_both_Means)
mean_value1 = p1 - p2 + 1.96 * standard_error_for_both_Means
mean_value2 = p1 - p2 - 1.96 * standard_error_for_both_Means
print(mean_value1, mean_value2)
""" this means we are 95% confidence that difference in two "Means" are -0.18 and -0.23"""
"""both ideas can be used to calculate p value """
