import sys


def find_functions_without_comments(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    missing_comments = []
    for line_number, line in enumerate(lines):
        if line.startswith("def "):
            has_comment = line_number > 0 and lines[line_number - 1].startswith("#")
            if not has_comment:
                function_name = line[4:].split("(", 1)[0]
                missing_comments.append((function_name, line_number + 1))
    return missing_comments


def main():
    filenames = []
    arguments = sys.argv[1:]
    if not arguments:
        arguments = [input()]

    for argument in arguments:
        filenames.extend(filename.strip() for filename in argument.split(","))

    for filename in filenames:
        if not filename:
            continue
        try:
            missing_comments = find_functions_without_comments(filename)
        except OSError:
            print(f'Error reading file: "{filename}"')
            continue

        for function_name, line_number in missing_comments:
            print(
                f"File: {filename} contains a function "
                f"[{function_name}()] on line [{line_number}] "
                "without a preceding comment."
            )


if __name__ == "__main__":
    main()