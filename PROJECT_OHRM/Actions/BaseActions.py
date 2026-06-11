from selenium.webdriver.support import expected_conditions as EC
from Utilities.Logger import log_generator


class BaseActions:

    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait
        self.logger = log_generator()

    
    def enter_text(self, locator, value):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()
            element.send_keys(str(value))

            self.logger.info(f"Entered : {value}")

        except Exception as e:

            self.logger.error("Failed to Enter Text")
            self.logger.exception(e)
            raise

    
    def click(self, locator):

        try:

            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

            self.logger.info("Element Clicked")

        except Exception as e:

            self.logger.error("Failed to Click")
            self.logger.exception(e)
            raise

   
   
    def get_text(self, locator):

        try:

            text = self.wait.until(
                EC.visibility_of_element_located(locator)
            ).text

            self.logger.info(f"Text : {text}")

            return text

        except Exception as e:

            self.logger.error("Failed to Get Text")
            self.logger.exception(e)
            raise

    
    def is_displayed(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except:
            return False

    
    def get_attribute(self, locator, attribute):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.get_attribute(attribute)

        except Exception as e:

            self.logger.exception(e)
            raise

   
    def clear(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()

        except Exception as e:

            self.logger.exception(e)
            raise

   
    def submit(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.submit()

        except Exception as e:

            self.logger.exception(e)
            raise