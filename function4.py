def list_of_words(words):
    longest = max(words, key=len)
    return longest, len(longest)

words = ['out', 'weather', 'mobile', 'breakfast', 'journey']
longest_word, word_length = list_of_words(words)
print(f"{longest_word}, {word_length}")
 
