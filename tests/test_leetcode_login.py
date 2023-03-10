from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from data import config

username = config.username
password = config.password


def test_login_leetcode(page):
    goto = Leetcodegotopage(page)
    Login = Leetcodeloginpage()
    goto.leetcodepage()
    Login.login_credentials(username, password)
