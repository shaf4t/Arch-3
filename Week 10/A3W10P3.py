def find_longest_words(filename):
    with open(filename, "r") as file:
        words = file.read().split()

    if not words:
        return 0, []

    longest_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == longest_length]
    return longest_length, longest_words


def main():
    filename = input().strip()
    try:
        longest_length, longest_words = find_longest_words(filename)
    except OSError:
        print(f'Error reading file: "{filename}"')
        return

    print(f"Length of longest word(s) is [{longest_length}] chars")
    print("These are all the words of that length:")
    print(", ".join(longest_words))


if __name__ == "__main__":
    main()