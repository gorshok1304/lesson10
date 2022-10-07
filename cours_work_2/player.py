class Player():
    def __init__(self, name):
        self.name = name
        self.user_words = []

    def get_name(self):
        return self.name

    def get_user_words_count(self):
        return len(self.user_words)

    def is_word_used(self, word):
        return word in self.user_words

    def add_word(self, word):
        self.user_words.append(word)
