from libs.goto_leetcodepage import Leetcodegotopage
from libs.loginpage import Leetcodeloginpage
from libs.leetcode_explore import Leetcodeexplorepage
from libs.leetcode_begginerguide import Leetcodebegginerpage
from libs.leetcode_problems import Leetcodeproblempage
from libs.weeklycontest332 import Leetcodeweeklypage
from libs.leetcode_discusstab import Leetcodediscusspage
from playwright.sync_api import Page
from data import config

username = config.username
password = config.password


class TestDiscusspage:

    def test_leetcodediscuss(self,page: Page):
        goto = Leetcodegotopage(page)
        login = Leetcodeloginpage(page)
        explore_page = Leetcodeexplorepage(page)
        begginer_page = Leetcodebegginerpage(page)
        problem_page = Leetcodeproblempage(page)
        contest_page = Leetcodeweeklypage(page)
        discuss_page = Leetcodediscusspage(page)
        goto.leetcodepage()
        login.login_credentials(username, password)
        explore_page.explorepage()
        begginer_page.leet_begginnerpage()
        problem_page.leetcodeproblemtab()
        contest_page.weeklycontestpage()
        discuss_page.discusspage()