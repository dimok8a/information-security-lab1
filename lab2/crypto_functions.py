ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"


# Функция построения нового алфавита на основе сдвига
def get_new_alphabet(start_index):
    newAlphabet = ""
    for i in range(len(ALPHABET)):
        if i + start_index < len(ALPHABET):
            newAlphabet += ALPHABET[i + start_index]
        else:
            newAlphabet += ALPHABET[i - (len(ALPHABET) - start_index)]
    return newAlphabet


# Шифрование текста методом Вижинера
def encrypt_text(text: str, secret_word: str):
    encrypted_text = ""
    secret_word_iterator = 0
    for i in range(len(text)):
        # Если символ буква
        if text[i].isalpha():
            letter_position = ALPHABET.find(text[i].upper())
            new_alphabet = get_new_alphabet(ALPHABET.find(secret_word[secret_word_iterator].upper()))
            # Преобразуем кейс в оригинальный
            if text[i].isupper():
                encrypted_text += new_alphabet[letter_position]
            else:
                encrypted_text += new_alphabet[letter_position].lower()
            secret_word_iterator += 1
            if secret_word_iterator >= len(secret_word):
                secret_word_iterator = 0
        else:
            encrypted_text += text[i]
    return encrypted_text


# Расшифровка текста
def decrypt_text(encrypted_text: str, secret_word: str):
    decrypted_text = ""
    secret_word_iterator = 0
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            # Строим новый алфавит на основе буквы ключа
            new_alphabet = get_new_alphabet(ALPHABET.find(secret_word[secret_word_iterator].upper()))
            # Получаем позицию символа в алфавите
            letter_position = new_alphabet.find(encrypted_text[i].upper())
            if encrypted_text[i].isupper():
                decrypted_text += ALPHABET[letter_position]
            else:
                decrypted_text += ALPHABET[letter_position].lower()
            secret_word_iterator += 1
            if secret_word_iterator >= len(secret_word):
                secret_word_iterator = 0
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text
