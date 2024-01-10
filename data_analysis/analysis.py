import os.path
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import parse_technologies

PATH_TO_DATA = "scrapped_data/python_all.csv"

OUTPUT_DIR = os.path.join("data_analysis", "output_plots", PATH_TO_DATA.split("/")[-1].replace(".csv", ""))
OUTPUT_DIR += "_" + datetime.now().strftime("%Y-%m-%d")


def get_technologies_plot(df):
    df['technologies'] = df['technologies'].apply(parse_technologies)

    all_technologies = [tech for sublist in df['technologies'] for tech in sublist]
    technology_counts = pd.Series(all_technologies).value_counts()

    plt.figure(figsize=(15, 8))
    technology_counts[:20].plot(kind="bar", color="skyblue", fontsize=10)
    plt.title("Popularity of Technologies")
    plt.xlabel("Technologies")
    plt.ylabel("Number of Vacancies")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/technologies")


def get_english_plot(df):
    plt.figure(figsize=(12, 6))

    df["english"].value_counts().sort_index().plot(kind="bar", color="skyblue")

    plt.title("Distribution of Vacancies by English Level")
    plt.xlabel("English Level")
    plt.ylabel("Number of Vacancies")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/english")


def get_employment_types(df):
    plt.figure(figsize=(10, 6))

    df["employment_type"].value_counts().plot(kind="pie", autopct="%1.1f%%")

    plt.title("Distribution of Vacancies by Employment Type")
    plt.ylabel("")
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/employment_types")


def get_top_companies(df):
    top_companies = df["company"].value_counts().nlargest(10)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_companies.values, y=top_companies.index, palette="viridis")
    plt.xlabel("Number of Vacancies")
    plt.ylabel("Company")
    plt.title("Top Companies with the Most Vacancies")

    plt.savefig(f"{OUTPUT_DIR}/top_companies")


def get_experience_distribution(df):
    plt.figure(figsize=(12, 6))
    df["years_of_experience"].value_counts().sort_index().plot(kind="bar", color="skyblue")
    plt.title(f"Distribution of Vacancies by Experience for Python Technology")
    plt.xlabel("Years of Experience")
    plt.ylabel("Number of Vacancies")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/experience_distribution_python.png")


def main():
    df = pd.read_csv(PATH_TO_DATA)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    get_technologies_plot(df)
    get_english_plot(df)
    get_employment_types(df)
    get_top_companies(df)
    get_experience_distribution(df)


if __name__ == "__main__":
    main()
