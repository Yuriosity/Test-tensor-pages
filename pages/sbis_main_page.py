from selenium.webdriver.common.by import By

class SbisMainPage:
    
    url = 'https://sbis.ru/'
    contacts_xpath = '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]'
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(SbisMainPage.url)
        
    def go_to_contacts(self):
        contancts_element = self.driver.find_element(By.XPATH, SbisMainPage.contacts_xpath)
        contancts_element.click()
        
    def close(self):
        self.driver.close()
        
    def current_url(self):
        return self.driver.current_url