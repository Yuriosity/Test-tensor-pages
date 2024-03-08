from selenium.webdriver.common.by import By

class TensorMainPage:
    
    url = 'https://tensor.ru/'
    about_xpath = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
    power_is_in_people_xpath = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'
    
    scroll_script = "arguments[0].scrollIntoView();"
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(TensorMainPage.url)
    
    def go_to_about(self):
        about_element = self.driver.find_element(By.XPATH, TensorMainPage.about_xpath)
        self.driver.execute_script(TensorMainPage.scroll_script, about_element)
        about_element.click()
    
    def find_power_is_in_people(self):
        power_element = self.driver.find_element(By.XPATH, TensorMainPage.power_is_in_people_xpath)
        self.driver.execute_script(TensorMainPage.scroll_script, power_element)
        return power_element.text
    
    def close(self):
        self.driver.close()    
    
    def current_url(self):
        return self.driver.current_url    