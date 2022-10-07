import functions

def main():
    name = input("Введите ваше имя: ")

    words = functions.get_words("words.txt")
    points_counter = 0

    for word in words:
        shufled_word = functions.shuffle_char_in_word(word)

        user_answer = input(f"Угадайте слово: {shufled_word}")
        user_answer = input("Ваш ответ: ")
        user_answer = user_answer.lower()

    if user_answer == word:
        print("Верно! Вы получаете 10 очков")
        points_counter += 10
    else:
        print(f"Неверно! Верный ответ – {word}")

    functions.save_user_result_to_history(name, points_counter)

    functions. print_statics()

if __name__=="__main__":
    main()