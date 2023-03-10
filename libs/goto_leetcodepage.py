from playwright.sync_api import Page
from data import config


class Leetcodegotopage:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://leetcode.com/")
        self.signbtn = page.locator("//span[normalize-space()='Sign in']")

    def leetcodepage(self):
        self.signbtn.click()
