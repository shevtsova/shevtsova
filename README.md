# zignaly_ui_tests

Шаблон проекта для UI-тестов на Python с использованием Playwright.

Особенности:
- pytest + pytest-playwright
- Page Object Model (пример)
- Фикстуры для base_url и логина
- Скриншоты при падениях тестов
- GitHub Actions CI для запуска тестов

Требования
- Python 3.10+
- pip

Быстрая установка
1. Клонируйте репозиторий (или создайте виртуальное окружение в своей копии проекта)
2. Установите зависимости:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Установите браузеры Playwright:
```bash
playwright install
```

Настройки
- BASE_URL можно задать в .env или через опцию pytest `--base-url`
- Скриншоты сохраняются в директорию `screenshots/` (по умолчанию)

Запуск тестов
- Все тесты:
```bash
pytest
```
- Конкретный тест:
```bash
pytest tests/test_homepage.py::test_example_title -q
```
- Запуск в конкретном браузере (pytest-playwright поддерживает опцию `--browser`):
```bash
pytest --browser chromium
```

CI
- В `.github/workflows/ci.yml` настроен базовый pipeline, который устанавливает зависимости и запускает pytest.

Дальше можно добавить:
- авторизацию через API/сессии, чтобы ускорить тесты
- отчётность (Allure / pytest-html)
- параллелизация (pytest-xdist)
- тестовые данные/фабрики
