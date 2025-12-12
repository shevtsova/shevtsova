from pages.home_page import HomePage


def test_example_title(page, base_url):
    """
    Простой пример теста с использованием pytest-playwright fixture `page`
    и Page Object Model.
    """
    home = HomePage(page, base_url)
    home.goto()
    assert "Example Domain" in home.title_text()
