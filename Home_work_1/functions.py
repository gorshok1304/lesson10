import random

def get_words(filenames):
    with open(filenames, 'r') as f:
        words = f.read().splitlines()
    return words

def shuffle_char_in_word(word):
    word_lisr = list(word)
    random.shuffle(word_lisr)
    return ''.join(word_lisr)

def save_user_result_to_history(user_name, points):
    with open('history.txt', 'a') as f:
        f.write(f"{user_name} {points}\n")

def print_statics():
    with open('history.txt', 'r') as f:
        data = f.read().splitlines()

        total_count_game = len(data)
        points_list = list()

        for note in data:
            print(note)
            user_name, points = note.split(' ')
            points_list.append(points)

        max_record = max(points_list)

        print(f"Всего игр сыграно: {total_count_game}")
        print( f"Максимальный рекорд: {max_record}")
