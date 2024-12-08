import functools
from aoc_lube import fetch, submit  # type: ignore


def part_1(inp: str) -> int:
    numbers = [int(i) for i in inp.split()]
    return sum([abs(a - b) for a, b in zip(sorted(numbers[::2]), sorted(numbers[1::2]))])


def part_2(inp: str) -> int:
    numbers = [int(i) for i in inp.split()]
    second_col = numbers[1::2]

    return sum(i * second_col.count(i) for i in numbers[::2])


if __name__ == "__main__":
    raw_input = fetch(2024, 1)
    submit(2024, 1, 1, functools.partial(part_1, raw_input))
    submit(2024, 1, 2, functools.partial(part_2, raw_input))
