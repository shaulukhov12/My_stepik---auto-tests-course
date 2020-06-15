with open("C:\Users\A-SHAULUKHOV\Downloads\dataset_24465_4.txt", "r" ) as f, open("C:\Users\A-SHAULUKHOV\Downloads\Ответ.txt", "w" ) as w: #Рекомендуется так вызывать файл чтобы не было необходимости отдельно вызывать closed
    for line in f:
        w.write(line)

