from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class Engine:
    def __init__(self, link, login, password, mode):
        self.link = link
        self.login = login
        self.password = password
        self.mode = mode
        # self.button_resume_up = "//button[@data-qa='resume-update-button']"
        self.button_resume_up = "//button[@data-qa='resume-update-button_actions']"
        self.auto_refresher()

    # Авторизация в сервисе
    def auto_refresher(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        with webdriver.Chrome(options=options) as self.browser:
            self.browser.maximize_window()
            self.browser.get(self.link)
            self.browser.implicitly_wait(5)
            print('Авторизируемся на сервисе HeadHunter')
            print('Нажимаем кнопки авторизации')
            self.browser.find_element('xpath', "//button[@data-qa='expand-login-by-password']").click()
            set_login_field = self.browser.find_element('xpath', "//input[@inputmode]")
            set_login_field.send_keys(self.login)
            set_pass_field = self.browser.find_element('xpath', "//input[@placeholder='Пароль']")
            set_pass_field.send_keys(self.password)
            self.browser.find_element('xpath', "//button[@data-qa='account-login-submit']").click()
            result = self.check_button()
            if result == False:
                self.auto_check(False)

    # реализация авто-проверки
    def auto_check(self, button_ready):
        while not button_ready:
            print('Начинаем проверку доступности кнопки')
            button_ready = self.check_button()
            if not button_ready:
                print('Ожидаем доступность кнопки')
                self.pause_timer()
            print(button_ready)
        self.mode_selector()

    # Обработка счётчика времени
    def pause_timer(self):
        print(f"Период ожидания в 20 минут начат {time.asctime()}")
        for i in range(19):
            time.sleep(60)
            # time.sleep(1)
            print(f"До следующей проверки осталось {19 - i} минут")
        print("Время ожидания окончилось.")
        self.auto_check(False)


    # Проверка доступности кнопки button_resume_up
    def check_button(self):
        print('Проверяем доступность активной кнопки')
        try:
            if self.browser.find_element("xpath", self.button_resume_up):
                print('Кнопка авто-апдейта найдена!')
                self.mode_selector()
        except NoSuchElementException as NSEE:
            print(f"Кнопка авто-апдейта не найдена: {type(NSEE).__name__} ")
            return False


    # Выбор логики для Mode 1 или Mode 2
    def mode_selector(self):
        if self.mode == '1':
            print("Нажимаем одну кнопку")
            self.button_up_finder()
        if self.mode == '2':
            print("Нажимаем несколько кнопок")
            self.buttons_up_finder()
        else:
            print('не понятно')


    # Mode 1: нажатие одной кнопки "Поднять в поиске"
    def button_up_finder(self):
        auto_up_button = self.browser.find_element('xpath', self.button_resume_up)
        print(auto_up_button.text)
        if auto_up_button.text == "Поднять в поиске":
            auto_up_button.click()
            print("Кнопку нажали")
            self.auto_check(False)


    # Mode 2: выбор всех кнопок "Поднять в поиске" на странице в список и последовательное нажатие
    def buttons_up_finder(self):
        auto_up_buttons = self.browser.find_elements('xpath', self.button_resume_up)
        for button in auto_up_buttons:
            if auto_up_button.text == "Поднять в поиске":
                button.click()  # нажимаем последовательно кнопки на странице
                print("Одна из кнопок нажата")
                time.sleep(3)
        self.auto_check(False)

