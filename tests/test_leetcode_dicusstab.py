from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from libs.leetcode_explore import Leetcodeexplorepage
from libs.leetcode_begginerguide import Leetcodebegginerpage
from libs.leetcode_problems import Leetcodeproblempage
from libs.weeklycontest332 import Leetcodeweeklypage
from libs.leetcode_discusstab import Leetcodediscusspage
from data import config

username = config.username
password = config.password

def test_leetcodediscuss(page):
    goto = Leetcodegotopage(page)
    login = Leetcodeloginpage()
    explore_page = Leetcodeexplorepage()
    begginer_page = Leetcodebegginerpage()
    problem_page = Leetcodeproblempage()
    contest_page = Leetcodeweeklypage()
    discuss_page = Leetcodediscusspage()
    goto.leetcodepage()
    login.login_credentials(username, password)
    explore_page.explorepage()
    begginer_page.leet_begginnerpage()
    problem_page.leetcodeproblemtab()
    contest_page.weeklycontestpage()
    discuss_page.discusspage()