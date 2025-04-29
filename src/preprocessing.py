
import pandas as pd
import numpy as np
from scipy import stats

def remove_roce_outliers(df, column='ROCE'):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    mask = ~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))

    z_scores = np.abs(stats.zscore(df[column]))
    mask &= (z_scores < 3)

    return df[mask]

def winsorize_series(series, lower_quantile=0.05, upper_quantile=0.95):
    lower = series.quantile(lower_quantile)
    upper = series.quantile(upper_quantile)
    return series.clip(lower, upper)
