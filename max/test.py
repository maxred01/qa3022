import request
import pytest_check as check
import time


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на главную страницу")
def test_get_home_page():
    """ Вход на главную страницу. """
    start_time = time.time()

    Url = 'hhttps://test.com'
    headers = {
        "Accept-Language": "ru,en",  # добавляем язык агента
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = request.send_request_get('GET', Url, headers=headers, timeout=10)
    end_time = time.time()
    load_time = end_time - start_time
    # time.sleep(1)
    with allure.step("Проверка кода ответа"):
        if response.status_code == 404:
            # Проверяем, что на странице присутствует изображение 404
            check.is_in("/images/404", response.content.decode(),
                        "На странице отсутствует изображение 404")
        else:
            assert (response.status_code == 200), f"Неверный код ответа," \
                                                  f" получен {response.status_code}"
    with allure.step(f"Время загрузки страницы: {load_time:.2f} сек."):
        assert (load_time < 4), "Время загрузки страницы слишком долгое"
