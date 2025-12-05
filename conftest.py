import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """Добавление параметра language в командную строку"""
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, ru, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для создания браузера с нужным языком"""
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")

    # Настройки Chrome
    options = Options()

    # Устанавливаем язык браузера
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': user_language}
    )

    # Опционально: headless режим для CI/CD
    # options.add_argument("--headless")

    # Устанавливаем ChromeDriver через webdriver-manager
    service = Service(ChromeDriverManager().install())

    # Создаем браузер с настройками
    browser = webdriver.Chrome(service=service, options=options)

    # Настройки браузера
    browser.implicitly_wait(10)
    browser.maximize_window()

    # Возвращаем браузер тесту
    yield browser

    # Закрываем браузер после теста
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    """Фикстура для получения языка (опционально)"""
    return request.config.getoption("language")