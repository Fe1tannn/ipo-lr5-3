with open ("text.txt", "r", encoding="utf-8") as file: #Открываем файл
    a = file.read() #Сохраняем данные файла в переменной a
    b = a.split() #Сохраняем разделенные слова в список b
print(len(b)) #Выводим количество слов
