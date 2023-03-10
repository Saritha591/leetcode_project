from playwright.sync_api import sync_playwright
from data import config


class Leetcodetraceviewer:

    username = config.username
    password = config.password

    def traceviewer(self,page):
        with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        # start tracing
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()

