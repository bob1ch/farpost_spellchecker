from spellchecker import SpellChecker

spell = SpellChecker(language='ru')

def get_words():
    user_document = input('Введите фразу: ').split()
    res = list()
    for word in user_document:
        word_correction = spell.correction(word)
        print('исходное слово -> исправленное')
        print(f'{word} -> {word_correction}')
        res.append(word_correction)
    
    if len(res) == 1:
        print(*res)
        return
        
    print(' '.join(res))
        
        