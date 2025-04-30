import pandas as pd

# Load the dataset
file_path = "/Users/tamannasharma/Downloads/DATA_RAW - stock_info_k.csv"  # Update with actual file path
df = pd.read_csv(file_path)

# Selecting relevant features for Coffee Can Investing
selected_columns = [
    "symbol", "currentPrice", "marketCap", "fiftyTwoWeekRange", "twoHundredDayAverageChangePercent",
    "netIncomeToCommon", "revenueGrowth", "earningsQuarterlyGrowth", "totalRevenue", "enterpriseToRevenue",
    "returnOnAssets", "operatingCashflow", "grossMargins", "operatingMargins", "profitMargins", "freeCashflow",
    "debtToEquity", "totalDebt", "priceToBook", "forwardPE", "priceToSalesTrailing12Months",
    "enterpriseToEbitda", "beta", "shortPercentOfFloat", "heldPercentInstitutions", "heldPercentInsiders",
    "payoutRatio", "freeCashflow", "sharesOutstanding", "heldPercentInstitutions", "bookValue", "ebitda"
]

# Filtering only the selected columns
df = df[selected_columns]

# Handling missing values
# Fill missing numerical values with median to maintain distribution
#df.fillna(df.median(numeric_only=True), inplace=True)

# Handling categorical values (if any in the dataset)
df.dropna(subset=["symbol"], inplace=True)  # Ensure no missing stock symbols

# Removing duplicate entries if any
df.drop_duplicates(subset=["symbol"], keep="first", inplace=True)

# Save the cleaned data
df.to_csv("cleaned_stock_data11.csv", index=False)

print("Feature selection and data cleaning completed. Cleaned dataset saved as 'cleaned_stock_data.csv'.")