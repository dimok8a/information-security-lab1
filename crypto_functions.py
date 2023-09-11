import string


# Шифрование текста
def encrypt_text(text, horizontal_count, vertical_count):
    encrypted_text = ""
    for i in range(horizontal_count):
        for j in range(vertical_count):
            if i + j * horizontal_count < len(text):
                encrypted_text += text[i + j * horizontal_count]
            else:
                encrypted_text += " "
    # Лишние пробелы из начала и конца обрезаем
    return encrypted_text.strip()


# Расшифровка текста
def decrypt_text(encrypted_text: str, horizontal_count: int, vertical_count: int):
    decrypted_text = ""
    for i in range(vertical_count):
        for j in range(horizontal_count):
            if i + j * vertical_count < len(encrypted_text):
                decrypted_text += encrypted_text[i + j * vertical_count]
    # Лишние пробелы из начала и конца обрезаем
    return decrypted_text.strip()


# Используется для очищения текста от знаков препинания
punctuation_dict = {}
for i in range(len(string.punctuation)):
    punctuation_dict[string.punctuation[i]] = ""
table = str.maketrans(punctuation_dict)


# Удаление знаков препинания из текста
def strip_punctuation(text):
    return text.translate(table)


# Возвращает массив всех найденных в словаре (russian.txt) слов, встреченных в тексте decrypted_text
def get_text_words(decrypted_text: str):
    all_text_words = []
    text_words = strip_punctuation(decrypted_text.lower()).split(" ")
    with open("russian.txt", "r") as file1:
        for line in file1:
            word = line.strip().lower()
            if text_words.count(word) > 0:
                all_text_words.extend([word] * text_words.count(word))
    return all_text_words


# Проверяет, содержит ли массив text_words столько же букв, сколько и в тексте decrypted_text
def does_words_contain_all_letters(text_words, decrypted_text):
    text_words_letter_count = 0
    decrypted_text_letter_count = 0
    # Считаем буквы в массиве слов
    for word in text_words:
        text_words_letter_count += len(word)
    # Считаем буквы в тексте
    for letter in decrypted_text:
        if letter.isalpha():
            decrypted_text_letter_count += 1
    if text_words_letter_count == decrypted_text_letter_count:
        return True
    return False


def hack_text(encrypted_text: str):
    decrypted_text = ""
    max_words_count = 0
    text_words_variants = {}
    # Перебираем все варианты формы "бруска"
    for i in range(1, len(encrypted_text) + 1):
        for j in range(1, len(encrypted_text) + 1):
            if len(encrypted_text) <= i * j:
                # Расшифровываем текст с i буквами в строки и j в столбце
                decrypted_text_check = decrypt_text(encrypted_text, i, j)
                # Если еще не было такой "расшифровки"
                if not (decrypted_text_check in text_words_variants):
                    # Получаем все слова текста
                    text_words = get_text_words(decrypted_text_check)
                    # Если все буквы слов покрывают текст
                    if does_words_contain_all_letters(text_words, decrypted_text_check):
                        return decrypted_text_check
                    # Записываем в dict
                    text_words_variants[decrypted_text_check] = text_words
    # Проверяем словарь. Ищем вариант с максимальных кол-вом слов в тексте
    for text, text_words in text_words_variants.items():
        if len(text_words) > max_words_count:
            max_words_count = len(text_words)
            decrypted_text = text
    return decrypted_text
