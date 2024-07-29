from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load("life_expectancy_years.csv")
    df_france = df[df['country'] == 'France']
    years = df_france.columns[1:]
    values = df_france.values[0][1:]
    plt.plot(years, values)
    plt.title('France life Expectancy Over the Years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    # plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()