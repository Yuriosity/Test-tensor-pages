from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SbisContactsPage:

    url = 'https://sbis.ru/contacts'
    banner_xpath = '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'
    change_region_xpath = '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
    list_of_partners_xpath = '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'
    input_select_region_xpath = '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/input'
    select_region_xpath = '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li/span'
    
    script_text_puller = """
        var parent = arguments[0];
        var child = parent.firstChild;
        var ret = "";
        while(child) {
            if (child.nodeType === Node.TEXT_NODE)
                ret += child.textContent;
            child = child.nextSibling;
        }
        return ret;
        """
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(SbisContactsPage.url)
    
    def go_to_banner_tensor(self):
        banner_tensor_element = self.driver.find_element(By.XPATH, SbisContactsPage.banner_xpath)
        banner_tensor_element.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def check_region(self):
        region_element = self.driver.find_element(By.XPATH, SbisContactsPage.change_region_xpath)
        return self.driver.execute_script(SbisContactsPage.script_text_puller, region_element)
        
    def check_list_of_partners(self):
        return self.driver.find_elements(By.XPATH, SbisContactsPage.list_of_partners_xpath)[0].text
             
    def open_change_region_window(self):
        window_element = self.driver.find_element(By.XPATH, SbisContactsPage.change_region_xpath)
        window_element.click()

    def change_region(self, region):
        self.open_change_region_window()
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SbisContactsPage.input_select_region_xpath)))
        search_region_element = self.driver.find_element(By.XPATH, SbisContactsPage.input_select_region_xpath)
        search_region_element.send_keys(region)

        sleep(1)
        
        region_element = self.driver.find_element(By.XPATH, SbisContactsPage.select_region_xpath)
        region_element.click()
    
    def close(self):
        self.driver.close()
        
    def current_url(self):
        return self.driver.current_url
    
    def title(self):
        return self.driver.title