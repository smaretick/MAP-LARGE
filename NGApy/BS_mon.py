from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '62.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768'
}

driver = webdriver.Remote(
    command_executor='http://smaretick3:gqzxib7a1Gwg8bbNAyNm@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://mapbeta.gvslabs.com/?profile=maplarge&mlSession=true&mlSessionTestMode=false&mode=both#/")
print driver.title
driver.quit()
