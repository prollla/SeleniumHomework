import time

import allure


@allure.title("Тест на поиска текста на странице")
def test_main_page(browser, main_page):
    expected_text = 'Ситимобил — информационный сервис заказа транспортных и иных услуг, оказываемых партнерами. 0+'
    with allure.step("Открыть сайт"):
        main_page.open('https://city-mobil.ru/')
    with allure.step('Поиск элемента'):
        text_object = main_page.find_text()
    with allure.step('Проверка текста'):
        assert text_object.text == expected_text
