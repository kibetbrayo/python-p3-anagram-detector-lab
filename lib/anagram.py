# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, other_words):
        anagram = []
        for word in other_words:
            if sorted(word.lower()) == sorted(self.word.lower()) and word.lower() != self.word.lower():
                anagram.append(word)
        return anagram