"""
Text Processing Utility for Manuscript Analysis

This program analyzes and manipulates multi-line manuscript text.
It demonstrates:
- Advanced string operations
- Text statistics computation
- Title formatting with linguistic rules
- Quote extraction
- Symbol replacement with word equivalents
"""

import re


# Multi-line manuscript text (3+ paragraphs, 500+ characters)
manuscript = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. "Ut enim ad minim veniam",
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum. The editor said,
"This section needs revision," but no changes were made.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta sunt explicabo & analyzed
at 100% accuracy. Another note read "Check formatting here.
"""


def word_stats(text):
    """
    Analyze text and return statistics.

    Returns:
        dict: {
            total_characters,
            total_words,
            total_sentences,
            average_word_length
        }
    """
    # Total characters (including spaces)
    total_characters = len(text)

    # Normalize whitespace and split into words
    words = text.split()
    total_words = len(words)

    # Remove non-letter characters from words for length calculation
    clean_words = [re.sub(r"[^A-Za-z]", "", word) for word in words]
    clean_words = [word for word in clean_words if word]

    # Sentence split using punctuation
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    total_sentences = len(sentences)

    # Average word length
    if clean_words:
        avg_word_length = sum(len(word) for word in clean_words) / len(clean_words)
    else:
        avg_word_length = 0.0

    return {
        "total_characters": total_characters,
        "total_words": total_words,
        "total_sentences": total_sentences,
        "average_word_length": round(avg_word_length, 2),
    }


def format_title(title):
    """
    Convert a string to title case, excluding certain words unless first.

    Excluded words:
    - Articles: a, an, the
    - Conjunctions: and, but, or
    - Prepositions: in, on, at
    """
    excluded = {"a", "an", "the", "and", "but", "or", "in", "on", "at"}
    words = title.lower().split()

    formatted_words = []
    for index, word in enumerate(words):
        if index == 0 or word not in excluded:
            formatted_words.append(word.capitalize())
        else:
            formatted_words.append(word)

    return " ".join(formatted_words)


def find_quotes(text):
    """
    Extract all text enclosed in double quotes.

    Returns:
        list: Quoted strings in order of appearance.
    """
    quotes = []
    in_quote = False
    current = ""

    for char in text:
        if char == '"':
            if in_quote:
                quotes.append(current)
                current = ""
                in_quote = False
            else:
                in_quote = True
        elif in_quote:
            current += char

    return quotes


def replace_symbols(text):
    """
    Replace symbols with word equivalents:
    @ -> at
    & -> and
    % -> percent

    Preserves capitalization where applicable.
    """
    replacements = {
        "@": "at",
        "&": "and",
        "%": "percent",
    }

    for symbol, word in replacements.items():
        text = text.replace(symbol, word)

    return text


def main():
    """Demonstrate text processing features."""
    print("\n--- Word Statistics ---")
    stats = word_stats(manuscript)
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title():<25}: {value}")

    print("\n--- Title Formatting ---")
    sample_title = "the rise and fall of an empire in history"
    print("Original :", sample_title)
    print("Formatted:", format_title(sample_title))

    print("\n--- Extracted Quotes ---")
    quotes = find_quotes(manuscript)
    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote}")

    print("\n--- Symbol Replacement ---")
    replaced_text = replace_symbols(manuscript)
    print(replaced_text[:300], "...\n")  # Preview first 300 chars


if __name__ == "__main__":
    main()
