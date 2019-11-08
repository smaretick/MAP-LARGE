from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
profile.acceptSslCerts = True
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://mapbeta.gvslabs.com/?profile=maplarge&mlSession=true&mlSessionTestMode=false&mode=both#/')
time.sleep(30);
driver.close()
