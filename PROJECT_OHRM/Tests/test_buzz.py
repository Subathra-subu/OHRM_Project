import pytest
import os
from Actions.buzzActions import buzzActions
from Utilities.Logger import log_generator

@pytest.mark.usefixtures("test_setup_and_down")
@pytest.mark.krishna
class Test_buzz:

    logger = log_generator()

    def test_successfully_share_buzz_photo(self):
        try:
            self.logger.info("******** Buzz Image Share Test Started ********")

            self.buzz = buzzActions(self.driver, self.wait)

            current_dir = os.path.dirname(os.path.abspath(__file__))
            image_relative_path = os.path.join(current_dir, "..", "test_data", "sample_data.jpg")

            self.logger.info(f"Resolving image upload file target path to: {image_relative_path}")
            is_image_visible = self.buzz.share_buzz_image(image_relative_path)
            
            assert is_image_visible, "The uploaded image is not visible on the Buzz feed timeline."
            
            self.logger.info("******** Buzz Image Share Test Passed ********")

        except Exception as e:
            self.logger.error("******** Buzz Image Share Test Failed ********")
            self.logger.exception(e)
            raise

    
    def test_successfully_post_buzz_text(self):
        try:
            self.logger.info("******** Buzz Text Post Test Started ********")

            self.buzz = buzzActions(self.driver, self.wait)

            message = "Automation Test Buzz Post"

            actual_text = self.buzz.share_buzz_text(message)

            assert actual_text == message, (
                f"Expected '{message}' but found '{actual_text}'"
            )

            self.logger.info("******** Buzz Text Post Test Passed ********")

        except Exception as e:
            self.logger.error("******** Buzz Text Post Test Failed ********")
            self.logger.exception(e)
            raise

    
    def test_successfully_edit_buzz_text(self):
        try:
            self.logger.info("******** Buzz Text Edit Test Started ********")

            self.buzz = buzzActions(self.driver, self.wait)

            original_message = "Automation Test Buzz Post"
            edited_message = "Edited Automation Test Buzz Post"

            # First, post the original message
            self.buzz.share_buzz_text(original_message)

            # Now, edit the posted message
            actual_edited_text = self.buzz.edit_buzz_text(original_message, edited_message)

            assert actual_edited_text == edited_message, (
                f"Expected '{edited_message}' but found '{actual_edited_text}'"
            )

            self.logger.info("******** Buzz Text Edit Test Passed ********")

        except Exception as e:
            self.logger.error("******** Buzz Text Edit Test Failed ********")
            self.logger.exception(e)
            raise    