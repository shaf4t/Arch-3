def remove_comments(line):
    quote = None
    escaped = False

    for position, character in enumerate(line):
        if escaped:
            escaped = False
        elif character == "\\" and quote is not None:
            escaped = True
        elif character in ("'", '"'):
            if quote is None:
                quote = character
            elif quote == character:
                quote = None
        elif character == "#" and quote is None:
            line_ending = line[len(line.rstrip("\r\n")):]
            return line[:position] + line_ending

    return line


def main():
    input_filename = input("File to read: ").strip()
    output_filename = input("File to save: ").strip()

    try:
        with open(input_filename, "r") as input_file:
            cleaned_lines = [remove_comments(line) for line in input_file]
        with open(output_filename, "w") as output_file:
            output_file.writelines(cleaned_lines)
    except OSError:
        print(f'Error reading file: "{input_filename}"')


if __name__ == "__main__":
    main()