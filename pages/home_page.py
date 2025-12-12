from pages.base_page import BasePage

class HomePage(BasePage):
    def title_text(self) -> str:
        # Возвращает заголовок страницы
        return self.page.title()
