from data import config


class Leetcodeproblempage:

    username = config.username
    password = config.password

    def __init__(self,page):
        self.page = page 
        self.problempage = page.locator("//a[normalize-space()='Problems']")

    def leetcodeproblemtab(self):
        self.problempage.click()

    

    