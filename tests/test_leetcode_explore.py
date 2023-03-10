from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from libs.leetcode_explore import Leetcodeexplorepage
from data import config

username = config.username
password = config.password


def test_explore_leetcode(page):
    goto = Leetcodegotopage(page)
    login = Leetcodeloginpage(page)
    explore = Leetcodeexplorepage(page)
    goto.leetcodepage()
    login.login_credentials(username, password)
    explore.explorepage()
