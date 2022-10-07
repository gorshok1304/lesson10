class Question:
    def __init__(self, text, complexity, correct_answer):
        self.text = text
        self.complexity = complexity
        self.correct_answer = correct_answer

        self.is_ask = False
        self.user_answer = None
        self.points = self.complexity * 10


    def get_points(self):
        return self.points


    def is_correct(self):
        return self.user_answer == self.correct_answer



    def build_question(self):
        return f"Вопрос: {self.text}"



    def build_positive_feedback(self):
        return f"Ответ верный, получено {self.points} баллов"



    def build_negative_feedback(self):
        return f"Ответ неверный, верный ответ {self.correct_answer}"





