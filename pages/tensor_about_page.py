from selenium.webdriver.common.by import By

from time import sleep

class TensorAboutPage:
    
    url = 'https://tensor.ru/about'
    first_image_in_working_xpath = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img'
    second_image_in_working_xpath = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img'
    third_image_in_working_xpath = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img'
    fourth_image_in_working_xpath = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img'
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(TensorAboutPage.url)
    
    def check_size_images_in_working(self):
        images = []
        images.append(self.driver.find_element(By.XPATH, TensorAboutPage.first_image_in_working_xpath))
        images.append(self.driver.find_element(By.XPATH, TensorAboutPage.second_image_in_working_xpath))
        images.append(self.driver.find_element(By.XPATH, TensorAboutPage.third_image_in_working_xpath))
        images.append(self.driver.find_element(By.XPATH, TensorAboutPage.fourth_image_in_working_xpath))
        return images
    
    def close(self):
        self.driver.close()
    
    def current_url(self):
        return self.driver.current_url
