import sys


def print_first_ten_lines(filename):
    try:
        with open(filename, "r") as file:
            for _ in range(10):
                line = file.readline()
                if not line:
                    break
                print(line, end="")
    except OSError:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    print_first_ten_lines(sys.argv[1])