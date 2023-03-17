from libs.goto_leetcodepage import Leetcodegotopage
from playwright.sync_api import Page
from data import config

username = config.username
password = config.password

class TestLeetcodegoto:

    def test_gotopage(self, page: Page):
        goto = Leetcodegotopage(page)
        goto.leetcodepage()
