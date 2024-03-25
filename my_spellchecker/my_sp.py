import requests as r
import numpy as np
from Levenshtein import distance

#вынести эту херню в отдельный модуль, чтобы она не качала словарь каждый раз когда прога запускается
res = r.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
text = res.content.decode('cp1251')

with open('russian.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))

with open('russian.txt', encoding='utf-8') as file_in:
    dictionary = np.array([word.strip() for word in file_in.readlines()])

def get_candidates(user_word, dictionary):
    
    if len(user_word) == 1:
        print(f'Потеницальные кандидаты: {user_word} \nРасстояние Левенштейна = 0')
        return None
    
    distance_list = np.array([distance(user_word, word) for word in dictionary])
    lev_dist = distance_list.min()

    print(f'Потеницальные кандидаты: {dictionary[np.argwhere(distance_list == lev_dist)].T} \nРасстояние Левенштейна = {lev_dist}')

def get_words():
    user_document = input('Введите фразу: ')
    for user_word in user_document.split():
        get_candidates(user_word, dictionary)

print("Модуль my_spellchecker успешно подгружен")
