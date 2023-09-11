import tkinter.messagebox
from tkinter import *
from crypto_functions import *


class UserInterface:
    def __init__(self, title="Шифр бруска", size='700x400'):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(size)
        self.window.resizable(False, False)

        # Раздел "Зашифровать"
        self.label_encrypt_text = Label(self.window, text="Исходное сообщение:")
        self.label_encrypt_text.grid(column=0, row=1)
        self.label_encrypt_text.grid_forget()
        self.txt_encrypt_text = Entry(self.window, width=30)
        self.txt_encrypt_text.grid(column=0, row=2)
        self.txt_encrypt_text.grid_forget()
        self.label_encrypt_number_vertical = Label(self.window,
                                                   text="Введите количество букв, помещаемых по вертикали:")
        self.label_encrypt_number_vertical.grid(column=0, row=3)
        self.label_encrypt_number_vertical.grid_forget()
        self.txt_encrypt_number_vertical = Entry(self.window, width=10)
        self.txt_encrypt_number_vertical.grid(column=0, row=4)
        self.txt_encrypt_number_vertical.grid_forget()
        self.label_encrypt_number_horizontal = Label(self.window,
                                                     text="Введите количество букв, помещаемых по горизонтали:")
        self.label_encrypt_number_horizontal.grid(column=0, row=5)
        self.label_encrypt_number_horizontal.grid_forget()
        self.txt_encrypt_number_horizontal = Entry(self.window, width=10)
        self.txt_encrypt_number_horizontal.grid(column=0, row=6)
        self.txt_encrypt_number_horizontal.grid_forget()
        self.btn_encrypt_start = Button(self.window, text="Зашифровать", command=self.btn_encrypt_start_clicked)
        self.btn_encrypt_start.grid(column=0, row=7)
        self.btn_encrypt_start.grid_forget()

        self.btn_decrypt_start = Button(self.window, text="Расшифровать", command=self.btn_decrypt_start_clicked)
        self.btn_decrypt_start.grid(column=0, row=7)
        self.btn_decrypt_start.grid_forget()

        self.btn_hack_start = Button(self.window, text="Взломать", command=self.btn_hack_start_clicked)
        self.btn_hack_start.grid(column=0, row=7)
        self.btn_hack_start.grid_forget()

        # Раздел "Расшифровать"
        self.label_encrypt_answer = Label(self.window, text="Зашифрованное сообщение:")
        self.label_encrypt_answer.grid(column=0, row=8)
        self.label_encrypt_answer.grid_forget()
        self.text_encrypt_answer = Entry(self.window, width=30)
        self.text_encrypt_answer.grid(column=0, row=9)
        self.text_encrypt_answer.grid_forget()

        self.btn_encrypt = Button(self.window, text="Зашифровать", command=self.btn_encrypt_clicked)
        self.btn_encrypt.grid(column=0, row=0, padx=20, pady=20)

        self.btn_decrypt = Button(self.window, text="Расшифровать", command=self.btn_decrypt_clicked)
        self.btn_decrypt.grid(column=1, row=0, padx=20, pady=20)

        self.btn_hack = Button(self.window, text="Хакнуть", command=self.btn_hack_clicked)
        self.btn_hack.grid(column=2, row=0, padx=20, pady=20)

        self.current_mode = 'None'
        self.window.mainloop()

    # Нажатие на "зашифровать"
    def btn_encrypt_start_clicked(self):
        text = self.txt_encrypt_text.get()
        vertical_count = int(self.txt_encrypt_number_vertical.get())
        horizontal_count = int(self.txt_encrypt_number_horizontal.get())
        if len(text) > vertical_count * horizontal_count:
            return tkinter.messagebox.showwarning(title="Ошибка!", message=
            f'Текст размером {len(text)} не поместится на брусок размера {vertical_count} x {horizontal_count}!'
                                                  )
        encrypted_text = encrypt_text(text, horizontal_count, vertical_count)
        self.label_encrypt_answer.grid()
        self.text_encrypt_answer.delete(0, END)
        self.text_encrypt_answer.insert(0, encrypted_text)
        self.text_encrypt_answer.grid()

    # Нажатие на "расшифровать"
    def btn_decrypt_start_clicked(self):
        text = self.text_encrypt_answer.get()
        vertical_count = int(self.txt_encrypt_number_vertical.get())
        horizontal_count = int(self.txt_encrypt_number_horizontal.get())
        if (len(text) > vertical_count * horizontal_count):
            return tkinter.messagebox.showwarning(title="Ошибка!", message=
            f'Текст размером {len(text)} не поместится на брусок размера {vertical_count} x {horizontal_count}!'
                                                  )
        decrypted_text = decrypt_text(text, horizontal_count, vertical_count)
        self.label_encrypt_text.grid()
        self.txt_encrypt_text.delete(0, END)
        self.txt_encrypt_text.insert(0, decrypted_text)
        self.txt_encrypt_text.grid()

    # Нажатие на "хакнуть"
    def btn_hack_start_clicked(self):
        text = self.text_encrypt_answer.get()
        decrypted_text = hack_text(text)
        self.label_encrypt_text.grid()
        self.txt_encrypt_text.delete(0, END)
        self.txt_encrypt_text.insert(0, decrypted_text)
        self.txt_encrypt_text.grid()

    # Смена режима (вкладки)
    def change_mode(self, new_mode):
        if self.current_mode == new_mode:
            return
        self.current_mode = new_mode
        if new_mode == 'encrypt':
            self.label_encrypt_text.grid(row=1)
            self.txt_encrypt_text.grid(row=2)
            self.label_encrypt_text.grid()
            self.txt_encrypt_text.grid()
            self.label_encrypt_number_vertical.grid()
            self.txt_encrypt_number_vertical.grid()
            self.label_encrypt_number_horizontal.grid()
            self.txt_encrypt_number_horizontal.grid()
            self.btn_encrypt_start.grid()
            self.label_encrypt_answer.grid(row=8)
            self.text_encrypt_answer.grid(row=9)
            self.label_encrypt_answer.grid_forget()
            self.text_encrypt_answer.grid_forget()
            self.btn_decrypt_start.grid_forget()
            self.btn_hack_start.grid_forget()
        elif new_mode == 'decrypt':
            self.label_encrypt_answer.grid(row=1)
            self.text_encrypt_answer.grid(row=2)
            self.label_encrypt_number_vertical.grid()
            self.txt_encrypt_number_vertical.grid()
            self.label_encrypt_number_horizontal.grid()
            self.txt_encrypt_number_horizontal.grid()
            self.label_encrypt_text.grid(row=8)
            self.txt_encrypt_text.grid(row=9)
            self.label_encrypt_text.grid_forget()
            self.txt_encrypt_text.grid_forget()
            self.btn_encrypt_start.grid_forget()
            self.btn_decrypt_start.grid()
            self.btn_hack_start.grid_forget()
        elif new_mode == 'hack':
            self.label_encrypt_answer.grid(row=1)
            self.text_encrypt_answer.grid(row=2)
            self.label_encrypt_number_vertical.grid_forget()
            self.txt_encrypt_number_vertical.grid_forget()
            self.label_encrypt_number_horizontal.grid_forget()
            self.txt_encrypt_number_horizontal.grid_forget()
            self.label_encrypt_text.grid(row=8)
            self.txt_encrypt_text.grid(row=9)
            self.label_encrypt_text.grid_forget()
            self.txt_encrypt_text.grid_forget()
            self.btn_encrypt_start.grid_forget()
            self.btn_decrypt_start.grid_forget()
            self.btn_hack_start.grid()

    # Кнопки смены вкладки
    def btn_encrypt_clicked(self):
        self.change_mode('encrypt')

    def btn_decrypt_clicked(self):
        self.change_mode('decrypt')

    def btn_hack_clicked(self):
        self.change_mode('hack')
