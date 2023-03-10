from playwright.sync_api import Page
from data import config


class Leetcodeloginpage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.username = page.locator("//input[@id='id_login']")
        self.password = page.locator("//input[@id='id_password']")
        self.loginbtn = page.locator(
            "//div[@class='btn-content-container__2HVS']")

    def login_credentials(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginbtn.click()
