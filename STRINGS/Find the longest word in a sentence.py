sentence="hello my name is tanishk."
def longest_word(sentence):
    words=sentence.split()
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
print(longest_word(sentence))
