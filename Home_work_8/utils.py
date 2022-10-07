import json
from question import Question

PATH = 'questions.json'


def load_data(path=PATH):
    with open(path, "r", encoding="utf8") as file:
        return json.load(file)


def load_questions(path=PATH):
    questions_data = load_data(path)
    questions = []

    for questions_data in questions_data:
        q = Question(
            questions_data["q"],
            questions_data["d"],
            questions_data["a"],
        )
        questions.append(questions)

    return questions


print("Игра начинается!")
