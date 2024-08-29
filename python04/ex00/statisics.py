def ft_statistics(*args: any, **kwargs: any) -> None:
    values = []
    for arg in args:
        values.append(arg)
    values.sort()

    def meanfuc(sortelist: tuple) -> float:
        try:
            mean = sum(args)/len(args)
            print(f"mean: {mean}")
            return mean
        except Exception:
            print("ERROR")

    def medianfuc(sortelist: tuple) -> float:
        try:
            lenth = len(args)
            indexmedian = lenth // 2
            if lenth % 2 == 0:
                medi = (
                    sortelist[indexmedian - 1] + sortelist[indexmedian]) / 2
            else:
                medi = sortelist[indexmedian]
            print(f"median: {medi}")
            return (medi)
        except Exception:
            print("ERROR")

    def quartfuc(sortelist: tuple) -> list:
        try:
            q1_index = len(sortelist) // 4
            q3_index = q1_index * 3
            quartl = [float(sortelist[q1_index]), float(sortelist[q3_index])]
            print(f"quartile: {quartl}")
            return quartl
        except Exception:
            print("ERROR")

    def varfunc(values: any) -> float:
        try:
            mean = sum(values)/len(values)
            variance_total = 0
            for value in values:
                variance_total += (value - mean) ** 2

            variance = variance_total / len(values)
            print(f"var: {variance}")
            return (variance)
        except Exception:
            print("ERROR")

    def stdvarfunc(values: any) -> float:
        try:
            mean = sum(values)/len(values)
            variance_total = 0
            for value in values:
                variance_total += (value - mean) ** 2
            stdvariance = (variance_total / len(values)) ** 0.5
            print(f"std: {stdvariance}")
            return (stdvariance)
        except Exception:
            print("ERROR")

    for value in kwargs.values():
        if value == "mean":
            meanfuc(values)
        elif value == "median":
            medianfuc(values)
        elif value == "quartile":
            quartfuc(values)
        elif value == "var":
            varfunc(values)
        elif value == "std":
            stdvarfunc(values)


def main():
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
