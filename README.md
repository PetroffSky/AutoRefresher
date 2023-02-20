# AutoRefresher
Program for auto-updater resume 


Программа для поднятия позиции резюме в релевантном поиске на сайте HeadHunter.ru по таймеру.
Включает в себя 2 модуля и файл настроек.

Требования:
- установленнный Python 3 c Path по-умолчанию;
- установленный в venv Python модуль art: pip install art;
- установленный Python Selenium: pip install selenium; 
- установленный Chromedriver в C:\chromedriver и в Path;
- настройка файла settings.txt;

Альфа-версия.
В дальнейшем планируется:
- расширение возможностей настроек: проверка настроек, запрос настроек;
- переход структуры файла настроек с txt на json формат;
- хранение конструкций XML Path Language в файл настроек;
- добавление других ресурсов.

Запуск программы производится через start_settings.py.

Структура файла настроек:
https://hh.ru/applicant/resumes?hhtmFromLabel=header&hhtmFrom=negotiations_item
LOGIN
PASSWORD
1
