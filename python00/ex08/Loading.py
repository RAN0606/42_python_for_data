import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, item in enumerate(lst, start=1):
        completion = i / total
        progress = int(105 * completion)
        bar = f"{'=' * progress}{' ' * (105 - progress)}"
        output = f"{int(completion * 100):3}%|{bar}| {i}/{total}\r"
        if (i % 20 == 0 or i == total):
            sys.stdout.write(output)
        yield item
    sys.stdout.write("\n")
