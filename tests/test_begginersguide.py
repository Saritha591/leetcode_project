from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from libs.leetcode_explore import Leetcodeexplorepage
from libs.leetcode_begginerguide import Leetcodebegginerpage
from data import config

username = config.username
password = config.password

def test_begginerpage(page):
    goto = Leetcodegotopage(page)
    login = Leetcodeloginpage(page)
    explore = Leetcodeexplorepage(page)
    begginer = Leetcodebegginerpage(page)
    goto.leetcodepage()
    login.login_credentials(username, password)
    explore.explorepage()
    begginer.leet_begginnerpage()



