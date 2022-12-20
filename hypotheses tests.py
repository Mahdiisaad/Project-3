import statsmodels.api as sm
import numpy as np
import pandas as pd
import scipy.stats.distributions as dist

# Research Question
# ""One Population Proportion""
# In previous years 52% of parents believed that electronics and social media was the cause of
# their teenager’s lack of sleep. Do more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media?

# Population: Parents with a teenager (age 13-18)
# Parameter of Interest: p
# Null Hypothesis: p = 0.52
# Alternative Hypthosis: p > 0.52 (note that this is a one-sided test)

# 1018 Parents

# 56% believe that their teenager’s lack of sleep is caused due to electronics and social media.
n = 1018
phat1 = .52
phat2 = 0.56
test_statistics = sm.stats.proportions_ztest(
    phat2 * n, n, phat1, alternative='larger', prop_var=0.52)
print(test_statistics)
"""look at the above quistion, this is a way to calculate both, test statistics and P value, because normal calculations
will not make iit easy to find P value """
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# Difference in Population Proportions
# Research Question
# Is there a significant difference between the population proportions of parents of black children
# and parents of Hispanic children who report that their child has had some swimming lessons?

# Populations: All parents of black children age 6-18 and all parents of Hispanic children age 6-18
# Parameter of Interest: p1 - p2, where p1 = black and p2 = hispanic
# Null Hypothesis: p1 - p2 = 0
# Alternative Hypthosis: p1 - p2  ≠  = 0
# 91 out of 247 (36.8%) sampled parents of black children report that their child has had some swimming lessons.
# 120 out of 308 (38.9%) sampled parents of Hispanic children report that their child has had some swimming lessons.

n1 = 247
p_hat1 = 0.37
n2 = 308
p_hat2 = 0.39
""" you can easily calculate the test statistics by the next equation, but you will need another
equation to get the P-Value """
se = np.sqrt((p_hat1 * (1 - p_hat1) / n1) + (p_hat2 * (1 - p_hat2) / n2))
test_stat = (p_hat2 - p_hat1) / se
print(test_stat)
""" there is a lot of functions to calculate p value, learn about them more"""
pvalue = 2 * dist.norm.cdf(-np.abs(test_stat))
print(pvalue)

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# One Population Mean
# Research Question
# Is the average cartwheel distance (in inches) for adults more than 80 inches?

# Population: All adults
# Parameter of Interest:  μ , population mean cartwheel distance.
# Null Hypothesis: μ = 80 Alternative Hypthosis: μ > 80

# 25 Adults


df = pd.read_csv(r'C:\Users\User\Desktop\Python\data2.csv')
""" there is two way to calculate from file, the first one is here"""
n_ = len(df)
mean = df.CWDistance.mean()
hypoth_mean = 80
std = df.CWDistance.std()

standar_err = std / np.sqrt(n_)
test_sta = (mean - hypoth_mean) / standar_err
print(test_sta)
pvaluee = dist.norm.cdf(-np.abs(test_sta))
print(pvaluee)
""" or there is another way with only one equation"""
test_and_pvalue = sm.stats.ztest(
    df["CWDistance"], value=80, alternative="larger")
print(test_and_pvalue)

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# Difference in Population Means
# Research Question
# Considering adults in the NHANES data, do males have a significantly higher mean Body Mass Index than females?

# Population: Adults in the NHANES data.
# Parameter of Interest:  μ1−μ2 , Body Mass Index.
# Null Hypothesis:  μ1=μ2
# Alternative Hypthosis:  μ1≠μ2

# 2976 Females
# μ1=29.94
# σ1=7.75

# 2759 Male Adults
# μ2=28.78
# σ2=6.25

# μ1−μ2=1.16

dt = pd.read_csv(r'C:\Users\User\Desktop\Python\data.csv')

females = dt[dt["RIAGENDR"] == 2]
males = dt[dt["RIAGENDR"] == 1]

females_n = len(females)
females_mean = females.BMXBMI.mean()
females_std = females.BMXBMI.std()


males_n = len(males)
males_mean = males.BMXBMI.mean()
males_std = males.BMXBMI.std()

""" we have two approaches to calculate test statistics, the first one """

standr_err = np.sqrt(((females_std**2) / females_n) +
                     ((males_std**2) / males_n))
test_st = (females_mean - males_mean) / standr_err
print(test_st)
p_value = 2 * dist.norm.cdf(-np.abs(test_st))
print(p_value)
""" the other way will have different evaluations, i have checked for 1 hour and i think there
is something messing i cant catch

here is the second approach"""

teststat_and_pvalue = sm.stats.ztest(
    females["BMXBMI"].dropna(), males["BMXBMI"].dropna())
print(teststat_and_pvalue)
