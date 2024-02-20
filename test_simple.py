import random

import pytest
import time

# pytestmark = pytest.mark.skip(reason="TASK-1234 Тест нестабильный потому что время от времени не хватает таймаута")


@pytest.fixture(scope="session")
def browser():
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


@pytest.fixture()
def user(browser):
    return random.randint(0, 49)


@pytest.mark.fast
@pytest.mark.skip(
    reason='Task 3501 не стабильный, не хватает таймаута'
)  # причина пропуска теста
def test_first(browser):
    time.sleep(1)


@pytest.mark.slow
@pytest.mark.usefixtures('browser')
def test_second(user):
    time.sleep(5)


@pytest.fixture()
def is_macos():
    return True


def test_third(is_macos):
    if is_macos:
        pytest.mark.skip(reason='Не запускается на МакОс')


# @pytest.mark.xfail(reason='')
def test_fail():
    user = random.randint(1, 100)
    user2 = random.randint(1, 100)
    try:
        assert user == user2
    except AssertionError:
        pytest.mark.xfail(reason='Task 112233')