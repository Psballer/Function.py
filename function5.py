def string_of_words(text):
    for word in text:
        if len(word) % 2 == 1:
            return word
