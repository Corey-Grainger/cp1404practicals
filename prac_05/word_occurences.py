"""CP1404 Week 5 Prac
Word Occurrences Program
Estimated: 25 minutes
Actual: 15 minutes"""

string = input("Text: ").lower()
words = string.split()
words.sort()
words_to_characters_in_word = {}
for word in words:
    try:
        words_to_characters_in_word[word] += 1
    except KeyError:
        words_to_characters_in_word[word] = 1
longest_word_length = max((len(word) for word in words))
for word, count in words_to_characters_in_word.items():
    print(f"{word:{longest_word_length}} : {count}")
