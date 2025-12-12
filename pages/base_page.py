class BasePage:
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = ""):
        url = self.base_url.rstrip("/") + "/" + path.lstrip("/")
        self.page.goto(url)
