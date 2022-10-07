class BasicWord:
    def __init__(self, full_word, subs_words):
        self.full_word = full_word
        self.subs_words = subs_words

    def get_is_correct(self, user_answer):
        """возвращает bool при проверке слова в списке допустимых подслов"""
        return user_answer in self.subs_words

    def get_count_sub_words(self):
        """возвращает int после подсчета количества подслов"""
        return len(self.subs_words)
