from ..pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize('username, password, expect', [
    ('standard_user', 'secret_sauce', True),
    ('locked_out_user', 'secret_sauce', False),
    ('problem_user', 'secret_sauce', True),
    ('error_user', 'secret_sauce', True),
    ('visual_user', 'secret_sauce', True)
])
def test_login(username, password, expect, page):
    login_page = LoginPage(page)

    login_page.load()

    login_page.login(username, password)
    if expect:
        assert '/inventory.html' in page.url
    else:
        assert page.get_by_text('Epic sadface:').is_visible()