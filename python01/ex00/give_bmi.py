import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    import numpy as np
    arH = np.array(height)
    arW = np.array(weight)
    return (np.divide(weight, np.power(height, 2)).tolist)
    

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    import numpy as np
    aBmi = np.array(bmi)
    return (aBmi > limit)


def main():
    import numpy as np
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()