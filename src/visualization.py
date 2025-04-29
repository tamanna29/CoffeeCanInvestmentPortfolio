
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column, title="Distribution Plot"):
    plt.figure(figsize=(10,6))
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.show()
