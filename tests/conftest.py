import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None # This is a way to make the driver global


# This is to take the browser name as a command line argument
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
# "--browser_name” is a key here, and we will give the value while running the py.test from the cmd prompt. - - This
# is also called as a HOOK By Doing this we can run the test from the CMD prompt like py.test --browser_name chrome


@pytest.fixture(scope="class")
def setup(request):
    global driver # Using the global driver
    browser_name = request.config.getoption("browser_name")  # Retrieving the browser_name value
    if browser_name == "chrome":
        service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/IEDriverServer.exe")
        driver = webdriver.Ie(service=service_obj)

    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

