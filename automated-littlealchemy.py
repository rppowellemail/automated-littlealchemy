import time

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://littlealchemy.com"


class Workbench:
    def __init__(self, driver):
        print "searching for workspace"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='workspace']")))
        print "workspace found"
        self.workspace = driver.find_element_by_xpath("//div[@id='workspace']")

        print "searching for library"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='library']")))
        print "library found"
        self.library = driver.find_element_by_xpath("//div[@id='library']")

    def get_elements(self):
        print "searching for elements"
        elements = self.library.find_elements_by_xpath(".//div[@class='element']")
        found = []
        for element in elements:
            n = element.find_element_by_xpath(".//div[@class='elementName']").text
            found.append(n)
        print "found:", found
        return found

    def get_element(self, e):
        s=".//div[@class='element']/div[contains(text(),'{0}')]".format(e)
        print s
        return self.library.find_element_by_xpath(".//div[@class='element']/div[contains(text(),'{0}')]".format(e))

    

if __name__ == "__main__":

    if (True):
        fp = selenium.webdriver.FirefoxProfile()
        driver = selenium.webdriver.Firefox(fp)
    else:

        driver = selenium.webdriver.PhantomJS()

    driver.get(url)

    print "loading..."
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='progressBar' and @style='opacity: 1;']")))
    print "finished loading"

    playButton = driver.find_element_by_xpath("//div[@class='playButton']")
    playButton.click()

    #driver.find_element_by_xpatih(xp).click()
    
    workbench = Workbench(driver)
    workbench.get_elements()
    
    print workbench.get_element('water')


    #driver.execute_script("
    #wait.until(EC.presence_of_element_located((By.XPATH, "//div[class='progressBar' and contains(@style='opacity: 1')]")))
    print "Done"
