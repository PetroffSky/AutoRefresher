import autorefresher
from art import tprint


def main():
    tprint('AutoUP', font="block")  # Заставка названия приложения
    print("Программа авто-обновления резюме работает!")
    print('Читаем настройки')
    with open('settings.txt', 'r', encoding='utf-8') as settings:
        sets = settings.read().split('\n')
        link, login, password, mode = sets[0], sets[1], sets[2], sets[3]
        print(f'Настройки прочитаны:\n',
              f'link: {link}\n',
              f'login: {login}\n',
              f'password: {password}\n',
              f'work_mode: {mode}')  # режим запуска скрипта: 1 - одна кнопка, 2 - много кнопок

    # Создаём экземпляр класса и запускаем скрипт движка работы с сайтом Head Hunter
    # Возвращаем ЭК для дальнейшей работы с ним
    run_instance = autorefresher.Engine(link, login, password, mode)
    return run_instance


if __name__ == "__main__":
    main()
    print(type(main()))






    # logger.add("debug.json", format="{time} {level} {message}",
    #            level='DEBUG', rotation="10 KB", serialize=True)
    # также параметр rotation поддерживает: вес файла - "10 МВ",
    # период обновления - "1 week", время обновления = "10:00"
    # компрессию zip: compression='zip'
    # serialize=True - поддержка json в дампе, debug.log лучше
    # переименовать в debug.json
    # декоратор @logger.catch поддерживает traceback исключений в файл дампа


