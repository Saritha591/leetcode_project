from data import config


class Leetcodediscusspage:

    username = config.username
    password = config.password

    def __init__(self,page):
        self.page = page
        self.discusstab = page.locator("//li[normalize-space()='Discuss']")
        

    def discusspage(self):
        self.discusstab.click()