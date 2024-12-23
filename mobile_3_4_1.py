def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем каждое слово из переданного набора
    for word in other_words:
        # Проверяем наличие корня в слове без учета регистра
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():

            # Если корень найден, добавляем слово в список
            same_words.append(word)

    # Возвращаем сформированный список
    return same_words
# Вызываем функцию и выводим результат
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)