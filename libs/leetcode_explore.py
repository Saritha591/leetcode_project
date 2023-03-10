from data import config


class Leetcodeexplorepage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.explore = page.locator("//a[contains(text(),'Explore')]")

    def explorepage(self):
        self.explore.click()
