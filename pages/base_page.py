from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self,driver):
       self.driver = driver
       self.wait = WebDriverWait(driver,5)

    def click(self,by_locator):
        self.wait.until(expected_conditions.element_to_be_clickable(by_locator)).click()

    def send_keys(self,by_locator,text):
        self.wait.until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def find_element(self,by_locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(by_locator))

    def is_element_visible(self,by_locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_text(self,by_locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(by_locator)).text
