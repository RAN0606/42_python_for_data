from load_csv import load
import matplotlib.pyplot as plt


def clean_population(pop_str):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.
    Returns:
        float: population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def visulize_population():
    """
    Loads population data from a CSV file, processes and
    plots(used for creating line plots)
    the population comparison of two countries.
    """

    data = load("population_total.csv")
    countries = ["Belgium", "France"]
    colors = {"Belgium": "blue", "France": "green"}
    cutoff_year = 2050
    plt.figure(figsize=(10, 6))

    for country in countries:
        country_data = data[data['country'] == country].iloc[:, 1:]
        years = country_data.columns.astype(int)
        # Filter for years
        valid_years = years[years <= cutoff_year]
        population = [clean_population(
            country_data[str(year)].values[0]) for year in valid_years]
        plt.plot(
            valid_years, population, label=country, color=colors[country])

    plt.title("Population Projection (Up to 2040)")
    plt.xlabel("Year")
    plt.xticks(range(1800, cutoff_year + 1, 40))
    plt.xlim(1800, 2060)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()

    max_pop = max(max(population) for population in [population])
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


def main():
    visulize_population()


if __name__ == "__main__":
    main()
