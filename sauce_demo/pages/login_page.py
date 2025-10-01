import allure

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder('Username')
        self.password = page.get_by_placeholder('Password')
        self.login_btn = page.get_by_role('button', name='Login')

    def load(self):
        with allure.step(f'Открываем браузер {self.page.context.browser.browser_type.name}'):
            self.page.goto('https://www.saucedemo.com/')


    def login(self, username, password):
        with allure.step(f'логинимся под {username}'):
            self.username.fill(username)
            self.password.fill(password)
            self.login_btn.click()
