# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""
Cookiecutter script for generating the solution structure for each day.
"""

import argparse
import pathlib

PYTHON_FILE_TEMPLATE = """from aoc_lube import fetch, submit  # type: ignore


def part_1() -> None:
    ...


def part_2() -> None:
    ...


if __name__ == "__main__":
    raw_input = fetch(2024, {day})
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        "generator",
        description="Generates the structure for a specific day's advent of code solution.",
    )
    parser.add_argument("day", type=int)

    args = parser.parse_args()
    generate(args.day)


def generate(day: int) -> None:
    path = pathlib.Path(f"day{day}")
    python_path = path / "python"

    python_path.mkdir(parents=True, exist_ok=True)
    python_file_path = python_path / "main.py"

    with open(python_file_path, "w") as f:
        f.write(PYTHON_FILE_TEMPLATE.format(day=day))

    print("Generated structure.")


if __name__ == "__main__":
    main()
