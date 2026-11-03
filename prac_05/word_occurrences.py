"""
CP1404 Practical - Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""


def main():
    """Count word occurrences in user text and display aligned results."""
    text = input("Text: ")

    # Use key_to_value naming convention for dictionaries
    word_to_count = {}

    for word in text.split():
        # Using .get() for clean,dictionary updates
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Generator expression to calculate padding width
    longest_word_length = max((len(word) for word in word_to_count), default=0)

    # Display words alphabetically with aligned counts
    for word in sorted(word_to_count):
        print(f"{word:{longest_word_length}} : {word_to_count[word]}")


main()
