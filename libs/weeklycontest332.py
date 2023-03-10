from data import config


class Leetcodeweeklypage:

    username = config.username
    password = config.password

    def __init__(self,page):
        self.page = page 
        self.weeklycontest332 = page.locator("//li[normalize-space()='Contest']")
        
        
        
    def weeklycontestpage(self):
        self.weeklycontest332.click()
        















