import pandas as pd


def load(filepath: str) -> pd.DataFrame:
    try:
        load_data = pd.read_csv(filepath)
        return (load_data)
    except Exception as e:
        print("Error:", e)


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
