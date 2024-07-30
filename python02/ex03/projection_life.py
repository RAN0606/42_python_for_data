from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads data: Gross National Product per capita
    and life expectancy from separate CSV files.
    Create a new figure to visualize the scatter plot

    Generate a scatter plot with GNP on
    the x-axis and life expectancy on the y-axis
    """
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")
    merged_data = income_data[["1900"]].join(life_expectancy_data[
        ["1900"]], lsuffix='_gnp', rsuffix='_life_expectancy')

    # Drop rows with missing data
    merged_data.dropna(inplace=True)

    gnp_1900 = merged_data["1900" + '_gnp']
    life_expectancy_1900 = merged_data["1900" + '_life_expectancy']
    plt.figure(figsize=(8, 6))
    plt.scatter(gnp_1900, life_expectancy_1900)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
