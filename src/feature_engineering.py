
import pandas as pd

def calculate_growth(df, column, periods=5):
    return (df[column] - df[column].shift(periods)) / df[column].shift(periods)

def add_financial_ratios(df):
    df['debt_to_equity'] = df['TotalDebt'] / df['Equity']
    df['profit_margin'] = df['NetIncome'] / df['Revenue']
    return df
