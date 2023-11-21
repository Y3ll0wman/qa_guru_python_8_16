import pytest

from selene.support.shared import browser


@pytest.fixture(params=[(3840, 2160), (1920, 1080)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1024, 768), (800, 600)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(3840, 2160), (1920, 1080), (1024, 768), (800, 600)])
def is_desktop_browser(request):
    resolution = request.param
    if resolution in [(3840, 2160), (1920, 1080)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False


@pytest.fixture(params=[(3840, 2160), (1920, 1080), (1024, 768), (800, 600)])
def is_mobile_browser(request):
    resolution = request.param
    if resolution in [(1024, 768), (800, 600)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False
