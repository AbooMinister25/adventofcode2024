import functools
import itertools


from aoc_lube import fetch, submit  # type: ignore


def parse_input(inp: str) -> list[list[int]]:
    return [[int(n) for n in lst.split()] for lst in inp.splitlines()]


def is_safe(report: list[int]) -> bool:
    differences = (a - b for a, b in itertools.pairwise(report))
    return all(0 < abs(i) < 4 for i in differences) and (
        report == sorted(report) or report == sorted(report, reverse=True)
    )


def part_1(inp: str) -> int:
    reports = parse_input(inp)
    return sum(is_safe(report) for report in reports)


def part_2(inp: str) -> int:
    reports = parse_input(inp)
    return sum(
        is_safe(report)
        or any(is_safe(list(c)) for c in itertools.combinations(report, len(report) - 1))
        for report in reports
    )


if __name__ == "__main__":
    raw_input = fetch(2024, 2)
    submit(2024, 2, 1, functools.partial(part_1, raw_input))
    submit(2024, 2, 2, functools.partial(part_2, raw_input))
