from Actions.BaseActions import BaseActions
from Pages.buzzPage import buzzPage
from Pages.BasePage import BasePage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
import os

class buzzActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    def share_buzz_image(self, relative_image_path):
        try:
            self.logger.info("Buzz - Sharing image flow started")
            LoginActions.login(
                self, 
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )
            absolute_image_path = os.path.abspath(relative_image_path)
            
            self.click(BasePage.Buzz)
            self.click(buzzPage.post_image)
            file_element = self.driver.find_element(*buzzPage.buzz_file_input)
            file_element.send_keys(absolute_image_path)
            
            self.wait_for_visibility(buzzPage.share_btn)
            self.click(buzzPage.share_btn)
            
            self.wait_for_visibility(buzzPage.posted_image)
            is_posted = self.driver.find_element(*buzzPage.posted_image).is_displayed()
            
            self.logger.info(f"Buzz - Image successfully uploaded. Display Status on Feed: {is_posted}")
            return is_posted
            
        except Exception as e:
            self.logger.error("Buzz - Sharing image flow failed")
            self.logger.exception(e)
            raise

    def share_buzz_text(self, message):
        try:
            self.logger.info("Buzz - Sharing text post started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.click(BasePage.Buzz)

            self.wait_for_visibility(buzzPage.textarea)
            self.enter_text(buzzPage.textarea, message)

            self.click(buzzPage.postbutton)

            locator = buzzPage.posted_text_locator(message)

            self.wait_for_visibility(locator)

            posted_text = self.get_text(locator)

            return posted_text

        except Exception as e:
            self.logger.error("Buzz - Sharing text post failed")
            self.logger.exception(e)
            raise