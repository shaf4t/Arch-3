import os
import sys


def tail_option_one(filename):
    with open(filename, "r") as file:
        return file.readlines()[-10:]


def tail_option_two(filename):
    with open(filename, "r") as file:
        line_count = sum(1 for _ in file)

    last_lines = []
    with open(filename, "r") as file:
        for line_number, line in enumerate(file):
            if line_number >= line_count - 10:
                last_lines.append(line)
    return last_lines


def tail_option_three(filename):
    last_lines = []
    with open(filename, "r") as file:
        for line in file:
            last_lines.append(line)
            if len(last_lines) > 10:
                last_lines.pop(0)
    return last_lines


def measure_performance(filename):
    timings = {}
    for name, option in (
        ("option_one", tail_option_one),
        ("option_two", tail_option_two),
        ("option_three", tail_option_three),
    ):
        start = os.times().elapsed
        option(filename)
        timings[name] = os.times().elapsed - start
    return timings


def print_tail(filename):
    for line in tail_option_three(filename):
        print(line, end="")


def main():
    try:
        print_tail(sys.argv[1])
    except OSError:
        print(f'Error reading file: "{sys.argv[1]}"')


if __name__ == "__main__":
    main()