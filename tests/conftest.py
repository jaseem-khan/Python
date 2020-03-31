import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("\n Running one time setUp")
    baseURL = "https://learn.letskodeit.com/"
    if browser == 'chrome':

        driver = webdriver.Chrome(r"C:\Users\JASEEM-KHAN\workspace\drivers\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("\n Running tests on Chrome")
    else:
        driver = webdriver.Firefox()
        driver.get(baseURL)
        print("\n Running tests on Firefox")

    if request.cls is not None:

        request.cls.driver = driver
        print(request.cls.driver)

    yield driver
    driver.quit()
    print("\n Running one time tearDown")



@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="class")
def practice():
    print("i am a practice method")