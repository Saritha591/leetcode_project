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
    object = Leetcodegotopage(page)
    object_1 = Leetcodeloginpage(page)
    object_2 = Leetcodeexplorepage(page)
    object_3 = Leetcodebegginerpage(page)
    object_4 = Leetcodeproblempage(page)
    object_5 = Leetcodeweeklypage(page)
    object.leetcodepage()
    object_1.login_credentials(username, password)
    object_2.explorepage()
    object_3.leet_begginnerpage()
    object_4.leetcodeproblemtab()
    object_5.weeklycontestpage()