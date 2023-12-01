"""CP1404 Week 5 Prac
Word Occurrences Program
Estimated: 25 minutes
Actual: 15 minutes"""

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

string = input("Text: ").lower()
for character in string:
    if character in SPECIAL_CHARACTERS:
        string = string.replace(character, '')
words = string.split()
words.sort()
words_to_count = {}
for word in words:
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1
longest_word_length = max((len(word) for word in words))
for word, count in words_to_count.items():
    print(f"{word:{longest_word_length}} : {count}")
