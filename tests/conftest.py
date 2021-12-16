import pytest
from selenium import webdriver


driver = None   #Aula 103

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="class")
def setup(request):

    global driver #Aula 103

    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        pass
        #codigo para o chrome
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(8)
    driver.get("https://savee.it/lara_/boards/")
    driver.maximize_window()

    request.cls.driver = driver # para passar o driver para a class TestOne
    yield           #teardown
    driver.quit()

'''
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


#def _capture_screenshot(name):
    #driver.get_screenshot_as_file(name)
'''