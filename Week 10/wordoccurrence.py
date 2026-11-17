PUNCTUATION_CHARACTERS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def normalize_word(word):
    return word.strip().strip(PUNCTUATION_CHARACTERS).lower()


def find_word_frequencies(filename):
    frequencies = {}
    with open(filename, "r") as file:
        for line in file:
            for word in line.split(" "):
                normalized_word = normalize_word(word)
                if normalized_word:
                    frequencies[normalized_word] = (
                        frequencies.get(normalized_word, 0) + 1
                    )
    return frequencies


def find_most_and_least_frequent(filename):
    frequencies = find_word_frequencies(filename)
    if not frequencies:
        return [], []

    highest_frequency = max(frequencies.values())
    lowest_frequency = min(frequencies.values())
    most_frequent = [
        word for word, count in frequencies.items() if count == highest_frequency
    ]
    least_frequent = [
        word for word, count in frequencies.items() if count == lowest_frequency
    ]
    return most_frequent, least_frequent


def main():
    filename = input().strip()
    try:
        most_frequent, least_frequent = find_most_and_least_frequent(filename)
    except OSError:
        print(f'Error reading file: "{filename}"')
        return

    print(f"Most: {most_frequent}")
    print(f"Least: {least_frequent}")


if __name__ == "__main__":
    main()