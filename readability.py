def count_letters(text):
    return sum(c.isalpha() for c in text)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    sentence_endings = ['.', '!', '?']
    return sum(text.count(end) for end in sentence_endings)

def main():
    text = input("Text: ")

    letter_count = count_letters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    L = (letter_count / word_count) * 100
    S = (sentence_count / word_count) * 100

    index = 0.0588 * L - 0.296 * S - 15.8

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")

if __name__ == "__main__":
    main()



