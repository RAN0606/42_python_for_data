def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    function for calculate mean, median, quarts
    and variance and std variance of the given numbers
    """
    values = []
    for arg in args:
        values.append(arg)
    values.sort()

    def meanfuc(sortelist: tuple) -> float:
        """
        inner function for calculating mean
        """

        try:
            mean = sum(args)/len(args)
            print(f"mean: {mean}")
            return mean
        except Exception:
            print("ERROR")

    def medianfuc(sortelist: tuple) -> float:
        """
        inner function for calculating median
        """
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
        """
        inner function for calculating a list of quart
        """
        try:
            q1_index = len(sortelist) // 4
            q3_index = q1_index * 3
            quartl = [float(sortelist[q1_index]), float(sortelist[q3_index])]
            print(f"quartile: {quartl}")
            return quartl
        except Exception:
            print("ERROR")

    def varfunc(values: any) -> float:
        """
        inner function for calculating variance
        """
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
        """
        inner function for calculating std variance
        """

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
