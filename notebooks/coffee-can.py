import pandas as pd

# Load the CSV file with eligible stocks
file_path = "merged_cleaned_stock_data.csv"  # Update with the correct path if needed
df = pd.read_csv(file_path)

# Define thresholds for different decision categories
HIGH_DIVIDEND_MIN_PAYOUT = 0.30  # Favoring strong dividend payers
GROWTH_MIN_EARNINGS_GROWTH = 0.10  # High earnings growth threshold
STABLE_MIN_ROA = 0.10  # Minimum return on assets for stability
STABLE_MAX_BETA = 1.2  # Maximum beta for stability
VALUE_MIN_PAYOUT = 0.10  # Minimum payout ratio for value stocks
VALUE_MAX_PE = 20  # Maximum forward P/E ratio for value stocks

# Columns to consider
cols_to_consider = ["payoutRatio", "returnOnAssets", "earningsQuarterlyGrowth", "forwardPE", "marketCap", "beta"]

# Ensure necessary columns are numeric
df[cols_to_consider] = df[cols_to_consider].apply(pd.to_numeric, errors="coerce")


# Define a function to categorize stocks based on decision rules
def categorize_stock(stock):
    categories = []
    if pd.notna(stock["payoutRatio"]) and stock["payoutRatio"] > HIGH_DIVIDEND_MIN_PAYOUT:
        categories.append("High Dividend")
    if pd.notna(stock["earningsQuarterlyGrowth"]) and stock["earningsQuarterlyGrowth"] > GROWTH_MIN_EARNINGS_GROWTH:
        categories.append("Growth")
    if (pd.notna(stock["returnOnAssets"]) and stock["returnOnAssets"] > STABLE_MIN_ROA) or \
            (pd.notna(stock["beta"]) and stock["beta"] < STABLE_MAX_BETA):
        categories.append("Stable")
    if pd.notna(stock["payoutRatio"]) and pd.notna(stock["forwardPE"]) and stock["payoutRatio"] > VALUE_MIN_PAYOUT and \
            stock["forwardPE"] < VALUE_MAX_PE:
        categories.append("Value")

    return categories


# Apply the categorization function
df["Investment_Category"] = df.apply(categorize_stock, axis=1)

# Filter stocks based on the combined decision logic
selected_stocks = df[df["Investment_Category"].apply(
    lambda x: ("High Dividend" in x and "Value" in x) or ("Growth" in x and "Stable" in x)
)].copy()

# Save the selected stocks
selected_stocks.to_csv("selected_stocks2.csv", index=False)

print("Selection complete. Check 'selected_stocks.csv' for details.")
