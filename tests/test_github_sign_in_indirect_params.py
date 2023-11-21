import pytest
from selene import browser, be, have


@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(3840, 2160), (1920, 1080)], indirect=True)
def test_github_sign_in_desktop(desktop_browser):
    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize("mobile_browser", [(1024, 768), (800, 600)], indirect=True)
def test_github_sign_in_mobile(mobile_browser):
    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()

    # THEN
    browser.element('#login').should(have.text('Sign in to GitHub'))
