from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class Engine:
    def __init__(self, link, login, password):
        self.link = link
        self.login = login
        self.password = password
        self.button_resume_up = ["//span[text()='Врач стоматолог терапевт-отропед-хирург']/../../../child::*[7]//span[text()='Поднять в поиске']",
                                 "//span[text()='Начинающий специалист тестировщик Python-Selenium']/../../../child::*[7]//span[text()='Поднять в поиске']"]
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
            for button in self.button_resume_up:
                if self.browser.find_element("xpath", button):
                    print('Кнопка авто-апдейта найдена!')
                    self.button_up_clicker(button)
        except NoSuchElementException as NSEE:
            print(f"Кнопка авто-апдейта не найдена: {type(NSEE).__name__} ")
        finally:
            self.auto_check(False)


    # Нажимаем указанную кнопку
    def button_up_clicker(self, button):
        auto_up_button = self.browser.find_element('xpath', button)
        print(auto_up_button.text)
        auto_up_button.click()
        print("Кнопку нажали")
