def vowel_count(word):
    vowels = "aeiou"

    count = 0

    for w in word.lower():
        if w in word:
            count += ord(w)

    return count


def sort_words_by_vowels(words):
    return sorted(words, key=lambda word:(len(word), vowel_count(word)))

words = ["sky", "aeiou", "test", "Apple", "rhythm"]
print(sort_words_by_vowels(words))