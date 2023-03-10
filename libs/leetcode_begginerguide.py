from data import config


class Leetcodebegginerpage:

    username = config.username
    password = config.password

    def __init__(self,page):
        self.page = page
        self.begginnerpage = page.locator("(//i[@class='icon fa fa-play'])[2]")

    def leet_begginnerpage(self):
        self.begginnerpage.click()