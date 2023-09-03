import string

def word_frequency(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        # Remove punctuation and make the word lowercase
        cleaned_word = word.strip(string.punctuation).lower()

        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    return word_count

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
