import autorefresher
from art import tprint


def main():
    tprint('AutoUP', font="block")  # Заставка названия приложения
    print("Программа авто-обновления резюме работает!")
    print('Читаем настройки')
    with open('settings.txt', 'r', encoding='utf-8') as settings:
        sets = settings.read().split('\n')
        link, login, password = sets[0], sets[1], sets[2]
        print(f'Настройки прочитаны:\n',
              f'link: {link}\n',
              f'login: {login}\n',
              f'password: {password}\n')

    # Создаём экземпляр класса и запускаем скрипт движка работы с сайтом Head Hunter
    run_instance = autorefresher.Engine(link, login, password)



if __name__ == "__main__":
    main()
