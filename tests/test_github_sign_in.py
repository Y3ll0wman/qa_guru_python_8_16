import pytest
from selene import browser, be, have


@pytest.mark.desktop
@pytest.mark.parametrize('window_width, window_height', [('3840', '2160'), ('1920', '1080')])
def test_github_sign_in_desktop(window_width, window_height):
    # GIVEN
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.open('https://github.com')

    # WHEN
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize('window_width, window_height', [('1024', '768'), ('800', '600')])
def test_github_sign_in_mobile(window_width, window_height):
    # GIVEN
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.open('https://github.com')

    # WHEN
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))


"""
- Параметризовать тест различным размером окна браузера;

- Обратите внимание, что для мобильной версии сайта потребуется другой автотест из-за изменения структуры локаторов;

- Сделайте два варианта пропуска неподходящих параметров и тестов.

1. Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот);

2. Переопределите параметр с помощью indirect;

3. Сделайте разные фикстуры для каждого теста.
"""

# тест один!
# В первом варианте использовать разные фикстуры (эти фикстуры отдельно параметризовать друг от друга)
# и вообще не использовать параметризацию в тесте

# Во втором варианте inderect параметризация. Есть фикстура которая параметризована всеми возможными разрешениями экрана,
# но для десктопа и для мобайла мы переопредеяем значения конкретными

# В третьем варианте параметризовать всеми возможными вариантами и в тесте если мы получили не подходящее разрешение
# экрана, например для десктопа - то пропускаем тест
