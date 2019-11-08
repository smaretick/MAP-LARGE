from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=options)
#driver.get("https://mapbeta.gvslabs.com/?profile=maplarge&mlSession=true&mlSessionTestMode=false&mode=both#/")
#driver.get("https://mapbeta.gvslabs.com/")
#driver.close()
