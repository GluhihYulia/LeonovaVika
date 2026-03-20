def sortie(): #выход из библиотеки
    print("\nДо свидания!👋")
    
def ajouter(): #добавить книгу
    print("\nДобавьте книгу в библиотеку📗")
    auteur = input("Введите автора: ")
    nom = input("Введите название: ")
    genre = input("Введите жанр: ")
    resultat = auteur + " " + nom + " "  + genre + "\n"
    my_file = open("bibliotheque.txt", "a")
    my_file.write(resultat)
    my_file.close()
    
    
def regarder(): #посмотреть список книг
    print("\nСписок книг📋")
    try:
        my_file = open("bibliotheque.txt", "r")
        contenu = my_file.read()
        print(contenu)
        my_file.close()
    except FileNotFoundError:
        print("У вас нет добавленных книг")
     
    
def trier(): #отсортировать книги
    print("\nСортировка📑")
    try:
        my_file = open("bibliotheque.txt", "r")
        lines = my_file.readlines()
        lines.sort()
        for line in lines:
            print(line.rstrip())
        
    except FileNotFoundError:
         print("\nУ вас нет добавленных книг")    



def supprimer(): #удалить книгу
    print("\nУдаление книги❌")
    print("Функция скоро будет добавлена")

    
def ajouter_aux_favoris(): #добавить книгу в избранное
    print("\nДобавление книги в избранное✅")
    print("Функция скоро будет добавлена")

    
def supprimer_des_favoris(): #удалить книгу из избранного
    print("\nУдаление книги❎")
    print("Функция скоро будет добавлена")

    
def faute(): #ошибка
    print("\nПопробуйте ввести другое число")
   

while True:
    #меню для пользователя
    print("\nМЕНЮ 📑")
    print("Вы можете выбрать одно из действий в вашей библиотеке. Для этого просто выберите номер пункта в меню.")
    print("❶ Добавить книгу")
    print("❷ Посмотреть список книг")
    print("❸ Отсортировать книги")
    print("❹ Удалить книгу")
    print("❺ Добавить книгу в избранное")
    print("❻ Удалить книгу из избранного")
    print("❼ Выйти из библиотеки")
    answer = input("Введите номер действия: ")
    if answer == "7":
       sortie()
       break
    else:
        if answer == "1":
            ajouter()
        else:
            if answer == "2":
                regarder()
            else:
                if answer == "3":
                    trier()
                else:
                    if answer == "4":
                        supprimer()
                    else:
                        if answer == "5":
                            ajouter_aux_favoris()
                        else:
                            if answer == "6":
                                supprimer_des_favoris()
                            else:
                                faute()
            
