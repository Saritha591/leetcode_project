import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def browser(launch_browser: Callable[[], Browser]) -> Generator[Browser, None, None]:
     browser = launch_browser()