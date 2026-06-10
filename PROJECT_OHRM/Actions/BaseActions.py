from selenium.webdriver.common.by import By
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
                EC.visibility_of_element_located((By.XPATH, locator))
            )

            element.clear()
            element.send_keys(str(value))

            self.logger.info(f"Entered '{value}' into {locator}")

        except Exception as e:
            self.logger.error("Failed to enter text")
            self.logger.exception(e)
            raise

    def click(self, locator):

        try:
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator))
            ).click()

            self.logger.info(f"Clicked {locator}")

        except Exception as e:
            self.logger.error("Failed to click element")
            self.logger.exception(e)
            raise

    def get_text(self, locator):

        try:
            text = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator))
            ).text

            self.logger.info(f"Text Found : {text}")

            return text

        except Exception as e:
            self.logger.error("Failed to get text")
            self.logger.exception(e)
            raise