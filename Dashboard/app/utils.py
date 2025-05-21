# utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_paths):
    """
    Load and combine datasets into a single dictionary.

    Args:
        file_paths (dict): A dictionary with country names as keys and file paths as values.

    Returns:
        dict: A dictionary with country names as keys and combined DataFrames as values.
    """
    try:
        datasets = {}
        for country, file_path in file_paths.items():
            df = pd.read_csv(file_path)
            df["Country"] = country
            datasets[country] = df
        return datasets
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None


def plot_boxplot(dataframe, metric):
    """
    Generate a boxplot for the given metric.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        metric (str): The metric to be plotted (e.g., "GHI", "DNI", "DHI").

    Returns:
        plt.Figure: A matplotlib Figure object for the plot.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="Country", y=metric, data=dataframe, palette="viridis")
    plt.title(f"{metric} Comparison by Country")
    plt.xlabel("Country")
    plt.ylabel(metric)
    return plt


def generate_summary_table(dataframe):
    """
    Generate summary statistics: mean, median, and standard deviation by country.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: A summary table with statistics by country.
    """
    summary_stats = dataframe.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
    return summary_stats