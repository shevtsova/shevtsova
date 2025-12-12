import os
import pytest
from dotenv import load_dotenv

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://example.com"),
        help="Base URL for the tests"
    )

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("base_url")

@pytest.fixture
def login(page, base_url):
    """
    Пример фикстуры для логина: возвращает функцию, которую можно вызвать внутри теста.
    """
    def _login(username: str, password: str):
        page.goto(f"{base_url}/login")
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        return page
    return _login

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук: при падении теста сохраняем скриншот (если используется фикстура `page`).
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = os.getenv("SCREENSHOT_DIR", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            path = os.path.join(screenshots_dir, f"{item.name}.png")
            try:
                page.screenshot(path=path, full_page=True)
            except Exception:
                pass
