from player import Player
from utils import load_random_word
from basic_word import BasicWord


print(f"введите имя игрока")
user_input = input()
player = Player(user_input)

game_word = load_random_word()


print(f"Привет {player.get_name()}!")
print(f"Составьте {len(game_word.full_word)} слов из слова {game_word.full_word}")
print(f"Слова должны быть не короче 3 букв\n"
      f"Чтобы закончить игру, угадайте все слова или напишите stop\n"
      f"Поехали, ваше первое слово?")

count = 0

while count < len(game_word.subs_words):
    user_word = input().lower()
    if game_word.get_is_correct(user_word):
        print("Верно")
        player.add_word(user_word)
        count += 1
    elif user_word == "stop":
        break
    else:
        print("не верно")

print(f"слова закончились, игра завершена!\n"
      f"вы угадали {player.get_user_words_count()} слов!")



