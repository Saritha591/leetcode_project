from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from libs.leetcode_explore import Leetcodeexplorepage
from libs.leetcode_begginerguide import Leetcodebegginerpage
from libs.leetcode_problems import Leetcodeproblempage
from libs.weeklycontest332 import Leetcodeweeklypage
from data import config

username = config.username
password = config.username

def test_contestpage(page):
    goto = Leetcodegotopage(page)
    login_page = Leetcodeloginpage(page)
    explore_page = Leetcodeexplorepage(page)
    begginer_page = Leetcodebegginerpage(page)
    problem_page = Leetcodeproblempage(page)
    contest_page = Leetcodeweeklypage(page)
    goto.leetcodepage()
    login_page.login_credentials(username, password)
    explore_page.explorepage()
    begginer_page.leet_begginnerpage()
    problem_page.leetcodeproblemtab()
    contest_page.weeklycontestpage()