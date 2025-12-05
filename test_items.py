import time


def test_product_page_should_have_add_to_cart_button(browser):
    """
    Тест проверяет, что страница товара содержит кнопку добавления в корзину.

    Steps:
    1. Открыть страницу товара
    2. Проверить наличие кнопки добавления в корзину
    3. Убедиться, что кнопка кликабельна
    """
    # Шаг 1: Открываем страницу товара
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(product_url)

    # Для проверки языка раскомментируйте следующую строку:
    # time.sleep(30)

    # Шаг 2: Проверяем наличие кнопки добавления в корзину
    # Используем уникальный селектор для этой страницы
    add_to_cart_button = browser.find_element(
        "css selector",
        ".btn-add-to-basket"
    )

    # Шаг 3: Проверяем что кнопка видима и кликабельна
    assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не отображается"
    assert add_to_cart_button.is_enabled(), "Кнопка добавления в корзину неактивна"

    # Дополнительно: проверяем что у кнопки есть текст (не пустая)
    button_text = add_to_cart_button.text.strip()
    assert button_text, "Текст на кнопке пустой"

    print(f"Найдена кнопка с текстом: '{button_text}'")


def test_product_page_elements(browser):
    """
    Дополнительный тест для проверки других элементов страницы товара.
    """
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    # Проверяем заголовок товара
    product_title = browser.find_element("css selector", ".product_main h1")
    assert product_title.is_displayed(), "Заголовок товара не отображается"

    # Проверяем цену товара
    product_price = browser.find_element("css selector", ".product_main .price_color")
    assert product_price.is_displayed(), "Цена товара не отображается"

    # Проверяем описание товара
    product_description = browser.find_element("css selector", "#product_description")
    assert product_description.is_displayed(), "Описание товара не отображается"