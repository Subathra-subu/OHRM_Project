from Actions.BaseActions import BaseActions
from Pages.buzzPage import buzzPage
from Pages.BasePage import BasePage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

            if not os.path.isfile(absolute_image_path):
                raise FileNotFoundError(
                    f"Image file not found: {absolute_image_path}"
                )

            self.logger.info(f"Image upload path: {absolute_image_path}")

            self.clickstale(BasePage.Buzz)
            self.clickstale(buzzPage.post_image)

            self.logger.info("Image post modal opened.")

            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(buzzPage.buzz_file_input)
            )

            file_element = self.driver.find_element(
                *buzzPage.buzz_file_input
            )

            self.logger.info("File input found in DOM.")

            file_element.send_keys(absolute_image_path)

            self.logger.info("Image path sent to file input.")

            WebDriverWait(self.driver, 30).until(
                lambda driver: len(
                    driver.find_elements(*buzzPage.buzz_file_input)
                ) > 0
            )

            self.logger.info("Waiting for image preview to load.")

            WebDriverWait(self.driver, 30).until(
                lambda driver: self._image_preview_loaded()
            )

            self.logger.info("Image preview loaded successfully.")

            self.wait_for_clickable(
                buzzPage.share_btn,
                timeout=30
            )

            self.logger.info("Share button is clickable.")

            self.clickstale(
                buzzPage.share_btn,
                timeout=30
            )

            self.logger.info("Share button clicked.")

            self.wait_for_visibility(
                buzzPage.posted_image,
                timeout=30
            )

            is_posted = self.is_displayed(
                buzzPage.posted_image
            )

            self.logger.info(
                f"Buzz - Image successfully uploaded. "
                f"Display Status on Feed: {is_posted}"
            )

            return is_posted

        except Exception as e:
            self.logger.error("Buzz - Sharing image flow failed")
            self.logger.exception(e)

            try:
                self.save_screenshot("buzz_image_share_failure")
            except Exception:
                pass

            raise

    def _image_preview_loaded(self):
        try:
            images = self.driver.find_elements(
                *buzzPage.image_preview
            )

            if not images:
                return False

            for image in images:
                try:
                    if image.is_displayed():
                        src = image.get_attribute("src")

                        if src and src.strip():
                            return True
                except Exception:
                    continue

            return False

        except Exception:
            return False

    def share_buzz_text(self, message):
        try:
            self.logger.info("Buzz - Sharing text post started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.clickstale(BasePage.Buzz)

            self.wait_for_visibility(buzzPage.textarea)
            self.enter_text(buzzPage.textarea, message)

            self.clickstale(buzzPage.postbutton)

            locator = buzzPage.posted_text_locator(message)

            self.wait_for_visibility(locator)

            posted_text = self.get_text(locator)

            self.logger.info(
                f"Buzz - Text posted successfully: {posted_text}"
            )

            return posted_text

        except Exception as e:
            self.logger.error("Buzz - Sharing text post failed")
            self.logger.exception(e)
            raise

    def edit_buzz_text(self, original_message, edited_message):
        try:
            self.logger.info("Buzz - Editing text post started")

            original_locator = buzzPage.posted_text_locator(original_message)

            self.wait_for_visibility(original_locator)
            self.clickstale(buzzPage.threedot)

            self.clickstale(buzzPage.editpostBUT)

            self.wait_for_visibility(buzzPage.textarea_edit)
           
            self.clear_and_enter_text(buzzPage.textarea_edit, edited_message)

            self.clickstale(buzzPage.edit_post_btn)

            edited_locator = buzzPage.posted_text_locator(edited_message)

            self.wait_for_visibility(edited_locator)

            posted_edited_text = self.get_text(edited_locator)

            self.logger.info(
                f"Buzz - Text edited successfully: {posted_edited_text}"
            )

            return posted_edited_text

        except Exception as e:
            self.logger.error("Buzz - Editing text post failed")
            self.logger.exception(e)
            raise

    def delete_buzz_text(self, message):
        try:
            self.logger.info("Buzz - Deleting text post started")

            locator = buzzPage.posted_text_locator(message)
            self.wait_for_visibility(locator)

            self.clickstale(buzzPage.threedot)
            self.clickstale(buzzPage.deletepostBUT)
            self.wait_for_visibility(buzzPage.delete_post_btn)
            self.clickstale(buzzPage.delete_post_btn)

            try:
                WebDriverWait(self.driver, 15).until(
                    EC.invisibility_of_element_located(locator)
                )
                self.logger.info(f"Buzz - Post deleted successfully: {message}")
                return True
            except TimeoutException:
                self.logger.warning(f"Buzz - Delete confirmation timed out for: {message}")
                return False

        except Exception as e:
            self.logger.error("Buzz - Deleting text post failed")
            self.logger.exception(e)
            raise