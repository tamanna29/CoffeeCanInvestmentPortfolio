# ☕ AI Coffee Can Investment Strategy & Portfolio Optimization

## Overview
This project implements an **AI-driven Coffee Can investment strategy** by selecting fundamentally strong stocks using financial metrics, machine learning classification, and portfolio optimization techniques.

We aim to simulate a **long-term, passive investment approach** where selected stocks are held for at least 10 years without selling — optimizing the portfolio using **Mean-Variance Optimization (MVO)** to maximize returns while balancing risk.

---

## Agenda
- 📈 **Stock Classification** (Eligible vs Non-Eligible)
- 📚 **Coffee Can Strategy Overview**
- 📊 **Data Collection and Feature Engineering**
- 🛠 **Portfolio Optimization**
- 🔍 **Challenges and Future Work**

---

## Coffee Can Strategy
> Pick high-quality stocks based on fundamentals and hold them passively for a decade.

Using financial health indicators like **ROCE, Gross Margins, Revenue Growth,** and **Debt-to-Equity**, the system identifies promising stocks aligned with Coffee Can principles. 

---

## Data Overview
- **Sources**: NASDAQ Stock Screener, `yfinance`
- **Stock Universe**: ~1200 companies across Large, Mid, and Small Caps
- **Key Features**:
  - Return on Capital Employed (**ROCE**)
  - **Gross Margins**
  - **Revenue Growth**
  - **Debt-to-Equity Ratio**
  - **Free Cash Flow**
  - **Earnings Growth**

**Eligibility Criteria** (must meet at least 3 out of 4):
- Top 30% ROCE
- Top 40% Gross Margins
- Above Median Revenue Growth
- Bottom 40% Debt-to-Equity

---

## Methodology

### Data Preprocessing
- Outlier Removal: IQR method for ROCE
- Winsorization: Debt-to-Equity and Revenue Growth
- Missing Data: Filled using medians

### Stock Classification
- **Scoring system** based on financial thresholds
- **Random Forest Classifier** for predicting eligibility
  - SMOTE for class imbalance
  - StandardScaler for feature scaling
  - Achieved **96% weighted F1-score**

### Portfolio Optimization
- Applied **Mean-Variance Optimization** on eligible stocks
- Constructed an efficient portfolio maximizing **Sharpe Ratio**
- Built a **Covariance Matrix** for asset returns

---

## Challenges and Future Work
- ⚙️ Improve macroeconomic factor consideration
- 🧹 Enhance data aggregation and cleaning pipelines
- 📈 Explore advanced portfolio construction techniques (beyond MVO)
- 🔄 Implement dynamic rebalancing strategies

---

## Project Structure
```plaintext
coffee_can_po_24/
│
├── data/                  # Raw input data (e.g., stock financials)
├── src/                   # Python modules
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   └── __init__.py
├── notebooks/             # Final Jupyter notebook
│   └── Coffee_Can_PO_24.ipynb
├── README.md              # Project documentation
├── requirements.txt       # Python libraries
└── .gitignore             # Files/folders to ignore in GitHub
```

---

## Tech Stack
- **Python** (pandas, numpy, scikit-learn, scipy, matplotlib, seaborn)
- **Machine Learning**: Random Forest, SMOTE
- **Optimization**: Mean-Variance (MVO) - Portfolio Theory

---

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/coffee_can_po_24.git
cd coffee_can_po_24
pip install -r requirements.txt
```

---

## Authors
- **Kopal Bhatnagar**
- **Tamanna Sharma**

---

## License
This project is for educational and research purposes only.  
Not financial advice. 📈🚀

---

# 🚀 Let's build AI-powered investment tools for smarter long-term decisions!
