from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    print("The shape is: ", df.shape)
    print(df)


if __name__ == "__main__":
    main()
