from libs.goto_leetcodepage import Leetcodegotopage
from data import config

username = config.username
password = config.password


def test_gotopage(page):
    goto = Leetcodegotopage(page)
    goto.leetcodepage()
