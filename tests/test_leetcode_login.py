from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from playwright.sync_api import Page
from data import config

username = config.username
password = config.password

class TestLeetcodelogin:

    def test_login_leetcode(self, page:Page):
        goto = Leetcodegotopage(page)
        Login = Leetcodeloginpage(page)
        goto.leetcodepage()
        Login.login_credentials(username, password)
